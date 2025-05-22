def replace_at_index(string, index, char):
    string = string[:index] + char + string[index + 1:]
    return string