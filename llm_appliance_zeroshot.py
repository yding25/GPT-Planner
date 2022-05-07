import torch
import openai
import numpy as np
import math
import time
import re
import getpass
from sentence_transformers import SentenceTransformer
from sentence_transformers import util as st_utils

# customized modules
from utility import write_file, print_list, grammar_corrector

fidin = open('dataset/openai_api_key.txt', 'r')
key = fidin.read()
openai.api_key = key
fidin.close()

# set GPU
GPU = 0
if torch.cuda.is_available():
    torch.cuda.set_device(GPU)


def llm_appliance(situation, opp_situation, candidate_appliance, option3):
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

    def template_answer(template_answer_positive, template_answer_negative, responses, probs):
        template_answer_positive_embedding = translation_lm.encode(template_answer_positive, batch_size=512, convert_to_tensor=True, device=device)
        template_answer_negative_embedding = translation_lm.encode(template_answer_negative, batch_size=512, convert_to_tensor=True, device=device)
        sum_cos_score_positive = 0
        sum_cos_score_negative = 0
        responses_probs = list(zip(responses, probs))
        for (res, prob) in responses_probs:
            response_embedding = translation_lm.encode(res, batch_size=512, convert_to_tensor=True, device=device)
            # calculate cosine similarity against each candidate sentence in the corpus
            cos_score_positive = st_utils.pytorch_cos_sim(response_embedding, template_answer_positive_embedding)[0].detach().cpu().numpy()
            cos_score_negative = st_utils.pytorch_cos_sim(response_embedding, template_answer_negative_embedding)[0].detach().cpu().numpy()
            sum_cos_score_positive += cos_score_positive * prob
            sum_cos_score_negative += cos_score_negative * prob
        if sum_cos_score_positive > sum_cos_score_negative:
            return 'template_answer_positive'
        else:
            return 'template_answer_negative'

    # prompt design
    prompt = 'Is it ' + option3 +' to use a ' + candidate_appliance + ' to make ' + opp_situation[:-1] + ' if ' + situation[:-1] + '?'
    print('\n! prompt design')
    refined_prompt = grammar_corrector(prompt)
    print('prompt (raw):', prompt)
    print('prompt (refined):', refined_prompt)
    try:
        responses_1, probs_1 = llm(prompt)
        responses_2, probs_2 = llm(refined_prompt)
    except:
        print('Error -- no response in llm_appliance!')
    print('! results from LLM')
    print('response (raw prompt):', responses_1)
    # print('corresponding probs:', probs_1)
    print('response (refined prompt):', responses_2)
    # print('corresponding probs:', probs_2)

    # standardize responses from llm
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    translation_model = 'stsb-roberta-large'
    translation_lm = SentenceTransformer(translation_model).to(device)
    template_answer_positive = candidate_appliance + ' can do that.'
    template_answer_negative = candidate_appliance + ' can not do that.'
    answer_1 = template_answer(template_answer_positive, template_answer_negative, responses_1, probs_1)
    answer_2 = template_answer(template_answer_positive, template_answer_negative, responses_2, probs_2)
    if ('negative' in answer_1) or ('negative' in answer_2):
        print('template answer:', template_answer_negative)
        return False
    else:
        print('template answer:', template_answer_positive)
        return True


def llm_appliance_most_possible(situation, opp_situation, candidate_appliances):
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

    # prompt design
    prompt = 'There are some appliances, such as ' + ', '.join(candidate_appliances) + '. \nWhich is the most possible to make ' + opp_situation[:-1] + ' if ' + situation[:-1] + '?'
    print('\n! prompt design')
    print('raw prompt:', prompt)
    try:
        responses_1, probs_1 = llm(prompt)  # get responses from llm
    except:
        print('Error -- no response in llm_appliance_most_possible!')
    print('! results from LLM')
    print('response (raw prompt):', responses_1)
    # print('probs:', probs_1)
    for item in candidate_appliances:
        if item in responses_1[0]:
            target_appliance = item
            return target_appliance


def plan_modifier_add_effect_appliances(predicate, object, appliance, path_domain, path_problem, task_id):
    target_action = 'operate'
    target_object = object
    target_predicate = predicate

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

    # ------------------------------------------
    # step 1: change effect
    # ------------------------------------------
    print('! step 1: add effect')
    # add effect
    rule1 = re.compile(r'[(](and .*)[)]', re.S)
    effect_1 = re.findall(rule1, action_effect)
    effect_2 = '(not (' + target_predicate + ' ?' + target_object[0] + '))'
    new_effect = effect_1[0] + ' ' + effect_2
    action_effect_new = ':effect (' + new_effect + ')'
    print('step 1 is done.')

    # ------------------------------------------
    # step 2: change parameter
    # ------------------------------------------
    print('! step 2: add parameter')
    parameter_1 = action_parameters[:-1]
    parameter_2 = '?' + target_object[0] + ' - ' + target_object + ')'
    action_parameters_new = parameter_1 + ' ' + parameter_2

    target_action_part_new = '\t' + action_name + '\n' + '\t\t' + action_parameters_new + '\n' + '\t\t' + action_precondition + '\n' + '\t\t' + action_effect_new + '\n'
    # print('updated action in new domain.pddl:')
    # print(target_action_part_new)
    domain_new = target_action_part_before + [target_action_part_new] + target_action_part_after
    user = getpass.getuser()
    domain_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_new2.pddl'
    write_file(domain_new_path, domain_new)
    # print('path of new domain file:', domain_new_path)

    problem = []
    fidin = open(path_problem, 'r')
    for line in fidin.readlines():
        problem.append(line)
    fidin.close()
    # print('problem:')
    # print_list(problem)
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
    print('step 2 is done.')

    # ------------------------------------------
    # step 3: change init
    # ------------------------------------------
    print('! step 3: supplement init')
    # add fact in init
    problem_init_new = problem_init[:-2] + ' (appliance_at ' + appliance + ' kitchen))\n'
    print('step 3 is done.')

    # ------------------------------------------
    # step 4: supplement object
    # ------------------------------------------
    print('! step 4: supplement object')
    # add object
    problem_object_new = problem_object[:-2] + ' ' + appliance + ' - appliance)\n'

    problem_new = [problem_define] + [problem_problem] + [problem_domain] + [problem_object_new] + [problem_init_new] + [problem_goal]
    # print('problem_new:')
    # print_list(problem_new)
    user = getpass.getuser()
    problem_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_new2.pddl'
    write_file(problem_new_path, problem_new)
    # print('path of new domain:', problem_new_path)
    print('step 4 is done.')

    return domain_new_path, problem_new_path