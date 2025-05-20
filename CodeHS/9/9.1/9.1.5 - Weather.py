def sunny(): #function for if it is sunny
    print("On a sunny day, sandals are the norm.")
  
def rainy(): #function for if it is rainy
    print("On a rainy day, galoshes are appropriate footwear.")
  
def snowy(): #function for if it is snowy
    print("On a snowy day, you should wear boots.")
  
weather = input("What is the weather? (sunny, rainy, snowy): ") #asks the user for the weather

if weather == "sunny": #if statements that gives different answers depending on the input
    sunny()
elif weather == "rainy":
    rainy()
elif weather == "snowy":
    snowy()
else: #if the user inputs something other than the valid options, the code prints this
    print("Invalid input")
