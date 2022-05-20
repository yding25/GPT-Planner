import random
import getpass
import numpy as np
import os

# ------------------------------------------
# customized modules
# ------------------------------------------
from utility import task_planner, exist_remove, random_remove, extract_objects, locate_object, select_object, select_appliance, print_plan, print_file, read_plan, print_list, plan_manager, plan_monitor
from situation_simulator import situation_simulator
from action_translator import action_translator
from plan_modifier_add_constraint import plan_modifier_add_constraint
from llm_object import llm_object, llm_object_most, plan_modifier_add_effect_object
from llm_appliance import llm_appliance, llm_appliance_most, plan_modifier_add_effect_appliance

# ------------------------------------------
# select a task to execute
# ------------------------------------------
task_id = 11
task = {
    1: 'cleaning dirty area beside a table',
    4: 'filling a cup with water from faucet',
    6: 'setting a table to eat steak',
    9: 'putting a dirty plate in a sink',
    10: 'pouring coke into a glass',
    11: 'eating a burger on a plate'
}
task_name = task[task_id]

# ------------------------------------------
# some options of open world planner
# ------------------------------------------
option1 = 'suitable'  # level of plan monitor
option2 = 'suitable'  # level of llm object

ratio1 = 2  # 1/ratio objects are available in the case
ratio2 = 2

# ------------------------------------------
# if old file exists, remove them before running
# ------------------------------------------
exist_remove(task_id)

# ------------------------------------------
# if old file exists, remove them before running
# ------------------------------------------
random_remove(task_id)

# ------------------------------------------
# call classical task planner
# ------------------------------------------
user = getpass.getuser()
# setting == 0: world only have one objects that robot can manipulate
# setting == 1: ~~ two objects ~~
setting = np.random.choice(list(range(0, 2)), p=np.array([0.75, 0.25]))
print('setting:%d\n' % setting)
path_domain = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_basic.pddl'
if setting == 0:
    path_problem = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_basic.pddl'
else:
    path_problem = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_basic_2.pddl'
# test
# path_problem = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_basic.pddl'
# path_problem = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_basic_2.pddl'
try:
    path_plan = 'task_' + str(task_id) + '_basic_plan.txt'
    path_plan = task_planner(path_domain, path_problem, path_plan)
    print('#---------- generating basic plan! -----------')
    plan = read_plan(path_plan)
    print_plan(path_plan)
except:
    print('Error: no basic plan found!')

# ------------------------------------------
# call situation simulator
# ------------------------------------------
situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action = situation_simulator(task_id)
objects = extract_objects(path_plan)
situation_object_new = locate_object(situation_object, objects)
if '_' in situation_action:
    manipulate_object = situation_action.split('_')[1]
    manipulate_object_new = locate_object(manipulate_object, objects)
else:
    manipulate_object = 'None'
    manipulate_object_new = 'None'
print('\n#---------- generating situation! -----------')
print('situation index:', situation_index)
print('situation:', situation.replace(situation_object, situation_object_new))
print('action corresponding to situation:', situation_action)
print('corresponding predicate:', situation_predicate)
print('object manipulated by robot:', manipulate_object_new)
print('object in situation:', situation_object_new)

# ------------------------------------------
# call plan manager
# ------------------------------------------
print('\n#---------- executing plan! -----------')
result_monitor = False  # if action can be executed
signal_traversed = False  # if all actions in the checklist are examined
action_index = 0
while action_index < len(plan) and (not result_monitor) and (not signal_traversed):
    action_encoded = plan_manager(action_index, path_plan)
    action_decoded, action_decoded2 = action_translator(action_encoded, task_id)  # decode next action
    print('action:', action_encoded)
    print('action (decoded):', action_decoded)
    if situation_action not in action_encoded:
        print('this action is executed!\n')
        action_index += 1
    else:
        print('\n#---------- checking unexecuted actions! -----------')
        check_list = plan[action_index:]
        print_list(check_list)
        counter_check = 0
        for checked_action in check_list:
            counter_check = counter_check + 1
            if '_' in checked_action[0]:  # skip checking some actions, such as 'walk'
                checked_action_decoded, checked_action_decoded2 = action_translator(checked_action, task_id)
                print('\nunexecuted action:', checked_action)
                print('unexecuted action (decoded):', checked_action_decoded)
                # ------------------------------------------
                # call plan monitor
                # ------------------------------------------
                result_monitor = plan_monitor(task_id, situation, checked_action_decoded2, option1)
                if result_monitor:
                    print('#---------- current plan cannot be executed! -----------')
                    break
                else:
                    print('#---------- action can be executed! -----------')
                    if counter_check == len(check_list):
                        signal_traversed = True
            else:
                continue

if result_monitor:  # if plan cannot be executed
    # ------------------------------------------
    # call plan_modifier_add_constraint
    # ------------------------------------------
    print('\n#---------- adding constraint -----------')
    domain_path_new1, problem_path_new1 = plan_modifier_add_constraint(task_id, situation_action, situation_predicate, situation_object, situation_object_new, path_domain, path_problem)
    try:
        print('\n#---------- generating modified_plan_1! -----------')
        file_name = 'task_' + str(task_id) + '_modified_plan_1.txt'
        path_plan_modified_1 = task_planner(domain_path_new1, problem_path_new1, file_name)
        print_file(path_plan_modified_1)
    except:
        print('#---------- no modified_plan_1 found! -----------\n')
    # ------------------------------------------
    # call llm_object and plan_modifier_add_effect_object
    # ------------------------------------------
    if not os.path.exists(path_plan_modified_1):
        print('\n#---------- call llm_object -----------')
        object_list = select_object(task_id, ratio1)
        print('#---------- object that robot can operate: ----------\n', object_list)
        # ------------------------------------------
        # call llm_object
        # ------------------------------------------
        capable_objects = []  # save potentially useful objects
        if len(object_list) > 0:
            for item in object_list:
                if llm_object(task_id, path_plan, situation_object, item, option2):
                    capable_objects.append(item)
        else:
            print('Error: no object are selected!')
        if len(capable_objects) > 0:
            print('\n#---------- capable_objects: ----------\n', capable_objects)
        else:
            print('\n#---------- capable_objects: ----------\nNone')
        # ------------------------------------------
        # call llm_object_most
        # ------------------------------------------
        selected_object = ''
        if len(capable_objects) == 1:
            selected_object = random.choice(capable_objects)
            print('\n#---------- most possible object: ---------- \n', selected_object)
        elif len(capable_objects) > 1:
            # note, if there are too many objects, gpt-3 cannot work.
            selected_object = llm_object_most(task_id, task_name, situation, situation_object, capable_objects)
            print('\n#---------- most possible object: ---------- \n', selected_object)
        else:
            print('\n#---------- most possible object: ---------- \nNone')
        # ------------------------------------------
        # add effect
        # ------------------------------------------
        if selected_object:
            print('\n#---------- add effect -----------')
            temp = selected_object.split(' ')
            if len(temp) > 1:
                selected_object = '_'.join(temp)
            domain_path_new2, problem_path_new2 = plan_modifier_add_effect_object(task_id, situation_predicate, situation_object, situation_object_new, selected_object, domain_path_new1, problem_path_new1)
            try:
                print('\n#---------- generating modified_plan_2! -----------')
                file_name = 'task_' + str(task_id) + '_modified_plan_2.txt'
                path_plan_modified_2 = task_planner(domain_path_new2, problem_path_new2, file_name)
                # print_plan(path_plan_modified_2)
            except:
                print('\nno modified_plan_2 found!')
        else:
            print('\nno modified_plan_2 found!')

        # ------------------------------------------
        # call llm_appliance and plan_modifier_add_effect_appliance
        # ------------------------------------------
        print('\n#---------- call llm_appliance -----------')
        appliance_list = select_appliance(ratio2)
        print('appliance that robot can operate:', appliance_list)
        # ------------------------------------------
        # call llm_appliance
        # ------------------------------------------
        capable_appliances = []
        for candidate_appliance in appliance_list:
            if llm_appliance(situation, situation_opp, candidate_appliance, task_id):
                capable_appliances.append(candidate_appliance)
        if len(capable_appliances) > 0:
            print('\ncapable appliances:', capable_appliances)
        # ------------------------------------------
        # call llm_appliance_most
        # ------------------------------------------
        selected_appliance = ''
        if len(capable_appliances) == 1:
            selected_appliance = random.choice(capable_appliances)
            print('\n#---------- most possible appliance:\n', selected_appliance)
        elif len(capable_appliances) > 1:
            selected_appliance = llm_appliance_most(situation, situation_opp, capable_appliances,
                                                             task_id)
            print('\n#---------- most possible appliance:\n', selected_appliance)
        else:
            print('\nno capable appliance found!')
        # ------------------------------------------
        # add effect
        # ------------------------------------------
        if selected_appliance:
            print('\n#---------- add effect -----------')
            temp = selected_appliance.split(' ')
            if len(temp) > 1:
                selected_appliance = '_'.join(temp)
            domain_path_new3, problem_path_new3 = plan_modifier_add_effect_appliance(task_id, situation_predicate, situation_object, selected_appliance, domain_path_new1, problem_path_new1)
            try:
                print('\n#---------- modified_plan_3! exists -----------')
                file_name = 'task_' + str(task_id) + '_modified_plan_3.txt'
                path_plan_modified_3 = task_planner(domain_path_new3, problem_path_new3, file_name)
                # print_file(path_plan_modified_3)
            except:
                print('\nno modified_plan_3 found!')
        else:
            print('\nno modified_plan_3 found!')

        # ------------------------------------------
        # modified_plan_1, modified_plan_2 or modified_plan_3?
        # ------------------------------------------
        print('\n#---------- solution -----------')
        path9 = '/home/' + user + '/GPT-Planner/task_' + str(task_id) + '_modified_plan_1.txt'
        path10 = '/home/' + user + '/GPT-Planner/task_' + str(task_id) + '_modified_plan_2.txt'
        path11 = '/home/' + user + '/GPT-Planner/task_' + str(task_id) + '_modified_plan_3.txt'
        if os.path.exists(path9):
            print_plan(path_plan_modified_1)
        elif os.path.exists(path10) and os.path.exists(path11):
            print('both modified_plan_2 and modified_plan_3 exist.')
            if '2' in np.random.choice(['modified_plan_2', 'modified_plan_3'], p=np.array([0.5, 0.5])):
                print('randomly select modified_plan_2\n')
                print_plan(path_plan_modified_2)
            else:
                print('randomly select modified_plan_3\n')
                print_plan(path_plan_modified_3)
        elif os.path.exists(path10) and not os.path.exists(path11):
            print('only modified_plan_2 exists.\n')
            print_plan(path_plan_modified_2)
        elif not os.path.exists(path10) and os.path.exists(path11):
            print('only modified_plan_3 exists.\n')
            print_plan(path_plan_modified_3)
        else:
            print('none of modified_plan_1, modified_plan_2 and modified_plan_3 exist.')