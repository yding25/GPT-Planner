import re
from backup.write_file import write_file
import getpass
from backup.print_list import print_list


def plan_modifier_add_effect_appliances(action, predicate, object, appliance, path_domain, path_problem, task_id):
    target_action = 'operate'
    temp = action[0].split('_')
    # target_object = temp[1]
    target_object = object
    target_predicate = predicate
    # print('target_action:', target_action)
    # print('target_object:', target_object)  # get the object
    # print('target_predicate:', target_predicate)

    # extrac action content in domain.pddl
    target_action_part = []
    domain = []
    fidin = open(path_domain, 'r')
    signal = 0
    for line in fidin.readlines():
        domain.append(line)
        line = line.strip()
        if target_action in line or signal > 0:
            if target_action in line:
                signal = 4
            target_action_part.append(line)
        signal = signal - 1
    fidin.close()
    print('corresponding action in domain.pddl:')
    print_list(target_action_part)

    # extract content before/after action
    for index in range(len(domain)):
        if target_action_part[0] in domain[index]:
            target_action_part_before = domain[0:index]
        if target_action_part[-1] in domain[index]:
            target_action_part_after = domain[index + 1:]

    # analyze this part
    action_name = target_action_part[0]
    action_parameters = target_action_part[1]
    action_precondition = target_action_part[2]
    action_effect = target_action_part[3]

    # ------------------------------------------
    # step 1: change effect
    # ------------------------------------------
    print('\n')
    print('#---------- step 1: add effect by operating appliance -----------')
    # add effect
    rule1 = re.compile(r'[(](and .*)[)]', re.S)
    effect_1 = re.findall(rule1, action_effect)
    effect_2 = '(not (' + target_predicate + ' ?' + target_object[0] + '))'
    new_effect = effect_1[0] + ' ' + effect_2
    action_effect_new = ':effect (' + new_effect + ')'

    # ------------------------------------------
    # step 2: change parameter
    # ------------------------------------------
    print('#---------- step 2: add parameter by adding appliance -----------')
    parameter_1 = action_parameters[:-1]
    parameter_2 = '?' + target_object[0] + ' - ' + target_object + ')'
    action_parameters_new = parameter_1 + ' ' + parameter_2

    target_action_part_new = '\t' + action_name + '\n' + '\t\t' + action_parameters_new + '\n' + '\t\t' + action_precondition + '\n' + '\t\t' + action_effect_new + '\n'
    print('updated action in new domain.pddl:')
    print(target_action_part_new)
    domain_new = target_action_part_before + [target_action_part_new] + target_action_part_after
    user = getpass.getuser()
    domain_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_new2.pddl'
    write_file(domain_new_path, domain_new)
    print('path of new domain file:', domain_new_path)


    problem = []
    fidin = open(path_problem, 'r')
    for line in fidin.readlines():
        problem.append(line)
    fidin.close()
    print('problem:')
    print_list(problem)
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
    problem_goal = problem_goal + ')'

    # ------------------------------------------
    # step 3: change init
    # ------------------------------------------
    print('#---------- step 3: change init-----------')
    # add fact in init
    problem_init_new = problem_init[:-2] + ' (appliance_at ' + appliance + ' kitchen))\n'

    # ------------------------------------------
    # step 4: change object
    # ------------------------------------------
    print('#---------- step 4: change object-----------')
    # add object
    problem_object_new = problem_object[:-2] + ' ' + appliance + ' - appliance)\n'

    problem_new = [problem_define] + [problem_problem] + [problem_domain] + [problem_object_new] + [
        problem_init_new] + [problem_goal]
    print('problem_new:')
    print_list(problem_new)
    user = getpass.getuser()
    problem_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_new2.pddl'
    write_file(problem_new_path, problem_new)
    print('path of new domain:', problem_new_path)
    print('\n')

    return domain_new_path, problem_new_path
