import openai
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from sentence_transformers import util as st_utils
import math


def plan_monitor(prompt_missing):
    def llm(prompt, gpt_model, sampling_params):
        raw_response = openai.Completion.create(engine=gpt_model, prompt=prompt, **sampling_params)
        responses = [raw_response['choices'][i]['text'] for i in range(sampling_params['n'])]
        mean_probs = [math.exp(np.mean(raw_response['choices'][i]['logprobs']['token_logprobs'])) for i in
                          range(sampling_params['n'])]
        responses = [sample.strip().lower() for sample in responses]
        return responses, mean_probs

    def model_answer(model_answer_positive, model_answer_negative, responses, probs):
        model_answer_positive_embedding = translation_lm.encode(model_answer_positive, batch_size=512,
                                                                convert_to_tensor=True, device=device)
        model_answer_negative_embedding = translation_lm.encode(model_answer_negative, batch_size=512,
                                                                convert_to_tensor=True, device=device)
        sum_cos_score_positive = 0
        sum_cos_score_negative = 0
        responses_probs = list(zip(responses, probs))
        for (res, prob) in responses_probs:
            response_embedding = translation_lm.encode(res, batch_size=512, convert_to_tensor=True, device=device)
            # calculate cosine similarity against each candidate sentence in the corpus
            cos_score_positive = st_utils.pytorch_cos_sim(response_embedding, model_answer_positive_embedding)[0].detach().cpu().numpy()
            cos_score_negative = st_utils.pytorch_cos_sim(response_embedding, model_answer_negative_embedding)[0].detach().cpu().numpy()
            sum_cos_score_positive += cos_score_positive * prob
            sum_cos_score_negative += cos_score_negative * prob
        if sum_cos_score_positive > sum_cos_score_negative:
            return 'model_answer_positive'
        else:
            return 'model_answer_negative'

    # define llm hyperparameters
    openai_key = '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'
    gpt_model = 'text-davinci-002'
    openai.api_key = openai_key
    sampling_params = {"max_tokens": 64,
                       "temperature": 0,
                       "top_p": 0.95,
                       "n": 3,
                       "logprobs": 1,
                       "presence_penalty": 0,
                       "frequency_penalty": 0,
                       "stop": '\n'}

    # prompt design
    goal = 'Check if the action can be executed given a situation.\n\n'
    example1 = '###\nTask name: drinking water\n \nSituation: a cup is broken.\nNext action: a robot finds a ' \
               'faucet in kitchen room.\nQuestion: can the next action still be executed?\nAnswer: next ' \
               'action can still be executed.\n\n'
    example2 = '###\nTask name: drinking water\n \nSituation: a cup is broken.\nNext action: a robot holds a cup ' \
               'in kitchen room.\nQuestion: can the next action still be executed?\nAnswer: next action ' \
               'cannot be executed.\n\n'
    # example1 = '###\nTask name: drinking water\nPlan: Step 1: a robot walks from dining room to kitchen room. Step 2: ' \
    #            'a robot finds a cup in kitchen room.\nSituation: a cup is broken.\nNext action: a robot finds a ' \
    #            'faucet in kitchen room.\nQuestion: can the robot still execute next action?\nAnswer: next ' \
    #            'action can still be executed.\n\n'
    # example2 = '###\nTask name: drinking water\nPlan: Step 1: a robot walks from dining room to kitchen room. Step 2: ' \
    #            'a robot finds a cup in kitchen room.\nSituation: a cup is broken.\nNext action: a robot holds a cup ' \
    #            'in kitchen room.\nQuestion: can the robot still execute next action?\nAnswer: next action ' \
    #            'cannot be executed.\n\n'
    prompt_fixed = goal + example1 + example2
    prompt = prompt_fixed + prompt_missing
    print('#---------- full prompt -----------')
    print(prompt)
    # print('#---------- added prompt -----------')
    # print(prompt_missing)
    # get responses from llm
    responses, probs = llm(prompt, gpt_model, sampling_params)
    print('#---------- results from GPT-3 -----------')
    print('raw response from GPT-3:', responses)
    print('probs:', probs)

    # set GPU
    GPU = 0
    if torch.cuda.is_available():
        torch.cuda.set_device(GPU)

    # standardize responses from llm
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    translation_model = 'stsb-roberta-large'
    translation_lm = SentenceTransformer(translation_model).to(device)
    model_answer_positive = 'The next action can still be executed.'
    model_answer_negative = 'The next action can not be executed.'

    answer = model_answer(model_answer_positive, model_answer_negative, responses, probs)
    if 'positive' in answer:
        return model_answer_positive
    elif 'negative' in answer:
        return model_answer_negative
    else:
        print('error!')


# # test case 1
# plan = '###\nTask name: drinking water\nPlan: Step 1: a robot walks from dining room to kitchen room; Step 2: a robot ' \
#        'finds a cup in kitchen room.'
# situation = '\nSituation: a cup is broken.'
# nextaction = '\nNext action: a robot turns on a faucet in kitchen room.'
# question = '\nQuestion: can the robot still execute the next action?\nAnswer:'
# prompt_missing = plan + situation + nextaction + question
# print('final result:', plan_monitor(prompt_missing))

# # test case 2
# goal = 'Check if the next step can be executed given a situation.\n\n'
# plan = '###\nTask name: drinking water\nPlan: Step 1: a robot walks from dining room to kitchen room; Step 2: a robot ' \
#        'finds a cup in kitchen room. '
# situation = '\nSituation: a cup is broken.'
# nextaction = '\nNext action: a robot holds a cup in kitchen room.'
# question = '\nQuestion: can the robot still execute the next action?\nAnswer:'
# prompt_missing = plan + situation + nextaction + question
# print('final result:', plan_monitor(prompt_missing))
