import os
import getpass
import openai
import numpy as np
import torch
import math
import re

user = getpass.getuser()


def task_planner(path_domain, path_problem, name_output):
    address_taskplanner = '/home/' + getpass.getuser() + '/githubBase/GPT-Planner/FastDownward/fast-downward.py'
    if os.path.exists(address_taskplanner):
        output_filename = name_output
        command = 'python ' + address_taskplanner + ' --alias lama-first ' + '--plan-file ' + output_filename + ' ' + path_domain + ' ' + path_problem
        os.system(command + '>/dev/null 2>&1')
        # os.system(command)
        return '/home/' + user + '/githubBase/GPT-Planner/' + output_filename
    else:
        print('Error -- Not find fast-downward.py!')


def print_file(file_path):
    fidin = open(file_path, 'r')
    for line in fidin.readlines():
        line = line.strip()
        print(line)
    fidin.close()


def print_plan(file_path):
    fidin = open(file_path, 'r')
    for line in fidin.readlines():
        line = line.strip()
        print(line)
    fidin.close()


def print_list(input_list):
    for item in input_list:
        print(item)


def write_file(file_path, content):
    fidin = open(file_path, 'w')
    for item in content:
        fidin.write('%s' % item)
        fidin.flush()
    fidin.close()


def read_plan(file_path):
    fidin = open(file_path, 'r')
    plan = []
    for line in fidin.readlines():
        line = line.strip()
        line = line[1:-1]
        line = line.split(' ')
        plan.append(line)
    plan = plan[:-1]
    fidin.close()
    return plan


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

# set GPU
GPU = 0
if torch.cuda.is_available():
    torch.cuda.set_device(GPU)


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


def grammar_corrector(sentence):
    gpt_model = 'text-davinci-002'
    raw_response = openai.Completion.create(
        engine=gpt_model,
        prompt="Correct this to standard English:\n\n" + sentence,
        temperature=0,
        max_tokens=32,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['\\n', '.']
    )
    response = raw_response['choices'][0]['text']
    response = response.strip()
    return response


def plan_monitor(situation, action, option1, task_id):
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
    prompt = 'is it ' + option1 + ' that ' + action[:-1] + ' if ' + situation[:-1] + '?'
    print('! prompt design')
    print('raw prompt:', prompt)

    # ------------------------------------------
    # create a file to store experience
    # ------------------------------------------
    fidout1 = open('experience/experience_task_' + str(task_id) + '.txt', 'a')

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
            responses_1, probs_1 = llm(prompt)  # get responses from llm
            fidout1.write('%s\n' % target_prompt)
            fidout1.write('response (raw prompt):%s\n' % responses_1)
            fidout1.flush()
        except:
            print('Error -- no response from LLM!')
    else:
        rule = re.compile(r'[[](.*?)[]]')
        line2 = line2.strip()
        responses_1 = [re.findall(rule, line2)[0]]
    print('! response from LLM')
    print('response (raw prompt):', responses_1)
    if 'no' in responses_1[0] or 'not' in responses_1[0]:
        return True
    else:
        return False