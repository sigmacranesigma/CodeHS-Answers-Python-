def Fahrenheit(celsius): #function that turns celsius to fahrenheit
    try:
        fahrenheit = celsius * 1.8
        fahrenheit = fahrenheit + 32
        fahrenheit = round(fahrenheit, 0)
        return print(fahrenheit)
    except ValueError:
        print("Please enter a number.")

def Celsius(fahrenheit): #function that turns fahrenheit to celsius
    try:
        celsius = fahrenheit - 32
        celsius = celsius / 1.8
        celsius = round(celsius, 0)
        return print(celsius)
    except ValueError:
        print("Please enter a number.")
    
c_f = input("Celsius or Fahrenheit: ") #asks the user for an input
if c_f == "Celsius": #checks the user input
    fahrenheit = float(input("Enter a value (don't put a degree symbol): ")) #runs the function that matches the user input
    Celsius(fahrenheit)
elif c_f == "Fahrenheit":
    celsius = float(input("Enter a value (don't put a degree symbol): "))
    Fahrenheit(celsius)
else:
    print("Invalid input") #if input is not any of the other ones
