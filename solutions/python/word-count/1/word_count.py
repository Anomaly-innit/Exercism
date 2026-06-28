import string
import re
def count_words(sentence):
    sentence = sentence.lower()
    split_sentence = re.split(r"[^\w']|_", sentence)
    result = {}
    for word in split_sentence:
        word = word.strip(string.punctuation)
        if word:
            result[word] = result.get(word, 0) + 1
    return result
        