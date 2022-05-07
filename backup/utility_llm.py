import openai
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from sentence_transformers import util as st_utils
import math

fidin = open('openai_api_key.txt', 'r')
key = fidin.read()
openai.api_key = key
fidin.close()

# set GPU
GPU = 0
if torch.cuda.is_available():
    torch.cuda.set_device(GPU)


def predicate_generator(situation):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="tranlate a sentence into a predicate\n\n####\nsentence: The cup is broken.\npredicate: "
               "cup_is_broken\n\n####\nsentence: No water comes out of faucet.\npredicate: "
               "faucet_no_water\n\n####\nsentence: " + situation + "'\npredicate:",
        temperature=0,
        max_tokens=20,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result = response['choices'][0]
    return result['text'][1:]


def grammar_corrector(sentence):
    gpt_model = 'text-davinci-002'
    raw_response = openai.Completion.create(
        engine=gpt_model,
        prompt="Correct this to standard English:\n\n" + sentence,
        temperature=0,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response = raw_response['choices'][0]['text']
    response = response.strip()
    return response


def plan_monitor(situation, action):
    def llm(prompt):
        gpt_model = 'text-davinci-002'
        sampling_params = {"n": 1,  # sampling number
                           "max_tokens": 20,
                           "temperature": 0.1,
                           "top_p": 1,
                           "logprobs": 1,
                           "presence_penalty": 0,
                           "frequency_penalty": 0}
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
            cos_score_positive = st_utils.pytorch_cos_sim(response_embedding, model_answer_positive_embedding)[
                0].detach().cpu().numpy()
            cos_score_negative = st_utils.pytorch_cos_sim(response_embedding, model_answer_negative_embedding)[
                0].detach().cpu().numpy()
            sum_cos_score_positive += cos_score_positive * prob
            sum_cos_score_negative += cos_score_negative * prob
        if sum_cos_score_positive > sum_cos_score_negative:
            return 'model_answer_positive'
        else:
            return 'model_answer_negative'

    # prompt design
    prompt = 'Is it recommended that ' + action[:-1] + ', if ' + situation[:-1] + '?'
    refined_prompt = grammar_corrector(prompt)
    print('# ---------- prompt design -----------')
    print('raw prompt:', prompt)
    print('refined prompt:', refined_prompt)
    try:
        responses_1, probs_1 = llm(prompt)  # get responses from llm
        responses_2, probs_2 = llm(refined_prompt)
    except:
        print('Error -- no response from LLM!')
    print('# ---------- response from LLM -----------')
    print('response (raw prompt):', responses_1)
    print('probs:', round(probs_1, 2))
    print('response (refined prompt):', responses_2)
    print('probs:', round(probs_2, 2))

    # standardize responses from llm
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    translation_model = 'stsb-roberta-large'
    translation_lm = SentenceTransformer(translation_model).to(device)
    model_answer_positive = 'The action is recommended.'
    model_answer_negative = 'The action recommended.'
    answer_1 = model_answer(model_answer_positive, model_answer_negative, responses_1, probs_1)
    answer_2 = model_answer(model_answer_positive, model_answer_negative, responses_2, probs_2)
    if 'positive' in answer_2:
        return 'The action can still be executed.'
    elif 'negative' in answer_2:
        return 'The action can not be executed.'
    else:
        print('Error -- no result in model_answer!')