tuple_list = [] #creates a variable to store a list of tuples
numx = [] #creates a variable to store a list of x coordinates
numy = [] #creates a variable to store a list of y coordinates
slope = [] #creates a variable to store a list of slope values

for i in range(5): #loops 5 times
    x = int(input("Enter a number: ")) #asks the user for inputs
    y = int(input("Enter a number: "))
    numx.append(x) #stores all the x coordinates into the numx list
    numy.append(y) #stores all the y coordinates into the numx list
    a_tuple = (x, y) #makes a tuple using the coordinates
    tuple_list.append(a_tuple) #stores the tuple into a list
print(tuple_list) #print the list when loop is finsihed

index = 0 #creates a base counter variable
index_two = 1 #creates a base counter variable
for i in range(4): #loops 4 times
    changey = numy[index] - numy[index_two] #finds the change in y between two coordinates
    changex = numx[index] - numx[index_two] #finds the change in x
    slope_value = changey / changex #finds the slope using change in y and change in x
    slope.append(slope_value) #adds the slope value to a list
    print(f"Slope between {tuple_list[index]} and {tuple_list[index_two]}: {slope[index]}") #prints the new slope value every time the loops runs
    index += 1 #adds to the counter
    index_two += 1
