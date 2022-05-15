import re
import getpass
from utility import extract_action_content, write_file, print_list

user = getpass.getuser()

# ------------------------------------------
# how many steps in adding constraint?
# (domain file) step 1: supplement constraint to action precondition, e.g., '(not (cup_is_broken ?c))'
# (domain file) step 2: supplement action parameter, e.g., ?w - water
# (domain file) step 3: supplement type, e.g., water_1 - water
# (domain file) step 4: supplement predicates, e.g., '(cup_is_broken ?c - cup)'
# (problem file) step 5: supplement init, e.g., '(cup_is_broken cup_1)'
# (problem file) step 6: supplement object, e.g., 'water_1 - water'
# ------------------------------------------


def plan_modifier_add_constraint(task_id, situation_action, situation_predicate, situation_object, situation_object_new, path_domain, path_problem):
    # ------------------------------------------
    # step 1: supplement constraint to action precondition, e.g., '(not (cup_is_broken ?c))'
    # ------------------------------------------
    print('! step 1: supplement constraint to action precondition')
    # extract and analyze action content in domain.pddl
    domain, action_part, action_part_before, action_part_after, action_name, action_parameters, action_precondition, action_effect = extract_action_content(path_domain, situation_action)
    rule1 = re.compile(r'[(](and .*)[)]', re.S)
    condition_1 = re.findall(rule1, action_precondition)
    condition_2 = '(not (' + situation_predicate + ' ?' + situation_object[0] + '))'
    condition_new = condition_1[0] + ' ' + condition_2
    action_precondition_new = ':precondition (' + condition_new + ')'
    action_part_new = '\t' + action_name + '\n' + '\t\t' + action_parameters + '\n' + '\t\t' + action_precondition_new + '\n' + '\t\t' + action_effect + '\n'

    domain_new = action_part_before + [action_part_new] + action_part_after
    new_path_domain = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
    write_file(new_path_domain, domain_new)
    print('step 1 is done!')
    # ------------------------------------------
    # step 2: supplement action's parameter (domain.pddl), e.g., ?w - water
    # ------------------------------------------
    print('! step 2: supplement action\'s parameter')
    # extrac action content in domain file
    domain, action_part, action_part_before, action_part_after, action_name, action_parameters, action_precondition, action_effect = extract_action_content(new_path_domain, situation_action)

    if situation_object not in action_parameters:
        # add parameter
        action_parameters_new = action_parameters[:-1] + ' ?' + situation_object[0] + ' - ' + situation_object + ')'
        action_part_new = '\t' + action_name + '\n' + '\t\t' + action_parameters_new + '\n' + '\t\t' + action_precondition + '\n' + '\t\t' + action_effect + '\n'

        domain_new = action_part_before + [action_part_new] + action_part_after
        new_path_domain = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
        write_file(new_path_domain, domain_new)
        print('step 2 is done!')
    else:
        print('step 2 is skipped!')
    # ------------------------------------------
    # step 3: supplement type (domain.pddl); example: water_1 - water
    # ------------------------------------------
    print('! step 3: supplement type')
    fidin = open(new_path_domain, 'r')
    type_part = ''
    domain = []
    counter_line = 0
    index_type = 0
    for line in fidin.readlines():
        domain.append(line)
        line = line.strip()
        if 'types' in line:
            type_part = line
            index_type = counter_line
        counter_line = counter_line + 1
    fidin.close()

    # extract content before/after type
    type_part_before = domain[0:index_type]
    type_part_after = domain[index_type + 1:]

    # add fact in type
    if situation_object not in type_part:
        type_part_new = '\t' + type_part[:-1] + ' ' + situation_object + ')\n'
        domain_new = type_part_before + [type_part_new] + type_part_after
        new_path_domain = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
        write_file(new_path_domain, domain_new)
        print('step 3 is done!')
    else:
        print('step 3 is skipped!')
    # ------------------------------------------
    # step 4: supplement predicates in domain file, such as '(cup_is_broken ?c - cup)'
    # ------------------------------------------
    print('! step 4: supplement predicates')
    # extrac predicate content in domain file
    fidin = open(new_path_domain, 'r')
    predicate_part = ''
    domain = []
    counter_line = 0
    index_predicate = 0
    for line in fidin.readlines():
        domain.append(line)
        line = line.strip()
        if 'predicate' in line:
            predicate_part = line
            index_predicate = counter_line
        counter_line = counter_line + 1
    fidin.close()

    # extract content before/after predicate
    predicate_part_before = domain[0:index_predicate]
    predicate_part_after = domain[index_predicate + 1:]

    # add predicate in predicates
    predicate_part_new = '\t' + predicate_part[:-1] + ' (' + situation_predicate + ' ?' + situation_object[0] + ' - ' + situation_object + '))\n'
    domain_new = predicate_part_before + [predicate_part_new] + predicate_part_after
    new_path_domain = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
    write_file(new_path_domain, domain_new)
    print('step 4 is done!')
    # ------------------------------------------
    # step 5: supplement init in problem file, such as '(cup_is_broken cup_1)'
    # ------------------------------------------
    print('! step 5: supplement init')
    # extrac init content in problem.pddl
    fidin = open(path_problem, 'r')
    target_init_part = ''
    problem = []
    for line in fidin.readlines():
        problem.append(line)
        line = line.strip()
        if 'init' in line:
            target_init_part = line
    fidin.close()

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

    target_init_part_new = '\t' + target_init_part[:-1] + ' (' + situation_predicate + ' ' + situation_object_new + '))\n'

    # a special case --- rob
    if 'robot' in situation_object:
        target_init_part_new = '\t' + target_init_part[:-1] + ' (' + situation_predicate + ' rob' + '))\n'

    problem_new = target_init_part_before + [target_init_part_new] + target_init_part_after
    new_path_problem = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_new.pddl'
    write_file(new_path_problem, problem_new)
    print('step 5 is done!')
    # ------------------------------------------
    # step 6: supplement object in problem file, such as 'water_1 - water'
    # ------------------------------------------
    print('! step 6: supplement object')
    fidin = open(new_path_problem, 'r')
    target_object_part = ''
    problem = []
    for line in fidin.readlines():
        problem.append(line)
        line = line.strip()
        if 'objects' in line:
            target_object_part = line
    fidin.close()

    if situation_object not in target_object_part:
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

        target_object_part_new = '\t'+ target_object_part[:-1] + ' ' + situation_object_new + ' - ' + situation_object + ')\n'
        problem_new = target_object_part_before + [target_object_part_new] + target_object_part_after

        new_path_problem = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_new.pddl'
        write_file(new_path_problem, problem_new)
        print('step 6 is done!')
    else:
        print('step 6 is skipped!')

    return new_path_domain, new_path_problem