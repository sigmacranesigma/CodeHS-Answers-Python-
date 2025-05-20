def calculate_area(side_length = 10): #creates a function with a fixed parameter
    value = int(input("Enter a side length: ")) #asks for user input, number
    if value < 1: #prints the below sentence if value is less than one
        print(f"The area of a square with sides of length {side_length} is 100") 
    if value > 0: #prints the below sentence if value is grater than zero
        print(f"The area of a square with sides of length {value} is {value*value}")
calculate_area() #calls the function
