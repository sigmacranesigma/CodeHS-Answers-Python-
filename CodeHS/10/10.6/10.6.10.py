word = input(str("Enter word: "))
string = input(str("Enter string: "))

def remove_all_from_string(word,part):
    
    while len(word) > 0:
        index = word.find(part)
        if index == -1:
            break
        word = word[:index] + word[index + len(part):]
    
    
    return word
    
print(remove_all_from_string(word,string))