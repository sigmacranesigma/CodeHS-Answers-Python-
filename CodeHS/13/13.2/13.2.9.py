def safe_int(x):
    try:
        x = int(x)
        return x
    except ValueError:
        return 0
list_of_strings = ["a", "2", "7", "zebra"]
save = [safe_int(i) for i in list_of_strings]
print(save)
