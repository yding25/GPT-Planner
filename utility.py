import getpass
import openai
import numpy as np
import math
import re
import time
import os
from random import sample


user = getpass.getuser()


# ------------------------------------------
# classical task planner engine
# ------------------------------------------
def task_planner(path_domain, path_problem, name_output):
    path_engine = '/home/' + getpass.getuser() + '/GPT-Planner/FastDownward/fast-downward.py'
    if os.path.exists(path_engine):
        command = 'python ' + path_engine + ' --alias lama-first ' + '--plan-file ' + name_output + ' ' + path_domain + ' ' + path_problem
        os.system(command + '>/dev/null 2>&1')  # skip outputting intermediate results
        # os.system(command)  # outputting intermediate results
        return '/home/' + user + '/GPT-Planner/' + name_output
    else:
        print('Error: not find fast-downward.py!')


def exist_remove(task_id):
    path1 = 'task_' + str(task_id) + '_basic_plan.txt'
    path2 = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_new.pddl'
    path3 = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_new1.pddl'
    path4 = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_new2.pddl'
    path5 = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_new.pddl'
    path6 = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_new1.pddl'
    path7 = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_new2.pddl'
    path8 = '/home/' + user + '/GPT-Planner/task_' + str(task_id) + '_basic_plan.txt'
    path9 = '/home/' + user + '/GPT-Planner/task_' + str(task_id) + '_modified_plan_1.txt'
    path10 = '/home/' + user + '/GPT-Planner/task_' + str(task_id) + '_modified_plan_2.txt'
    path11 = '/home/' + user + '/GPT-Planner/task_' + str(task_id) + '_modified_plan_3.txt'
    for path in [path1, path2, path3, path4, path5, path6, path7, path8, path9, path10, path11]:
        if os.path.exists(path):
            os.remove(path)
        else:
            continue
    time.sleep(1)
    print('before running, all old files have been removed.\n')


def random_remove(task_id):
    path = 'experience/experience_task_' + str(task_id) + '.txt'
    if np.random.choice([True, False], p=np.array([0.01, 0.99])):
        if os.path.exists(path):
            os.remove(path)
        print('experience pool has been removed.\n')


def read_plan(path_file):
    fidin = open(path_file, 'r')
    plan = []
    for line in fidin.readlines():
        line = line.strip()  # remove space
        line = line[1:-1]  # remove ()
        line = line.split(' ')
        plan.append(line)
    plan = plan[:-1]
    fidin.close()
    return plan


def extract_objects(path_file):
    fidin = open(path_file, 'r')
    objects = []
    for line in fidin.readlines():
        line = line.strip()  # remove space
        line = line[1:-1]  # remove ()
        line = line.split(' ')
        line = line[1:]  # remove action
        for item in line:
            if ('rob' not in item) and ('dining' not in item) and ('kitchen' not in item) and (item not in objects):
                objects.append(item)
    fidin.close()
    return objects


def extract_action_content(path_domain, situation_action):
        fidin = open(path_domain, 'r')
        action_part = []
        domain = []
        counter_signal = 0
        for line in fidin.readlines():
            domain.append(line)  # save domain file with format
            line = line.strip()
            if (situation_action in line or counter_signal > 0) and len(action_part) <= 3:  # read the following 4 lines
                if situation_action in line:
                    counter_signal = 4
                action_part.append(line)
            counter_signal = counter_signal - 1
        fidin.close()

        # extract content before/after action
        for index in range(len(domain)):
            if action_part[0] in domain[index]:
                action_part_before = domain[0:index]
            if action_part[-1] in domain[index]:
                action_part_after = domain[index + 1:]

        # analyze action content
        action_name = action_part[0]
        action_parameters = action_part[1]
        action_precondition = action_part[2]
        action_effect = action_part[3]

        return domain, action_part, action_part_before, action_part_after, action_name, action_parameters, action_precondition, action_effect


def extract_problem_content(path_problem):
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
    return problem_define, problem_problem, problem_domain, problem_object, problem_init, problem_goal


def locate_object(target_object, objects):
    for item in objects:
        if target_object in item:
            target_object = item
            break
    return target_object


def select_object(task_id, ratio):
    path_object = {
        1: 'utensils.txt',
        4: 'utensils.txt',
        6: 'utensils_furnitures.txt',
        9: 'utensils.txt',
        10: 'utensils_beverages.txt',
        11: 'utensils_furnitures_foods.txt'
    }
    filein = open('dataset/' + path_object[task_id], 'r')
    objects = []
    for line in filein.readlines():
        line = line.strip()
        joint_rule = ''
        objects.append(joint_rule.join(line))
    objects_selected = sample(objects, round(len(objects) / ratio))
    return objects_selected


def select_appliance(ratio):
    filein = open('dataset/appliances.txt', 'r')
    appliances = []
    for line in filein.readlines():
        line = line.strip()
        joint_rule = ''
        appliances.append(joint_rule.join(line))
    appliances_selected = sample(appliances, round(len(appliances) / ratio))
    return appliances_selected


def template_response(response):
    # ideal response should be yes or no
    if response[0] == 'y':
        template = 'yes'
    elif response[0] == 'n':
        template = 'no'
    else:
        template = 'no'
        print('Error: no template answer.')
    return template


def print_plan(path_file):
    fidin = open(path_file, 'r')
    for line in fidin.readlines():
        line = line.strip()
        print(line)
    fidin.close()


def print_file(path_file):
    fidin = open(path_file, 'r')
    for line in fidin.readlines():
        line = line.strip()
        print(line)
    fidin.close()


def print_list(input_list):
    for item in input_list:
        print(item)


def write_file(path_file, content):
    fidin = open(path_file, 'w')
    for item in content:
        fidin.write('%s' % item)
        fidin.flush()
    fidin.close()


def plan_manager(step, path_plan):
    # extract i-th action
    fidin = open(path_plan, 'r')
    plan = []
    for line in fidin.readlines():
        line = line.strip()
        line = line[1:-1]
        line = line.split(' ')
        plan.append(line)
    plan = plan[:-1]
    return plan[step]


fidin = open('dataset/openai_api_key.txt', 'r')
key = fidin.read()
openai.api_key = key
fidin.close()


def predicate_generator(situation):
    response = openai.Completion.create(
        engine='text-curie-001',
        prompt="tranlate a sentence into a predicate\n\n####\nsentence: The cup is broken.\npredicate: "
               "cup_is_broken\n\n####\nsentence: No water comes out of faucet.\npredicate: "
               "faucet_no_water\n\n####\nsentence: " + situation + "'\npredicate:",
        temperature=0,
        max_tokens=20,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['\\n', '.']
    )
    result = response['choices'][0]
    return result['text'][1:]


def plan_monitor(task_id, situation, action_decoded, option1):
    def llm(prompt):
        gpt_model = 'text-davinci-002'
        sampling_params = {"n": 1,  # sampling number
                           "max_tokens": 32,
                           "temperature": 0,
                           "top_p": 1,
                           "logprobs": 1,
                           "presence_penalty": 0,
                           "frequency_penalty": 0,
                           "stop": ['\\n', '.']}
        raw_response = openai.Completion.create(engine=gpt_model, prompt=prompt, **sampling_params)
        responses = [raw_response['choices'][i]['text'] for i in range(sampling_params['n'])]
        mean_probs = [math.exp(np.mean(raw_response['choices'][i]['logprobs']['token_logprobs'])) for i in range(sampling_params['n'])]
        responses = [sample.strip().lower() for sample in responses]
        return responses, mean_probs

    # ------------------------------------------
    # prompt design
    # ------------------------------------------
    prompt = 'is it ' + option1 + ' that ' + action_decoded[:-1] + ' if ' + situation[:-1] + '?'
    print('! prompt design')
    print('raw prompt:', prompt)

    fidout1 = open('experience/experience_task_' + str(task_id) + '.txt', 'a')  # create a file to save experience
    # ------------------------------------------
    # search experience pool
    # ------------------------------------------
    fidout2 = open('experience/experience_task_' + str(task_id) + '.txt', 'r')
    target_prompt = 'raw prompt:' + prompt
    signal_experience = False  # signal if experience can be found
    for line1, line2 in zip(fidout2, fidout2):
        if target_prompt in line1:
            print('! experience found')
            signal_experience = True
            break
        else:
            continue
    if not signal_experience:
        try:
            responses, probs_1 = llm(prompt)  # get responses from llm
            resp = responses[0]
            fidout1.write('%s\n' % target_prompt)
            fidout1.write('%s\n' % resp)
            fidout1.flush()
        except:
            print('Error: no response from LLM!')
    else:
        line2 = line2.strip()
        responses = line2.split(' ')
        resp = responses[0]
    print('! response from LLM')
    print('response (raw prompt):', resp)
    if 'no' in resp or 'not' in resp:
        return True
    else:
        return False