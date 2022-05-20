import openai
import numpy as np
import math
import re
import getpass
import shutil


# ------------------------------------------
# customized modules
# ------------------------------------------
from action_translator import action_translator
from utility import extract_problem_content, read_plan, plan_manager, write_file, template_response

fidin = open('dataset/openai_api_key.txt', 'r')
key = fidin.read()
openai.api_key = key
fidin.close()


def llm_object(task_id, path_plan, situation_object, item, option):
    def llm(prompt):
        gpt_model = 'text-davinci-002'
        sampling_params = {"n": 1,
                           "max_tokens": 32,
                           "temperature": 0.0,
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

    fidout1 = open('experience/experience_task_' + str(task_id) + '.txt', 'a')  # create a file to store experience
    # ------------------------------------------
    # prepared decoded plan
    # ------------------------------------------
    plan = read_plan(path_plan)
    plan_decoded = []
    for index in range(len(plan)):
        action = plan_manager(index, path_plan)
        action_decoded, action_decoded2 = action_translator(action, task_id)
        plan_decoded.append(action_decoded2)
    # ------------------------------------------
    # prompt design, query llm, save and identify result
    # ------------------------------------------
    result_list = []  # record llm response
    for sentence in plan_decoded:
        if (situation_object in sentence) and ('find' not in sentence):
            new_sentence = sentence.replace(situation_object, item)
            new_sentence = new_sentence[:-1]
            prompt = 'is it ' + option + ' that a robot fills a cup with juice?\nanswer: yes\n\n' \
                     'is it ' + option + ' that a robot fills a cup with a cooking pot?\nanswer: no\n\n' \
                     'is it ' + option + ' that a robot pulls up a chair?\nanswer: yes\n\n' \
                     'is it ' + option + ' that a robot pulls up a cup?\nanswer: no\n\n' \
                     'is it ' + option + ' that a robot place a cup on a table?\nanswer: yes\n\n' \
                     'is it ' + option + ' that a robot place a chair on a table?\nanswer: no\n\n' \
                     'is it ' + option + ' that a robot grasps an apple?\nanswer: yes\n\n' \
                     'is it ' + option + ' that a robot grasps an table?\nanswer: no\n\n' \
                     'is it ' + option + ' that ' + new_sentence + '?' + '\nanswer:'
            print('\n! prompt design')
            print('raw prompt:', 'is it ' + option + ' that ' + new_sentence + '?' + '\nanswer:')
            # ------------------------------------------
            # firstly search experience pool
            # ------------------------------------------
            fidout2 = open('experience/experience_task_' + str(task_id) + '.txt', 'r')
            signal_found = False  # signal if experience can be found
            target_prompt = 'raw prompt:' + 'is it ' + option + ' that ' + new_sentence + '?'
            for line1, line2 in zip(fidout2, fidout2):
                if target_prompt in line1:
                    print('! experience found')
                    signal_found = True
                    break
                else:
                    continue
            # ------------------------------------------
            # secondly query llm
            # ------------------------------------------
            if not signal_found:
                try:
                    responses, probs_1 = llm(prompt)  # responses is a list
                    resp = template_response(responses[0])
                    fidout1.write('%s\n' % target_prompt)
                    fidout1.write('%s\n' % resp)
                    fidout1.flush()
                    # test
                    print(responses)
                    print(probs_1)
                except:
                    print('Error: no response in llm_object!')
            else:
                line2 = line2.strip()
                responses = line2.split(' ')
                resp = responses[0]
            print('! results from LLM')
            print('response (raw prompt):', resp)
            # ------------------------------------------
            # save llm result in result_list
            # ------------------------------------------
            if 'no' in resp[0:2] or 'No' in resp[0:2]:
                result_list.append('no')
                break
            else:
                result_list.append('yes')
    # ------------------------------------------
    # identify result
    # ------------------------------------------
    if 'no' in result_list or not result_list:
        return False
    else:
        return True


def llm_object_most(task_id, task_name, situation, situation_object, candidate_object):
    def llm(prompt):
        gpt_model = 'text-davinci-002'
        sampling_params = {"n": 1,
                           "max_tokens": 32,
                           "temperature": 0.0,
                           "top_p": 1,
                           "logprobs": 1,
                           "presence_penalty": 0,
                           "frequency_penalty": 0,
                           "stop": ['\\n', '.']}
        raw_response = openai.Completion.create(engine=gpt_model, prompt=prompt, **sampling_params)
        responses = [raw_response['choices'][i]['text'] for i in range(sampling_params['n'])]
        mean_probs = [math.exp(np.mean(raw_response['choices'][i]['logprobs']['token_logprobs'])) for i in
                      range(sampling_params['n'])]
        responses = [sample.strip().lower() for sample in responses]
        return responses, mean_probs

    fidout1 = open('experience/experience_task_' + str(task_id) + '.txt', 'a')  # create a file to store experience
    # ------------------------------------------
    # prompt design, search experience pool, query llm, and identify result
    # ------------------------------------------
    prompt = 'there are some objects, such as ' + ', '.join(candidate_object) + \
             '. which is the most suitable to replace a ' + situation_object + ' in the task of ' + task_name + \
             ' if ' + situation[:-1] + '?'
    print('\n! prompt design')
    print('raw prompt:', prompt)
    # ------------------------------------------
    # firstly search experience pool
    # ------------------------------------------
    fidout2 = open('experience/experience_task_' + str(task_id) + '.txt', 'r')
    target_prompt = 'raw prompt:' + prompt
    signal_found = False
    for line1, line2 in zip(fidout2, fidout2):
        if target_prompt in line1:
            print('! experience found')
            signal_found = True
            break
    # ------------------------------------------
    # secondly query llm
    # ------------------------------------------
    if not signal_found:
        try:
            responses, probs_1 = llm(prompt)  # get responses from llm
            resp = responses[0]
            fidout1.write('%s\n' % target_prompt)
            fidout1.write('%s\n' % resp)
            fidout1.flush()
        except:
            print('Error: no response in llm_object_most!')
    else:
        line2 = line2.strip()
        responses = line2.split(' ')
        resp = responses[0]
    print('! results from LLM')
    print('response (raw prompt):', resp)
    # ------------------------------------------
    # identify result
    # ------------------------------------------
    for item in candidate_object:
        if item in resp:
            return item


# ------------------------------------------
# how many steps in adding effect?
# (problem file) step 1: add object in objects
# (problem file) step 2: supplement init
# (problem file) step 3: change goal
# ------------------------------------------


def plan_modifier_add_effect_object(task_id, situation_predicate, situation_object, situation_object_new, selected_object, path_domain, path_problem):
    # ------------------------------------------
    # extract and analyze problem file
    # ------------------------------------------
    problem_define, problem_problem, problem_domain, problem_object, problem_init, problem_goal = extract_problem_content(path_problem)
    # ------------------------------------------
    # step 1: add object in objects
    # ------------------------------------------
    print('! step 1: supplement object')
    problem_object_new = problem_object[:-2] + ' ' + selected_object + ' - ' + situation_object + ')\n'
    print('step 1 is done.')
    # ------------------------------------------
    # step 2: supplement init
    # ------------------------------------------
    print('! step 2: supplement init')
    rule1 = re.compile(r'[(](.*?)[)]', re.S)
    problem_init_1 = re.findall(rule1, problem_init)
    problem_init_2 = []
    for item in problem_init_1:
        if (situation_object_new in item) and (situation_predicate not in item):
            problem_init_2.append(item.replace(situation_object_new, selected_object))
    problem_init_new_raw = problem_init_1 + problem_init_2
    problem_init_new = []
    for item in problem_init_new_raw:
        problem_init_new.append('(' + item + ')')
    problem_init_new = '\t' + ' '.join(problem_init_new) + ')\n'
    print('step 2 is done.')
    # ------------------------------------------
    # step 3: change goal
    # ------------------------------------------
    print('! step 3: change goal')
    rule1 = re.compile(r'[(](and.*)[)]', re.S)
    problem_goal_1 = re.findall(rule1, problem_goal)
    problem_goal_2 = problem_goal_1[0].replace(situation_object_new, selected_object)
    problem_goal_new = '\t(:goal (or ' + '(' + problem_goal_1[0] + ' ' + '(' + problem_goal_2 + '))' + '\n)'

    problem_new = [problem_define] + [problem_problem] + [problem_domain] + [problem_object_new] + [problem_init_new] + [problem_goal_new]
    user = getpass.getuser()
    problem_new_path = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_new1.pddl'
    write_file(problem_new_path, problem_new)
    print('step 3 is done.')

    domain_new_path = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_new1.pddl'
    shutil.copyfile(path_domain, domain_new_path)
    return domain_new_path, problem_new_path