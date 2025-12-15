import llmintegrator


def generate_sarcastic_words():

    llm = llmintegrator.LLMIntegrator()
    llm.model_name = "granite4:latest"
    # fallback list in case LLM fails
    words = ['quantum physics', 'serendipity', 'the art of procrastination', 'existential dread', 'the philosophy of '
                                                                                                  'nothingness', 'the beauty of monotony', 'the allure of simplicity', 'the complexity of simplicity', 'the irony of being ironic', 'the paradox of non-sequiturs', 'the humor in tragedy', 'the tragedy in comedy', 'the joy in sadness', 'the sadness in joy', 'the lightness of gravity', 'the heaviness of air', 'the weightlessness of dreams', 'the solidity of illusions', 'the fluidity of stillness', 'the motion of inaction']

    r = llm.generate_response("give me a python array with 20 random sarcastic topic words from any category. start with "
                              "words = [ and end with ] and separate each word with a comma. and put each word in quotation marks. dont comment on it and dont add any extra text. your response will be used directly in an exec() function.")


    try:
        exec('words = ' + r)
        print(words)

    except Exception as e:
        print("Error executing generated code:", e)
        print(r)
    return words

if __name__ == "__main__":
    generate_sarcastic_words()


