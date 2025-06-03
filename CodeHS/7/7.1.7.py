# Use a while loop here to repeatedly ask the user for
# a denominator for as long as the denominator is 0
# (or, put another way, until the denominator is not
# equal to 0).


while True:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter denominator: "))
    if int(numerator / denominator) * denominator == numerator:
        print("Divides evenly!")
    elif denominator == 0:
        print("Cannot Divide by zero")
        break
    else:
        print("Doesn't divide evenly.")
