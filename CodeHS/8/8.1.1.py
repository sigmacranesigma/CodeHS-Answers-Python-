print("Password Authentication Program\n")


tries = 3

password = '12345'


for i in range(3):
    check = str(input("Enter your password: "))
    if password == check:
        print("Correct password! Acess granted.")
        break
    elif tries == 1:
        print('Incorrect password. Maximum number of attempts reached. Access denied.')
        tries -= 1
    else:
        tries -= 1
        print(f'Incorrect password. You have {tries} attempts left. Please try again.')
