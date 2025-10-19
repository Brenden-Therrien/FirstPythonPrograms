import random as rand

print("welcome to the guessing game!")
print("Please guess the number...")
# The random number
randNum = rand.randint(1, 100)
# Declare userGuess
userGuess = 0

while userGuess != randNum:
    userGuess = int(input())
    if (userGuess > randNum):
        print("Number is lower than that...")
    elif (userGuess < randNum):
        print("Number is higher than that...")
    else:
        print("Correct!")
        break