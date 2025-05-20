def Fahrenheit(celsius): #function that turns celsius to fahrenheit
    fahrenheit = celsius * 1.8
    fahrenheit = fahrenheit + 32
    return print(fahrenheit)

def Celsius(fahrenheit): #function that turns fahrenheit to celsius
    celsius = fahrenheit - 32
    celsius = celsius / 1.8
    return print(celsius)

# Change 0C to F:
Fahrenheit(0)

# Change 100C to F:
Fahrenheit(100)

# Change 40F to C:
Celsius(40)

# Change 80F to C:
Celsius(80)
