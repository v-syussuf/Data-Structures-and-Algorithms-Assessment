import string
from collections import Counter

def word_frequency(sentence):
    
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    sentence = sentence.lower()

    
    words = sentence.split()
    frequency = Counter(words)

    return frequency


sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
