import random
from os.path import exists
import getpass
from random import sample
import time
import numpy as np

# ------------------------------------------
# customized modules
# ------------------------------------------
from utility import task_planner, print_plan, print_file, read_plan, print_list, plan_manager, plan_monitor
from situation_simulator import situation_simulator
from action_translator import action_translator
from plan_modifier_add_constraint import plan_modifier_add_constraint
from llm_utensil import llm_utensil_actionknowledge, llm_utensil_most_possible, plan_modifier_add_effect_utensils
from llm_appliance import llm_appliance, llm_appliance_most_possible, plan_modifier_add_effect_appliances

# ------------------------------------------
# select a task to perform
# ------------------------------------------
# task_id = 1
# task_name = 'clean floor'
task_id = 4
task_name = 'drink water'
# task_id = 6
# task_name = 'set up a table'
# task_id = 9
# task_name = 'pick up plate'
# task_id = 10
# task_name = 'drink coke'
# ------------------------------------------
# some options of open world planner; different versions
# ------------------------------------------
# level of plan monitor
# option1 = 'possible'
option1 = 'acceptable'
# option1 = 'suitable'

# level of llm utensil
# option2 = 'possible'
# option2 = 'acceptable'
option2 = 'suitable'

# level of llm appliance
option3 = 'possible'
# option3 = 'acceptable'
# option3 = 'suitable'

# print('option1:', option1)
# print('option2:', option2)
# print('option3:', option3)

ratio1 = 2  # 1/ratio objects will be tested
ratio2 = 2  # 1/ratio objects will be tested
# ------------------------------------------
# call task planner
# ------------------------------------------
user = getpass.getuser()
p_file = np.array([0.8, 0.2])
index_file = np.random.choice(list(range(0, 2)), p=p_file)
path_domain = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_basic.pddl'
if index_file == 0:
    path_problem = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_basic.pddl'
else:
    path_problem = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_basic_2.pddl'
# test
path_problem = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_basic_2.pddl'

try:
    file_name = 'task_' + str(task_id) + '_basic_plan.txt'
    path_plan = task_planner(path_domain, path_problem, file_name)
    # print(path_plan)
    print('#---------- generating basic_plan! -----------')
    print_plan(path_plan)
    plan = read_plan(path_plan)
except:
    print('#---------- no basic_plan found! -----------')

# ------------------------------------------
# call situation simulator
# ------------------------------------------
situation_curr, opp_situation_curr, situation_object, situation_predicate, situation_action = situation_simulator(task_id)
print('\n#---------- generating situation! -----------')
print('situation:', situation_curr)
print('corresponding predicate:', situation_predicate)
# two types of objects: one is object in situation; one is object that manipulated by robots
print('object in situation:', situation_object)
print('action that has situation:', situation_action)
if '_' in situation_action:  # avoid some actions, such as walk
    manipulate_object = situation_action.split('_')[1]
else:
    manipulate_object = 'None'
print('object manipulated by robot:', manipulate_object)

# ------------------------------------------
# call plan manager
# ------------------------------------------
print('\n#---------- executing plan! -----------')
executed_action_list = []  # record actions that are executed
result_plan_monitor = False  # if action can be executed
signal_traversed = False  # if all actions in the checklist are examined
next_action_index = 0
while next_action_index < len(plan) and (not result_plan_monitor) and (not signal_traversed):
    next_action_encoded = plan_manager(next_action_index, path_plan)
    next_action_decoded = action_translator(next_action_encoded, task_id)  # decode next action
    print('next action:', next_action_encoded)
    print('next action (decoded):', next_action_decoded)
    if situation_action not in next_action_encoded:  # situation corresponds to an action
        print('this action is executed!\n')
        executed_action_list.append(next_action_decoded)
        next_action_index += 1
    else:
        print('\n#---------- checking unexecuted actions! -----------')
        check_list = plan[next_action_index:]
        print_list(check_list)
        counter_check = 0
        for checked_action in check_list:
            # ------------------------------------------
            # Need all actions to be checked? No. some actions should be skipped, such as 'walk'
            # ------------------------------------------
            counter_check = counter_check + 1
            if '_' in checked_action[0]:
                checked_action_decoded = action_translator(checked_action, task_id)
                print('\nunexecuted action:', checked_action)
                print('unexecuted action (decoded):', checked_action_decoded)
                # ------------------------------------------
                # call plan monitor
                # ------------------------------------------
                result_plan_monitor = plan_monitor(situation_curr, checked_action_decoded, option1, task_id)
                if result_plan_monitor:
                    print('#---------- current plan cannot be executed! -----------')
                    break
                else:
                    print('#---------- action can be executed! -----------')
                    if counter_check == len(check_list):
                        signal_traversed = True
            else:
                continue


if result_plan_monitor:  # plan cannot be executed
    # ------------------------------------------
    # call plan_modifier_add_constraint
    # ------------------------------------------
    print('\n#---------- adding constraint -----------')
    domain_path_new1, problem_path_new1 = plan_modifier_add_constraint(next_action_encoded, situation_predicate, situation_object, manipulate_object, path_domain, path_problem, task_id)
    try:
        print('\n#---------- generating modified_plan_1! -----------')
        file_name = 'task_' + str(task_id) + '_modified_plan_1'
        path_plan_modified_1 = task_planner(domain_path_new1, problem_path_new1, file_name)
        print_file(path_plan_modified_1)
    except:
        path_plan_modified_1 = 'None'
        print('#---------- no modified_plan_1 found! -----------\n')

    # ------------------------------------------
    # call llm_utensils and plan_modifier_add_effect
    # ------------------------------------------
    if not exists(path_plan_modified_1):
        print('\n#---------- call llm_utensils -----------')
        if task_id == 1 or task_id == 4 or task_id == 6 or task_id == 9:
            filein = open('dataset/utensils_processed.txt')  # read utensil
        if task_id == 10:
            filein = open('dataset/beverage_utensils.txt')  # read utensil + beverage
        if task_id == 11:
            filein = open('dataset/food_utensils_furniture.txt')  # read utensil
        all_utensil_list = []
        for line in filein.readlines():
            line = line.strip()
            joint_rule = ''
            all_utensil_list.append(joint_rule.join(line))
        utensil_list = sample(all_utensil_list, round(len(all_utensil_list)/ratio1))
        print('#---------- utensil that robot can operate: ----------\n', utensil_list)
        # ------------------------------------------
        # use 'replace' -- external knowledge;
        # ------------------------------------------
        # capable_utensils = []
        # for candidate_utensil in utensil_list:
        #     if llm_utensil(situation_object, task_name, candidate_utensil):
        #         capable_utensils.append(candidate_utensil)
        # if len(capable_utensils) > 0:
        #     print('\n#---------- capable utensils: ---------- \n', capable_utensils)
        # else:
        #     print('\n#---------- capable utensils: ---------- \n None')
        # ------------------------------------------
        # use 'action knowledge'
        # ------------------------------------------
        capable_utensils_actionknowledge = []
        if len(utensil_list) > 0:
            for candidate_utensil in utensil_list:
                if llm_utensil_actionknowledge(path_plan, plan, task_id, situation_curr, situation_object, task_name, candidate_utensil, option2):
                    capable_utensils_actionknowledge.append(candidate_utensil)
        else:
            print('Error -- no utensil are selected!')
        if len(capable_utensils_actionknowledge) > 0:
            print('#---------- capable_utensils_actionknowledge: ----------\n', capable_utensils_actionknowledge)
        else:
            print('#---------- capable_utensils_actionknowledge: ----------\nNone')
        # ------------------------------------------
        # use 'most possible' -- external knowledge
        # ------------------------------------------
        selected_utensil = ''
        if len(capable_utensils_actionknowledge) == 1:
            selected_utensil = random.choice(capable_utensils_actionknowledge)
            print('\n#---------- most possible utensil: ---------- \n', selected_utensil)
        elif len(capable_utensils_actionknowledge) > 1:
            selected_utensil = llm_utensil_most_possible(situation_curr, situation_object, task_name, capable_utensils_actionknowledge, task_id)
            print('\n#---------- most possible utensil: ---------- \n', selected_utensil)
        else:
            print('\n#---------- capable utensils: ---------- \nNone')
        # ------------------------------------------
        # add effect
        # ------------------------------------------
        if selected_utensil:
            print('\n#---------- add effect -----------')
            temp = selected_utensil.split(' ')
            if len(temp) > 1:
                selected_utensil = '_'.join(temp)
            domain_path_new2, problem_path_new2 = plan_modifier_add_effect_utensils(situation_predicate, situation_object, selected_utensil, domain_path_new1, problem_path_new1, task_id)
            try:
                print('\n#---------- generating modified_plan_2! -----------')
                file_name = 'task_' + str(task_id) + '_modified_plan_2'
                path_plan_modified_2 = task_planner(domain_path_new2, problem_path_new2, file_name)
                print_plan(path_plan_modified_2)
                signal_appliance = 0  # binary result to indicate if robot need to try 'operate appliance'
            except:
                path_plan_modified_2 = 'None'
                print('\nno modified_plan_2 found!')
                signal_appliance = 1
        else:
            path_plan_modified_2 = 'None'
            print('\nno modified_plan_2 found!')
            signal_appliance = 1

    # ------------------------------------------
    # call llm_appliance and plan_modifier_add_effect
    # ------------------------------------------
    if not exists(path_plan_modified_1) and signal_appliance == 1:
        print('\n#---------- call llm_appliance -----------')
        filein = open('dataset/appliances_processed.txt')  # read appliance
        all_appliance_list = []
        for line in filein.readlines():
            line = line.strip()
            joint_rule = ''
            all_appliance_list.append(joint_rule.join(line))
        appliance_list = sample(all_appliance_list, round(len(all_appliance_list) / ratio2))
        print('appliance that robot can operate:', appliance_list)
        # ------------------------------------------
        # external knowledge;
        # ------------------------------------------
        capable_appliances = []
        for candidate_appliance in appliance_list:
            if llm_appliance(situation_curr, opp_situation_curr, candidate_appliance, option3, task_id):
                capable_appliances.append(candidate_appliance)
        if len(capable_appliances) > 0:
            print('\ncapable appliances:', capable_appliances)
        # ------------------------------------------
        # use 'most possible' -- external knowledge
        # ------------------------------------------
        selected_appliance = ''
        if len(capable_appliances) == 1:
            selected_appliance = random.choice(capable_appliances)
            print('\n#---------- most possible appliance:\n', selected_appliance)
        elif len(capable_appliances) > 1:
            selected_appliance = llm_appliance_most_possible(situation_curr, opp_situation_curr, capable_appliances, task_id)
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
            domain_path_new3, problem_path_new3 = plan_modifier_add_effect_appliances(situation_predicate, situation_object, selected_appliance, domain_path_new1, problem_path_new1, task_id)
            try:
                print('\n#---------- generating modified_plan_3! -----------')
                file_name = 'task_' + str(task_id) + '_modified_plan_3'
                path_plan_modified_3 = task_planner(domain_path_new3, problem_path_new3, file_name)
                print_file(path_plan_modified_3)
            except:
                print('\nno modified_plan_3 found!')
        else:
            print('\nno modified_plan_3 found!')