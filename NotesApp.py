# Simple app that allows you to write + save notes to a seperate file you can call back to (Learning file I/O)

import os
import datetime

while True:
    print(" Notes App")
    print("1. Take notes")
    print("2. View notes")
    print("3. Remove notes")
    print("4. Quit")

    result = input("What would you like to do?")

    if result == '4':
        print("Goodbye")
        break # Breaks out of the loop ("Quit app")

    # Write notes
    elif result == '1':
        with open(f"new.txt", "a") as f:
            timestamp = f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M" + '\n')) # Date, and time
            content = f.write(input() + '\n')


    # read from notes
    elif result == '2':
        with open('new.txt', 'r') as f:
            reading = f.read()
            print(reading)

    # Delete notes
    elif result == '3':
        filename = input("What file would you like to remove? ")
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"File {filename}, has been removes!")
        except PermissionError:
            print(f"Permission denied: unable to delete {filename}.")
        except Exception as e:
            print(f"An error has occured, {e}")