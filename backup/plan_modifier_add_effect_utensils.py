import re
import getpass
import shutil

from utility import write_file
from utility import print_list


def plan_modifier_add_effect_utensils(predicate, object, utensil, path_domain, path_problem, task_id):
    target_object = object
    target_predicate = predicate

    problem = []
    fidin = open(path_problem, 'r')
    for line in fidin.readlines():
        problem.append(line)
    fidin.close()

    problem_define = []
    problem_problem = []
    problem_domain = []
    problem_object = []
    problem_init = []
    problem_goal = []
    for line in problem:
        if 'define' in line:
            problem_define = line
        if 'problem' in line:
            problem_problem = line
        if 'domain' in line:
            problem_domain = line
        if 'objects' in line:
            problem_object = line
        if 'init' in line:
            problem_init = line
        if 'goal' in line:
            problem_goal = line

    # ------------------------------------------
    # step 1: add object
    # ------------------------------------------
    print('#---------- step 1: add object-----------')
    problem_object_new = problem_object[:-2] + ' ' + utensil + '_1 - ' + target_object + ')\n'
    # print(problem_object_new)
    print('step 1 is done.')

    # ------------------------------------------
    # step 2: add init
    # ------------------------------------------
    print('#---------- step 2: change init-----------')
    rule1 = re.compile(r'[(](.*?)[)]', re.S)
    problem_init_1 = re.findall(rule1, problem_init)
    problem_init_2 = []
    for item in problem_init_1:
        if (target_object in item) and (target_predicate not in item):
            problem_init_2.append(item.replace(target_object + '_1', utensil + '_1'))
    problem_init_new_raw = problem_init_1 + problem_init_2
    problem_init_new = []
    for item in problem_init_new_raw:
        problem_init_new.append('(' + item + ')')
    problem_init_new = '\t' + ' '.join(problem_init_new) + ')\n'
    # print(problem_init_new)
    print('step 2 is done.')

    # ------------------------------------------
    # step 3: change goal
    # ------------------------------------------
    print('#---------- step 3: change goal-----------')
    rule1 = re.compile(r'[(](and.*)[)]', re.S)
    problem_goal_1 = re.findall(rule1, problem_goal)
    # print('problem_goal_1:', problem_goal_1)
    problem_goal_2 = problem_goal_1[0].replace(target_object + '_1', utensil + '_1')
    # print('problem_goal_2:', problem_goal_2)
    problem_goal_new = '\t(:goal (or ' + '(' + problem_goal_1[0] + ' ' + '(' + problem_goal_2 + '))' + '\n)'
    # print('problem_goal_new:', problem_goal_new)

    problem_new = [problem_define] + [problem_problem] + [problem_domain] + [problem_object_new] + [
        problem_init_new] + [problem_goal_new]
    # print('problem_new:')
    print_list(problem_new)
    user = getpass.getuser()
    problem_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_new1.pddl'
    write_file(problem_new_path, problem_new)
    # print('path of new problem:', problem_new_path)
    print('step 3 is done.')

    domain_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_new1.pddl'
    shutil.copyfile(path_domain, domain_new_path)
    return domain_new_path, problem_new_path