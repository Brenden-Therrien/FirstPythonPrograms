# A simple wordle clone

import string

# All needed word info
word = "crane"
word_length = len(word)

# print word as '_'s
display = ['_'] * word_length
print(f"Word has {word_length} letters", display)

result = ""

won = False

tries = 5

while tries > 0 and won == False:
    print(' '.join(display))
    # Gets users word, and changes it to a list of arrays
    guess = input("Please guess a word: ")
    letters_in_guess = list(guess)
    results = ['' for _ in word]
    letters_in_word = list(word)

    for i in range(len(letters_in_guess)):
        if letters_in_guess[i] == letters_in_word[i]:
            results[i] = f'\033[92m{letters_in_guess[i]}\033[0m'
            letters_in_word[i] = " "
            letters_in_guess[i] = " "

    for i in range(len(letters_in_guess)):
        if letters_in_guess[i] != " ":
            if letters_in_guess[i] in letters_in_word:
                results[i] = f'\033[93m{letters_in_guess[i]}\033[0m'
                j = letters_in_word.index(letters_in_guess[i])
                letters_in_word[j] = " "
                letters_in_guess[i] = " "

    for i in range(len(letters_in_guess)):
        if letters_in_guess[i] != " ":
            results[i] = f'\033[91m{letters_in_guess[i]}\033[0m'
            
    result = "".join(results)        
    tries -= 1
    print(result)
    result = ""
    if guess == word:
        won = True
        if won:
            print("You won!")
    elif tries == 0:
        print("Out of tries")