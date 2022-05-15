import openai
import numpy as np
import math
import re
import getpass

# ------------------------------------------
# customized modules
# ------------------------------------------
from utility import extract_action_content, extract_problem_content, write_file, template_response

user = getpass.getuser()

fidin = open('dataset/openai_api_key.txt', 'r')
key = fidin.read()
openai.api_key = key
fidin.close()


def llm_appliance(situation, opp_situation, candidate_appliance, task_id):
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
    # prompt design, search experience pool, query llm, and identify result
    # ------------------------------------------
    prompt = 'can a microwave make water clean if water is dirty?\nanswer: no\n\n' \
             'can a water filter make water clean if water is dirty?\nanswer: yes\n\n' \
             + 'can a ' + candidate_appliance + ' make ' + opp_situation[:-1] + ' if ' + situation[:-1] + '? \nanswer:'
    print('\n! prompt design')
    print('prompt (raw):', 'can a ' + candidate_appliance + ' make ' + opp_situation[:-1] + ' if ' + situation[:-1] + '? \nanswer:')
    # ------------------------------------------
    # firstly search experience pool
    # ------------------------------------------
    fidout2 = open('experience/experience_task_' + str(task_id) + '.txt', 'r')
    signal_experience = False
    target_prompt = 'prompt (raw):' + 'can a ' + candidate_appliance + ' make ' + opp_situation[:-1] + ' if ' + situation[:-1] + '?'
    for line1, line2 in zip(fidout2, fidout2):
        if target_prompt in line1:
            print('! experience found')
            signal_experience = True
            break
        else:
            continue
    # ------------------------------------------
    # secondly query llm
    # ------------------------------------------
    if not signal_experience:
        try:
            responses, probs_1 = llm(prompt)
            resp = template_response(responses[0])
            fidout1.write('%s\n' % target_prompt)
            fidout1.write('%s\n' % resp)
            fidout1.flush()
        except:
            print('Error: no response in llm_appliance!')
    else:
        line2 = line2.strip()
        responses = line2.split(' ')
        resp = responses[0]
    print('! results from LLM')
    print('response (raw prompt):', resp)
    # ------------------------------------------
    # identify result
    # ------------------------------------------
    if 'no' in resp[0:2] or 'No' in resp[0:2]:
        return False
    else:
        return True


def llm_appliance_most(situation, opp_situation, candidate_appliances, task_id):
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
    # prompt design, search experience pool, query llm, and identify result
    # ------------------------------------------
    prompt = 'there are some appliances, such as ' + ', '.join(candidate_appliances) + \
             '. which is the most possible to make ' + opp_situation[:-1] + \
             ' if ' + situation[:-1] + '?'
    print('\n! prompt design')
    print('raw prompt:', prompt)
    # ------------------------------------------
    # firstly search experience pool
    # ------------------------------------------
    fidout2 = open('experience/experience_task_' + str(task_id) + '.txt', 'r')
    signal_experience = False
    target_prompt = 'raw prompt:' + prompt
    for line1, line2 in zip(fidout2, fidout2):
        if target_prompt in line1:
            print('! experience found')
            signal_experience = True
            break
        else:
            continue
    # ------------------------------------------
    # secondly query llm
    # ------------------------------------------
    if not signal_experience:
        try:
            responses, probs_1 = llm(prompt)  # get responses from llm
            resp = responses[0]
            fidout1.write('%s\n' % target_prompt)
            fidout1.write('%s\n' % resp)
            fidout1.flush()
        except:
            print('Error: no response in llm_appliance_most!')
    else:
        line2 = line2.strip()
        responses = line2.split(' ')
        resp = responses[0]
    print('! results from LLM')
    print('response (raw prompt):', resp)
    # ------------------------------------------
    # identify result
    # ------------------------------------------
    for item in candidate_appliances:
        if item in resp:
            target_appliance = item
            return target_appliance


# ------------------------------------------
# how many steps in adding effect?
# (domain file) step 1: change effect to 'operate'
# (domain file) step 2: change parameter
# (problem file) step 3: change init
# (problem file) step 4: supplement object
# ------------------------------------------


def plan_modifier_add_effect_appliance(task_id, situation_predicate, situation_object, selected_appliance, path_domain, path_problem):
    target_action = 'operate'
    # ------------------------------------------
    # extract and analyze action content in domain.pddl
    # ------------------------------------------
    domain, action_part, action_part_before, action_part_after, action_name, action_parameters, action_precondition, action_effect = extract_action_content(path_domain, target_action)
    # ------------------------------------------
    # step 1: change effect to 'operate'
    # ------------------------------------------
    print('! step 1: add effect')
    rule1 = re.compile(r'[(](and .*)[)]', re.S)
    effect_1 = re.findall(rule1, action_effect)
    effect_2 = '(not (' + situation_predicate + ' ?' + situation_object[0] + '))'
    effect_new = effect_1[0] + ' ' + effect_2
    action_effect_new = ':effect (' + effect_new + ')'
    print('step 1 is done.')
    # ------------------------------------------
    # step 2: change parameter
    # ------------------------------------------
    print('! step 2: add parameter')
    parameter_1 = action_parameters[:-1]
    parameter_2 = '?' + situation_object[0] + ' - ' + situation_object + ')'
    action_parameters_new = parameter_1 + ' ' + parameter_2
    action_part_new = '\t' + action_name + '\n' + '\t\t' + action_parameters_new + '\n' + '\t\t' + action_precondition + '\n' + '\t\t' + action_effect_new + '\n'
    domain_new = action_part_before + [action_part_new] + action_part_after
    domain_new_path = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/domain_new2.pddl'
    write_file(domain_new_path, domain_new)
    print('step 2 is done.')
    # ------------------------------------------
    # extract and analyze content in problem.pddl
    # ------------------------------------------
    problem_define, problem_problem, problem_domain, problem_object, problem_init, problem_goal = extract_problem_content(path_problem)
    problem_goal = problem_goal + ')'
    # ------------------------------------------
    # step 3: change init
    # ------------------------------------------
    print('! step 3: supplement init')
    problem_init_new = problem_init[:-2] + ' (appliance_at ' + selected_appliance + ' kitchen))\n'
    print('step 3 is done.')
    # ------------------------------------------
    # step 4: supplement object
    # ------------------------------------------
    print('! step 4: supplement object')
    problem_object_new = problem_object[:-2] + ' ' + selected_appliance + ' - appliance)\n'
    problem_new = [problem_define] + [problem_problem] + [problem_domain] + [problem_object_new] + [problem_init_new] + [problem_goal]
    problem_new_path = '/home/' + user + '/GPT-Planner/pddl/task' + str(task_id) + '/problem_new2.pddl'
    write_file(problem_new_path, problem_new)
    print('step 4 is done.')

    return domain_new_path, problem_new_path