import torch
import openai
import numpy as np
import math
import re
import getpass
import shutil
from sentence_transformers import SentenceTransformer
from sentence_transformers import util as st_utils

# ------------------------------------------
# customized modules
# ------------------------------------------
from action_translator import action_translator
from utility import plan_manager, write_file, print_list, grammar_corrector

fidin = open('dataset/openai_api_key.txt', 'r')
key = fidin.read()
openai.api_key = key
fidin.close()

# set GPU
GPU = 0
if torch.cuda.is_available():
    torch.cuda.set_device(GPU)


def llm_utensil(target_object, task_name, candidate_utensil, option2):
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

    # ------------------------------------------
    # prompt design
    # ------------------------------------------
    prompt = 'is it ' + option2 + ' that a ' + candidate_utensil + ' replaces a ' + target_object + ' to ' + task_name + '?'
    print('\n! prompt design')
    print('raw prompt:', prompt)
    try:
        responses_1, probs_1 = llm(prompt)
    except:
        print('Error -- no response in llm_utensil!')
    print('! results from LLM')
    print('response (raw prompt):', responses_1)

    # ------------------------------------------
    # standardize responses from llm
    # ------------------------------------------
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    translation_model = 'stsb-roberta-large'
    translation_lm = SentenceTransformer(translation_model).to(device)
    template_answer_positive = candidate_utensil + ' can replace ' + target_object + '.'
    template_answer_negative = candidate_utensil + ' can not replace ' + target_object + '.'
    answer_1 = template_answer(template_answer_positive, template_answer_negative, responses_1, probs_1)
    if 'negative' in answer_1:
        print('template answer:', template_answer_negative)
        return False
    else:
        print('template answer:', template_answer_positive)
        return True


def llm_utensil_actionknowledge(path_plan, plan, task_id, situation, target_object, task_name, candidate_utensil, option2):
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

    # ------------------------------------------
    # create a file to store experience
    # ------------------------------------------
    fidout1 = open('experience/experience_task_' + str(task_id) + '.txt', 'a')
    # ------------------------------------------
    # read the decoded plan
    # ------------------------------------------
    plan_decoded = []
    next_action_index_temp = 0
    while next_action_index_temp < len(plan):
        next_action_encoded_temp = plan_manager(next_action_index_temp, path_plan)
        next_action_decoded_temp = action_translator(next_action_encoded_temp, task_id)  # decode next action
        plan_decoded.append(next_action_decoded_temp)
        next_action_index_temp = next_action_index_temp + 1
    # ------------------------------------------
    # prompt design
    # ------------------------------------------
    result_list = []  # record the result from LLM
    for sentence in plan_decoded:
        if (target_object in sentence) and ('find' not in sentence):
            new_sentence = sentence.replace(target_object, candidate_utensil)
            new_sentence = new_sentence[:-1]
            prompt = 'can a robot fill a cup with a cooking pot from a faucet in the kitchen room.\npossibility: no\n\ncan a robot fill a cup with water from a faucet in the kitchen room?\npossibility: yes\n\n' + 'can ' + new_sentence + ' ?' + '\npossibility:'
            print('\n! prompt design')
            print('raw prompt:', 'can ' + new_sentence + ' ?' + '\npossibility:')
            # ------------------------------------------
            # search experience pool
            # ------------------------------------------
            fidout2 = open('experience/experience_task_' + str(task_id) + '.txt', 'r')
            signal_experience = False  # signal if experience can be found
            target_prompt = 'raw prompt:' + 'can ' + new_sentence + '?'
            for line1, line2 in zip(fidout2, fidout2):
                if target_prompt in line1:
                    print('! experience found')
                    signal_experience = True
                    break
                else:
                    continue
            if not signal_experience:
                try:
                    responses_1, probs_1 = llm(prompt)
                    fidout1.write('%s\n' % target_prompt)
                    fidout1.write('response (raw prompt):%s\n' % responses_1)
                    fidout1.flush()
                except:
                    print('Error -- no response in llm_utensil_actionknowledge!')
            else:
                rule = re.compile(r'[[](.*?)[]]')
                line2 = line2.strip()
                responses_1 = [re.findall(rule, line2)[0]]
            print('! results from LLM')
            print('response (raw prompt):', responses_1)
            if 'no' in responses_1[0] or 'No' in responses_1[0]:
                result_list.append('no')
                break
            else:
                result_list.append('yes')
    signal = 0
    for result in result_list:
        if 'no' in result:
            signal = 1
            break
    if signal == 0:
        return True
    else:
        return False


def llm_utensil_most_possible(situation, target_object, task_name, candidate_utensil, task_id):
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

    # ------------------------------------------
    # create a file to store experience
    # ------------------------------------------
    fidout1 = open('experience/experience_task_' + str(task_id) + '.txt', 'a')
    # ------------------------------------------
    # prompt design
    # ------------------------------------------
    prompt = 'there are some utensils, such as ' + ', '.join(candidate_utensil) + '. which is the most suitable to replace a ' + target_object + ' to ' + task_name + ' if ' + situation[:-1] + '?' + ' if there is no reasonable answer, please output no.'
    print('\n! prompt design')
    print('raw prompt:', prompt)
    # ------------------------------------------
    # search experience pool
    # ------------------------------------------
    fidout2 = open('experience/experience_task_' + str(task_id) + '.txt', 'r')
    target_prompt = 'raw prompt:' + prompt
    signal_experience = False
    for line1, line2 in zip(fidout2, fidout2):
        if target_prompt in line1:
            print('! experience found')
            signal_experience = True
            break
    if not signal_experience:
        try:
            responses_1, probs_1 = llm(prompt)  # get responses from llm
            fidout1.write('%s\n' % target_prompt)
            fidout1.write('response (raw prompt):%s\n' % responses_1)
            fidout1.flush()
        except:
            print('Error -- no response in llm_utensil_most_possible!')
    else:
        rule = re.compile(r'[[](.*?)[]]')
        line2 = line2.strip()
        responses_1 = [re.findall(rule, line2)[0]]
    print('! results from LLM')
    print('response (raw prompt):', responses_1)
    for item in candidate_utensil:
        if item in responses_1[0]:
            target_utensil = item
            return target_utensil


def plan_modifier_add_effect_utensils(target_predicate, target_object, utensil, path_domain, path_problem, task_id):
    # ------------------------------------------
    # read problem file
    # ------------------------------------------
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
    # question: how many steps in adding effect?
    # step 1: add object in objects in problem file
    # step 2: change goal in problem file
    # step 3: supplement init in problem file
    # ------------------------------------------
    # ------------------------------------------
    # step 1: add object
    # ------------------------------------------
    print('! step 1: supplement object')
    problem_object_new = problem_object[:-2] + ' ' + utensil + '_1 - ' + target_object + ')\n'
    # print(problem_object_new)
    print('step 1 is done.')
    # ------------------------------------------
    # step 2: supplement init in problem file
    # ------------------------------------------
    print('! step 2: supplement init')
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
    # step 3: change goal in problem file
    # ------------------------------------------
    print('! step 3: change goal')
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
    # print_list(problem_new)
    user = getpass.getuser()
    problem_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/problem_new1.pddl'
    write_file(problem_new_path, problem_new)
    # print('path of new problem:', problem_new_path)
    print('step 3 is done.')

    domain_new_path = '/home/' + user + '/githubBase/GPT-Planner/pddl/task' + str(task_id) + '/domain_new1.pddl'
    shutil.copyfile(path_domain, domain_new_path)
    return domain_new_path, problem_new_path