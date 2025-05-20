def positive(): #a function that repeats until the user inputs a positive number
    while True:
        try:
            num = int(input("Enter a postive number: "))
            if num < 0:
                print("The number must be positive!")
                continue
            else:
                break
        except ValueError:
            print("That wasn't a number!")
            continue
    return print(num)
positive() #calls a function
