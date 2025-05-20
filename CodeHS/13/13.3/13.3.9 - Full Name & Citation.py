first = input("Enter your first name: ") #asks for user input, name
last = input("Enter your last name: ")
print(f"Full name: {first} {last}") #prints the full name
first, last = last, first #swaps the variable values
print(f"Citation: {first}, {last}") #prints the citation
