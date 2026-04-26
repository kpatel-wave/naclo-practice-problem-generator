import random

def generate_random_word(length=2):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'k', 'n', 's', 't', 'm', 'p', 'l']
    word = ""
    for _ in range(length):
        word += random.choice(consonants) + random.choice(vowels)
    return word
