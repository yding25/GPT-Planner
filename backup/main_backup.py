from task_planner import task_planner
from plan_manager import plan_manager
from translator import translator
from situation_simulator import situation_simulator
from plan_monitor import plan_monitor
from backup.print_file import print_file
from backup.read_plan import read_plan
from plan_modifier_add_constraint import plan_modifier_add_constraint
import getpass
from os.path import exists
# from llm2 import llm2

# select a task
task_id = 4
task_name = 'drinking water'

# ------------------------------------------
# call basic symbolic task planner
# ------------------------------------------
user = getpass.getuser()
path_domain = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_basic.pddl'
path_problem = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_basic.pddl'
# path_problem = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_basic_2.pddl'

name_output = 'basic_plan'
path_plan = task_planner(path_domain, path_problem, name_output)
print_file(path_plan)
plan = read_plan(path_plan)

# ------------------------------------------
# simulate situation
# ------------------------------------------
situation_curr, opp_situation_curr, situation_predicate, situation_step = situation_simulator(task_id)
print('#----------simulate situation-----------')
print('situation, step, and corresponding predicate:', situation_curr, situation_step, situation_predicate)

# ------------------------------------------
# extract the i-th action using plan manager
# ------------------------------------------
print('#----------plan manager extract i-th action for robot-----------')
executed_action_list = []
for next_step in range(len(plan)):
    nextaction_encoded = plan_manager(next_step, path_plan)
    joint_rule = ' '
    # print('next action:', joint_rule.join(nextaction_encoded))

    # ------------------------------------------
    # decode next action
    # ------------------------------------------
    nextaction_decoded = translator(nextaction_encoded)
    print('next action (decoded):', nextaction_decoded)

    # ------------------------------------------
    # plan monitor
    # ------------------------------------------
    result_remaining_action_list = []
    if situation_step in nextaction_encoded:
        print('#---------- the situation exists, call plan monitor-----------')

        # plan_steps = ''
        # for step_id in range(len(executed_action_list)):
        #     plan_steps = plan_steps + 'Step ' + str(step_id + 1) + ': ' + executed_action_list[step_id] + ' '

        # check if next actions can be executed
        remaining_action_list = plan[next_step:]
        for remaining_action in remaining_action_list:
            remaining_action_decoded = translator(remaining_action)
            print('remaining action (decoded):', remaining_action_decoded)
            # design prompt
            plan = '###\nTask name: ' + task_name + '\n'
            # plan = '###\nTask name: ' + task_name + '\nPlan: ' + plan_steps
            situation = '\nSituation: ' + situation_curr
            nextaction = '\nNext action: ' + remaining_action_decoded
            question = '\nQuestion: can the next action still be executed?\nAnswer:'
            prompt_missing = plan + situation + nextaction + question
            result = plan_monitor(prompt_missing)
            print('result from plan monitor:', result)
            result_remaining_action_list.append(result)

    result_plan_monitor = False
    for result in result_remaining_action_list:
        if 'not' in result:
            result_plan_monitor = True
            break

    # ------------------------------------------
    # if the next action cannot be executed
    # ------------------------------------------
    if result_plan_monitor:
        print('#---------- final decision from plan mointor -----------')
        print('the current plan cannot be executed due to the situation!')

        # ------------------------------------------
        # call plan_modifier_add_constraint
        # ------------------------------------------
        print('#---------- call plan_modifier_add_constraint -----------')
        domain_path_new1, problem_path_new1 = plan_modifier_add_constraint(nextaction_encoded, situation_predicate,
                                                                           path_domain, path_problem, task_id)
        try:
            name_output = 'modified_plan1'
            path_plan_new1 = task_planner(domain_path_new1, problem_path_new1, name_output)
            print_file(path_plan_new1)
        except:
            print('#---------- No plan found! -----------')

        # ------------------------------------------
        # call plan_modifier_remove_constraint
        # ------------------------------------------
        if not exists(path_plan_new1):
            print('TBD: no path_plan_new1')

        # ------------------------------------------
        # call llm2
        # ------------------------------------------
        # target_appliance = llm2(nextaction_encoded, situation_curr, opp_situation_curr)

        # ------------------------------------------
        # call plan_modifier_add_effect
        # ------------------------------------------
        if not exists(path_plan_new1):
            print('#---------- call plan_modifier_add_effect -----------')
            # domain_path_new3, problem_path_new3 = plan_modifier_add_constraint(nextaction_encoded, situation_curr,
            #                                                                    path_domain, path_problem, task_id)

    else:
        executed_action_list.append(nextaction_decoded)
