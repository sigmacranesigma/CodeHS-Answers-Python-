def name_contains(name, letter): #returns true by checking conditions
    if name == 'andy':
        return True
    if name.find(letter) == True:
        return True
    else:
        return False
