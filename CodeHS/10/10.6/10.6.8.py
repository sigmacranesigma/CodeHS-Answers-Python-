def name_contains(name,letter):
    newist = list(name.strip())
    for i in newist:
        if i == letter:
            return True
        else:
            continue
    return False