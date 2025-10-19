# A simple countdown based off given time by user
import time

print("This will be a simple timer")
print("Do you want a custom 'countdown over' message? [y/n]")
answer = (input())
if answer.lower() == 'y':
    customMsg = input("Enter the message: ")
elif answer.lower() == 'n':
    customMsg = "Countdown over."

length = int(input("Please enter the length of the countdown: "))

while length > 0:
    print(length) # pretty self explanatory
    time.sleep(1) # this waits 1 second
    length -= 1 # removes 1 from the display
print(customMsg)