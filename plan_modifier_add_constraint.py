import re
import getpass

from utility import write_file
from utility import print_list


def plan_modifier_add_constraint(action, predicate, situation_object, manipulate_object, path_domain, path_problem, task_id):
    target_predicate = predicate
    target_action = action[0]
    target_object = situation_object
    # print('target predicate:', target_predicate)
    # print('target action:', target_action)
    # print('target object:', target_object)
    # print('manipulate object:', manipulate_object)

    # ------------------------------------------
    # question: how many steps in adding constraint?
    # step 1: supplement constraint to action precondition in domain file, such as '(not (cup_is_broken ?c))'
    # step 2: supplement action parameter in domain file, such as ?w - water
    # step 3: supplement type in domain.pddl, such as water_1 - water
    # step 4: supplement predicates in domain file, such as '(cup_is_broken ?c - cup)'
    # step 5: supplement init in problem file, such as '(cup_is_broken cup_1)'
    # step 6: supplement object in problem file, such as 'water_1 - water'
    # ------------------------------------------

    # ------------------------------------------
    # step 1: supplement constraint to action precondition in domain file, such as '(not (cup_is_broken ?c))'
    # ------------------------------------------
    print('! step 1: supplement constraint to action precondition')
    # extrac action content in domain.pddl
    target_action_part = []
    domain = []
    fidin = open(path_domain, 'r')
    signal = 0
    for line in fidin.readlines():
        domain.append(line)
        line = line.strip()
        if (target_action in line or signal > 0) and len(target_action_part) <= 3:  # read the following 4 lines
            if target_action in line:
                signal = 4
            target_action_part.append(line)
        signal = signal - 1
    fidin.close()
    # print('corresponding action in domain.pddl:')
    # print_list(target_action_part)

    # extract content before/after action
    for index in range(len(domain)):
        if target_action_part[0] in domain[index]:
            target_action_part_before = domain[0:index]
        if target_action_part[-1] in domain[index]:
            target_action_part_after = domain[index + 1:]

    # analyze action content
    action_name = target_action_part[0]
    action_parameters = target_action_part[1]
    action_precondition = target_action_part[2]
    action_effect = target_action_part[3]

    # add constraint in precondition
    rule1 = re.compile(r'[(](and .*)[)]', re.S)
    conditions_1 = re.findall(rule1, action_precondition)
    condition_2 = '(not (' + target_predicate + ' ?' + target_object[0] + '))'
    new_condition = conditions_1[0] + ' ' + condition_2
    action_precondition_new = ':precondition (' + new_condition + ')'
    target_action_part_new = '\t' + action_name + '\n' + '\t\t' + action_parameters + '\n' + '\t\t' + action_precondition_new + '\n' + '\t\t' + action_effect + '\n'
    # print('updated action in new domain.pddl:')
    # print(target_action_part_new)
    domain_new = target_action_part_before + [target_action_part_new] + target_action_part_after
    user = getpass.getuser()
    new_path_domain = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
    write_file(new_path_domain, domain_new)
    print('step 1 is done!')

    # ------------------------------------------
    # step 2: supplement action's parameter (domain.pddl) ; example: ?w - water
    # ------------------------------------------
    print('! step 2: supplement action\'s parameter')
    # extrac action content in domain.pddl
    target_action_part = []
    domain = []
    fidin = open(new_path_domain, 'r')
    signal = 0
    for line in fidin.readlines():
        domain.append(line)
        line = line.strip()
        if (target_action in line or signal > 0) and len(target_action_part) <= 3:  # read the following 4 lines
            if target_action in line:
                signal = 4
            target_action_part.append(line)
        signal = signal - 1
    fidin.close()
    # print('corresponding action in domain.pddl:')
    # print_list(target_action_part)

    # extract content before/after action
    for index in range(len(domain)):
        if target_action_part[0] in domain[index]:
            target_action_part_before = domain[0:index]
        if target_action_part[-1] in domain[index]:
            target_action_part_after = domain[index + 1:]

    # analyze action content
    action_name = target_action_part[0]
    action_parameters = target_action_part[1]
    action_precondition = target_action_part[2]
    action_effect = target_action_part[3]
    if target_object not in action_parameters:
        # add parameter
        action_parameters_new = action_parameters[:-1] + ' ?' + target_object[0] + ' - ' + target_object + ')'
        target_action_part_new = '\t' + action_name + '\n' + '\t\t' + action_parameters_new + '\n' + '\t\t' + action_precondition + '\n' + '\t\t' + action_effect + '\n'
        # print('updated action in new domain.pddl:')
        # print(target_action_part_new)
        domain_new = target_action_part_before + [target_action_part_new] + target_action_part_after
        user = getpass.getuser()
        new_path_domain = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
        write_file(new_path_domain, domain_new)
        print('step 2 is done!')
    else:
        print('step 2 is skipped!')

    # ------------------------------------------
    # step 3: supplement type (domain.pddl); example: water_1 - water
    # ------------------------------------------
    print('! step 3: supplement type')
    target_type_part = ''
    domain = []
    fidin = open(new_path_domain, 'r')
    counter = 0
    index_type = 0
    for line in fidin.readlines():
        domain.append(line)
        line = line.strip()
        if 'types' in line:
            index_type = counter
            target_type_part = line
        counter = counter + 1
    fidin.close()
    # print('corresponding types in domain.pddl:')
    # print('\t', target_type_part)

    # extract content before/after type
    target_type_part_before = domain[0:index_type]
    target_type_part_after = domain[index_type + 1:]

    # add fact in type
    if target_object not in target_type_part:
        target_type_part_new = '\t' + target_type_part[:-1] + ' ' + target_object + ')\n'
        # print('updated type in new problem.pddl:')
        # print(target_type_part_new)
        domain_new = target_type_part_before + [target_type_part_new] + target_type_part_after
        user = getpass.getuser()
        new_path_domain = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
        write_file(new_path_domain, domain_new)
        print('step 3 is done!')
    else:
        print('step 3 is skipped!')

    # ------------------------------------------
    # step 4: supplement predicates in domain file, such as '(cup_is_broken ?c - cup)'
    # ------------------------------------------
    print('! step 4: supplement predicates')
    # extrac predicate content in domain.pddl
    target_predicate_part = ''
    domain = []
    fidin = open(new_path_domain, 'r')
    for line in fidin.readlines():
        domain.append(line)
        line = line.strip()
        if 'predicate' in line:
            target_predicate_part = line
    fidin.close()
    # print('corresponding predicates in domain.pddl:')
    # print('\t', target_predicate_part)

    # extract content before/after predicate
    target_predicate_part_before = []
    target_predicate_part_after = []
    for index in range(len(domain)):
        if 'predicate' in domain[index]:
            target_predicate_part_before = domain[0:index]
            target_predicate_part_after = domain[index + 1:]

    # add predicate in predicates
    target_predicate_part_new = '\t' + target_predicate_part[:-1] + ' (' + target_predicate + ' ?' + target_object[0] + ' - ' + target_object + '))\n'
    # print('updated predicates in new domain.pddl:')
    # print(target_predicate_part_new)
    predicate_new = target_predicate_part_before + [target_predicate_part_new] + target_predicate_part_after
    user = getpass.getuser()
    predicate_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
    write_file(predicate_new_path, predicate_new)
    # print('path of new domain file:', predicate_new_path)
    print('step 4 is done!')

    # ------------------------------------------
    # step 5: supplement init in problem file, such as '(cup_is_broken cup_1)'
    # ------------------------------------------
    print('! step 5: supplement init')
    # extrac init content in problem.pddl
    target_init_part = ''
    problem = []
    fidin = open(path_problem, 'r')
    for line in fidin.readlines():
        problem.append(line)
        line = line.strip()
        if 'init' in line:
            target_init_part = line
    fidin.close()
    # print('corresponding init in problem.pddl:')
    # print('\t', target_init_part)

    # extract content before/after init
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

    target_init_part_new = '\t' + target_init_part[:-1] + ' (' + target_predicate + ' ' + target_object + '_1' + '))\n'
    # print('updated init in new problem.pddl:')
    # print(target_init_part_new)
    problem_new = target_init_part_before + [target_init_part_new] + target_init_part_after
    user = getpass.getuser()
    new_path_problem = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_new.pddl'
    write_file(new_path_problem, problem_new)
    # print('path of new problem file:', new_path_problem)
    print('step 5 is done!')

    # ------------------------------------------
    # step 6: supplement object in problem file, such as 'water_1 - water'
    # ------------------------------------------
    print('! step 6: supplement object')
    target_object_part = ''
    problem = []
    fidin = open(new_path_problem, 'r')
    for line in fidin.readlines():
        problem.append(line)
        line = line.strip()
        if 'objects' in line:
            target_object_part = line
    fidin.close()
    # print('corresponding object in problem.pddl:')
    # print('\t', target_object_part)

    if target_object not in target_object_part:
        # extract content before/after object
        target_object_part_before = []
        target_object_part_after = []
        for line in problem:
            if 'define' in line:
                target_object_part_before.append(line)
            if 'problem' in line:
                target_object_part_before.append(line)
            if 'domain' in line:
                target_object_part_before.append(line)
            if 'init' in line:
                target_object_part_after.append(line)
            if 'goal' in line:
                target_object_part_after.append(line)
        target_object_part_after.append(')')

        target_object_part_new = '\t'+ target_object_part[:-1] + ' ' + target_object + '_1' + ' - ' + target_object + ')\n'
        # print('updated object in new problem.pddl:')
        # print(target_object_part_new)
        problem_new = target_object_part_before + [target_object_part_new] + target_object_part_after
        user = getpass.getuser()
        new_path_problem = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_new.pddl'
        write_file(new_path_problem, problem_new)
        print('step 6 is done!')
    else:
        print('step 6 is skipped!')

    return new_path_domain, new_path_problem
