import openai
import numpy as np
import math
import time
import key


def llm_appliance_most_possible(situation, opp_situation, candidate_appliances):
    def llm(prompt, gpt_model, sampling_params):
        raw_response = openai.Completion.create(engine=gpt_model, prompt=prompt, **sampling_params)
        responses = [raw_response['choices'][i]['text'] for i in range(sampling_params['n'])]
        mean_probs = [math.exp(np.mean(raw_response['choices'][i]['logprobs']['token_logprobs'])) for i in
                      range(sampling_params['n'])]
        responses = [sample.strip().lower() for sample in responses]
        time.sleep(1)
        return responses, mean_probs

    # openai_key = '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'
    openai_key = key.value
    gpt_model = 'text-davinci-002'
    openai.api_key = openai_key
    sampling_params = {"max_tokens": 64,
                       "temperature": 0.1,
                       "top_p": 1,
                       "n": 1,
                       "logprobs": 1,
                       "presence_penalty": 0,
                       "frequency_penalty": 0}
    # prompt design
    prompt = 'There are some appliances, such as ' + ', '.join(candidate_appliances) + '. \nWhich is the most possible to make ' + opp_situation[:-1] + ' if ' + situation[:-1] + '?'
    print('#---------- prompt -----------')
    print('raw prompt:', prompt)
    try:
        responses_1, probs_1 = llm(prompt, gpt_model, sampling_params)  # get responses from llm
    except:
        print('error 1 in llm_appliance_best!')
    print('#---------- results from GPT-3 -----------')
    print('response from GPT-3 (raw prompt):', responses_1)
    print('corresponding probs:', probs_1)
    for item in candidate_appliances:
        if item in responses_1[0]:
            target_appliance = item
            return target_appliance
