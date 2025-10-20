# password generator, with password length

import random as rand
import string

print("this is a password generator.")
passLength = int(input("First, what length do you want the password to be: "))
print(f"password length will be", passLength)

def generateRandString(length):
    # All letters, numbers, and symbols
    chars = string.ascii_letters + string.punctuation + string.digits
    # get random character
    randChars = rand.choices(chars, k=passLength)
    # This returns the random characters at a string
    return "".join(randChars)

passowrd = generateRandString(passLength)
print(passowrd)