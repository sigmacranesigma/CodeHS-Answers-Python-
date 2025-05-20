one = int(input("Enter a number: ")) #asks the user for numbers
two = int(input("Enter another number: "))
operation = input("Choose and operation (add, subtract, multiply, divide): ") #asks the user for operation that they want

def add(): #functions for each operation
    print(f"{one} + {two} = {one+two}")
def subtract():
    print(f"{one} - {two} = {one-two}")
def multiply():
    print(f"{one} * {two} = {one*two}")
def division(): #an extra that I added this part is not necessary 
    print(f"{one} / {two} = {one/two}")
if operation == "add": #if statement to check the user input
    add()
elif operation == "subtract":
    subtract()
elif operation == "multiply":
    multiply()
elif operation == "divide": #this part here is also not needed
    division()
else:
    print("Invalid input") #prints invalid input if anything else is inputted
