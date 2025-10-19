# A simple wordle clone

import string

# All needed word info
word = "crane"
letters_in_word = list(word)
word_length = len(letters_in_word)

# print word as '_'s
display = ['_'] * word_length
print(f"letter has {word_length} letters", display)

result = ""

won = False

trys = 5

while trys > 0 and won == False:
    print(' '.join(display))
    guess = list(input("Please guess a word: ")) # Gets users word, and changes it to a list of arrays

    for i in range(len(guess)):
        if guess[i] == letters_in_word[i]:
            result += f'\033[92m{guess[i]}\033[0m'
        elif guess[i] in letters_in_word:
            result += f'\033[93m{guess[i]}\033[0m'
        else:
            result += f'\033[91m{guess[i]}\033[0m'
    trys -= 1
    print(result)
    result = ""
    if guess == letters_in_word:
        won = True
        if won == True:
            print("You won!")
        else:
            print("Out of tries")