def replace_at_index(string, index):
    string = string[:index] + '-' + string[index + 1:]
    return string