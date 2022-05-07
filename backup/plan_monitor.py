import openai
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from sentence_transformers import util as st_utils
import math
from grammar_corrector import grammar_corrector
import time
import key


def plan_monitor(situation, action):
    def llm(prompt, gpt_model, sampling_params):
        raw_response = openai.Completion.create(engine=gpt_model, prompt=prompt, **sampling_params)
        responses = [raw_response['choices'][i]['text'] for i in range(sampling_params['n'])]
        mean_probs = [math.exp(np.mean(raw_response['choices'][i]['logprobs']['token_logprobs'])) for i in
                          range(sampling_params['n'])]
        responses = [sample.strip().lower() for sample in responses]
        time.sleep(1)
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
            # print('positive:', cos_score_positive)
            # print('negative:', cos_score_negative)
            sum_cos_score_positive += cos_score_positive * prob
            sum_cos_score_negative += cos_score_negative * prob
        if sum_cos_score_positive > sum_cos_score_negative:
            return 'model_answer_positive'
        else:
            return 'model_answer_negative'

    # openai_key = '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'
    openai_key = key.value
    gpt_model = 'text-davinci-002'
    openai.api_key = openai_key
    sampling_params = {"max_tokens": 20,
                       "temperature": 0.1,
                       "top_p": 1,
                       "n": 1,
                       "logprobs": 1,
                       "presence_penalty": 0,
                       "frequency_penalty": 0
                       }

    # prompt design
    prompt = 'Is it recommended that ' + action[:-1] + ', if ' + situation[:-1] + '?'
    print('#---------- prompt -----------')
    print('raw prompt:', prompt)
    refined_prompt = grammar_corrector(prompt)
    print('refined prompt:', refined_prompt)
    try:
        responses_1, probs_1 = llm(prompt, gpt_model, sampling_params)  # get responses from llm
        responses_2, probs_2 = llm(refined_prompt, gpt_model, sampling_params)  # get responses from llm
    except:
        print('error 1 in plan_monitor!')
    print('#---------- results from GPT-3 -----------')
    print('response from GPT-3 (raw prompt):', responses_1)
    print('corresponding probs:', probs_1)
    print('response from GPT-3 (refined prompt):', responses_2)
    print('corresponding probs:', probs_2)

    # set GPU
    GPU = 0
    if torch.cuda.is_available():
        torch.cuda.set_device(GPU)

    # standardize responses from llm
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    translation_model = 'stsb-roberta-large'
    translation_lm = SentenceTransformer(translation_model).to(device)
    model_answer_positive = 'It is recommended.'
    model_answer_negative = 'It is not recommended.'
    answer_1 = model_answer(model_answer_positive, model_answer_negative, responses_1, probs_1)
    answer_2 = model_answer(model_answer_positive, model_answer_negative, responses_2, probs_2)
    if 'positive' in answer_2:
        return 'The action can still be executed.'
    elif 'negative' in answer_2:
        return 'The action can not be executed.'
    else:
        print('error 2 in plan_monitor!')