from task_planner import task_planner
from plan_manager import plan_manager
from translator import translator
from situation_simulator_test import situation_simulator
from object_simulator import object_simulator
from plan_monitor import plan_monitor
from plan_modifier_add_constraint import plan_modifier_add_constraint
from llm_appliance import llm_appliance
from llm_appliance_most_possible import llm_appliance_most_possible
from llm_utensil import llm_utensil
from llm_utensil_most_possible import llm_utensil_most_possible
from plan_modifier_add_effect_appliances import plan_modifier_add_effect_appliances
from plan_modifier_add_effect_utensils import plan_modifier_add_effect_utensils
import random
from os.path import exists
import getpass
from tools import print_file
from tools import read_plan

# domain_path_new1 = '/home/yan/githubBase/GPT-Planner/pddl/task4/domain_new_speical_good.pddl'
# problem_path_new1 = '/home/yan/githubBase/GPT-Planner/pddl/task4/problem_new_special_good.pddl'
# domain_path_new1 = '/home/yan/githubBase/GPT-Planner/pddl/task4/domain_new_speical_test.pddl'
# problem_path_new1 = '/home/yan/githubBase/GPT-Planner/pddl/task4/problem_new_special_test.pddl'
# domain_path_new1 = '/home/yan/githubBase/GPT-Planner/pddl/task4/domain_new2.pddl'
# problem_path_new1 = '/home/yan/githubBase/GPT-Planner/pddl/task4/problem_new2.pddl'
# domain_path_new1 = '/home/yan/githubBase/GPT-Planner/pddl/task6/domain_basic.pddl'
# problem_path_new1 = '/home/yan/githubBase/GPT-Planner/pddl/task6/problem_basic.pddl'
# file_name = 'test'
# path_plan = task_planner(domain_path_new1, problem_path_new1, file_name)
# print_file(path_plan)


# domain_new_path = '/home/yan/githubBase/GPT-Planner/pddl/task4/domain_new_speical_good.pddl'
# target_type_part = ''
# domain = []
# fidin = open(domain_new_path, 'r')
# counter = 0
# index_type = 0
# for line in fidin.readlines():
#     domain.append(line)
#     line = line.strip()
#     if 'types' in line:
#         index_type = counter
#         target_type_part = line
#     counter = counter + 1
# fidin.close()
# print('corresponding types in domain.pddl:')
# print('\t', target_type_part)
#
# # extract content before/after type
# target_action_part_before = domain[0:index_type]
# target_action_part_after = domain[index_type + 1:]
task_id = 6
fidin = open('trials' + '_task_' + str(task_id) + '.txt', 'w')
num_cupboard = 0
num_plate = 0
num_fork = 0
num_table = 0
for i in range(50):
    group, opp_group, group_object, group_predicate, group_action = situation_simulator(task_id)
    appliance_selected, utensil_selected = object_simulator()
    fidin.write('%s\n' % group)
    if 'cupboard' in group_object:
        num_cupboard = num_cupboard + 1
    if 'plate' in group_object:
        num_plate = num_plate + 1
    if 'fork' in group_object:
        num_fork = num_fork + 1
    if 'table' in group_object:
        num_table = num_table + 1
    fidin.write('%s\n' % appliance_selected)
    fidin.write('%s\n' % utensil_selected)
    fidin.write('-----------------------\n')
    fidin.flush()
print(num_cupboard)
print(num_plate)
print(num_fork)
print(num_table)