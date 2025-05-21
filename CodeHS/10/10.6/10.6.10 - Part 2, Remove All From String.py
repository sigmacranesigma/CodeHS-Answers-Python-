word = input("Enter a word: ")
string = input(str("Enter a string: "))

def remove_all_from_string(word, string):
    while len(word) > 0:
        index = word.find(string)
        if index == -1:
            break
        word = word[:index] + word[index + len(string):]
    return word
print(remove_all_from_string(word, string))
