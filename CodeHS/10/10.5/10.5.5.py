# use `in` to determine if `word` contains any vowels!
def contains_vowel(word):
    vowels = ['a','e','i','o','u']
    for i, vowel in enumerate(word):
        if vowel in vowels:
            return True
    return False