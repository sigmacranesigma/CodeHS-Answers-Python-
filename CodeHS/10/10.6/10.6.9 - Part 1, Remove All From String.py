def remove_all_from_string(word, letter):
    while word.find(letter) != -1:
        index = word.find(letter)
        word = word[:index] + word[index + 1:]
    return word
