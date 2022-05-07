import time

import openai

openai_key = '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'
openai.api_key = openai_key


def grammar_corrector(sentence):
    raw_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Correct this to standard English:\n\n" + sentence,
        temperature=0,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response = raw_response['choices'][0]['text']
    response = response.strip()
    time.sleep(1)
    return response


# test = 'if cup is dirty, is recommended to the robot fills cup with water from faucet in kitchen room?'
# result = grammar_corrector(test)
# print(result)
