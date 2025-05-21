def replace_at_index(string, index): #function that returns a string and replaces a letter with a "-"
    replacement = "-"
    return string[ :index] + replacement + string[index+1: ]
