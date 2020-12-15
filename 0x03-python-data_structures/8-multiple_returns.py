#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        first_character = sentence[0]
        largo_sentence = len(sentence)
        return (largo_sentence, first_character)
    else:
        return (largo_sentence, None)
