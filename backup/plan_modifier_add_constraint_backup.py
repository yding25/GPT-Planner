import re
from backup.write_file import write_file
import getpass
from backup.print_list import print_list


def plan_modifier_add_constraint(action, predicate, path_domain, path_problem, task_id):
    # ------------------------------------------
    # step 1: change precondition
    # ------------------------------------------
    print('\n')
    print('#----------step 1: add constraint to the precondition of an action -----------')
    target_action = action[0]  # get the action
    # print('target_action:', target_action)
    temp = target_action.split('_')  # get the object
    target_object = temp[1]
    # print('target_object:', target_object)
    target_predicate = predicate  # get the predicate
    # print('target_predicate:', target_predicate)

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
    print('target_action_part:')
    print_list(target_action_part)
    fidin.close()

    for index in range(len(domain)):
        if target_action_part[0] in domain[index]:
            target_action_part_before = domain[0:index]
        if target_action_part[-1] in domain[index]:
            target_action_part_after = domain[index + 1:]

    # analyze this part
    action_name = target_action_part[0]
    action_parameters = target_action_part[1]
    action_precondition = target_action_part[2]
    # print('action_precondition:', action_precondition)
    action_effect = target_action_part[3]

    # add constraint in precondition
    if 'or' not in action_precondition:
        rule1 = re.compile(r'[(](and .*)[)]', re.S)
        conditions_1 = re.findall(rule1, action_precondition)
        condition_2 = '(not (' + target_predicate + ' ?' + target_object[0] + '))'
        new_condition = conditions_1[0] + ' ' + condition_2
        action_precondition_new = ':precondition (' + new_condition + ')'
        # print('action_precondition(new):', action_precondition_new)
        target_action_part_new = '\t' + action_name + '\n' + '\t\t' + action_parameters + '\n' + '\t\t' + action_precondition_new + '\n' + '\t\t' + action_effect + '\n'
        print('target_action_part_new:')
        print(target_action_part_new)

        domain_new = target_action_part_before + [target_action_part_new] + target_action_part_after
        user = getpass.getuser()
        domain_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
        write_file(domain_new_path, domain_new)
        print('path of new domain:', domain_new_path)
    else:
        print('TBD, if precondition has \'or\'')

    # ------------------------------------------
    # step 2: change init
    # ------------------------------------------
    print('\n')
    print('#----------step 2: supplement init -----------')
    target_init_part = ''
    problem = []
    fidin = open(path_problem, 'r')
    for line in fidin.readlines():
        problem.append(line)
        line = line.strip()
        if 'init' in line:
            target_init_part = line
    print('target_init_part:')
    print('\t', target_init_part)
    fidin.close()

    # print('problem:', problem)
    target_init_part_before = []
    target_init_part_after = []
    for line in problem:
        if 'define' in line:
            target_init_part_before.append(line)
        if 'problem' in line:
            target_init_part_before.append(line)
        if 'domain' in line:
            target_init_part_before.append(line)
        if 'objects' in line:
            target_init_part_before.append(line)
        if 'goal' in line:
            target_init_part_after.append(line)
    target_init_part_after.append(')')

    # add fact in init
    target_object_full = ''
    for item in action:
        if target_object in item:
            target_object_full = item
    if 'or' not in target_init_part:
        target_init_part_new = '\t' + target_init_part[
                                      :-1] + ' (' + target_predicate + ' ' + target_object_full + '))\n'
        print('target_init_part_new:')
        print('\t', target_init_part_new)
        problem_new = target_init_part_before + [target_init_part_new] + target_init_part_after
        user = getpass.getuser()
        problem_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_new.pddl'
        write_file(problem_new_path, problem_new)
        print('path of new problem:', problem_new_path)
    else:
        print('TBD, if init has \'or\'')

    # ------------------------------------------
    # step 3: change predicates
    # ------------------------------------------
    print('\n')
    print('#----------step 3: supplement predicates -----------')
    target_predicate_part = ''
    domain = []
    fidin = open(domain_new_path, 'r')
    for line in fidin.readlines():
        domain.append(line)
        line = line.strip()
        if 'predicate' in line:
            target_predicate_part = line
    print('target_predicate_part:')
    print('\t', target_predicate_part)
    fidin.close()

    target_predicate_part_before = []
    target_predicate_part_after = []
    for index in range(len(domain)):
        if 'predicate' in domain[index]:
            target_predicate_part_before = domain[0:index]
            target_predicate_part_after = domain[index+1:]

    # add predicate in predicates
    if 'or' not in target_predicate_part:
        target_predicate_part_new = '\t' + target_predicate_part[:-1] + ' (' + target_predicate + ' ?' + target_object[0] + ' - ' + target_object + '))\n'
        print('target_predicate_part_new:')
        print('\t', target_predicate_part_new)
        predicate_new = target_predicate_part_before + [target_predicate_part_new] + target_predicate_part_after
        user = getpass.getuser()
        predicate_new_path = domain_new_path
        write_file(predicate_new_path, predicate_new)
        print('path of new problem:', predicate_new_path)
        print('\n')
    else:
        print('TBD, if predicate has \'or\'')

    return domain_new_path, problem_new_path
