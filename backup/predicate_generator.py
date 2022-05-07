import openai

f = open('openai_api_key.txt', "r")
key = f.read()
openai.api_key = key
f.close()


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
    result = result['text']

    return result[1:]
