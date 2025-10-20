# This'll be a basic calculator with (+, -, *, /)
print("Welcome to the calculator!")

num1 = float(input("Please enter the first number..."))

num2 = float(input("Please enter the second number..."))

op = input("Please enter the operator...")
if (op == '+'):
    print(num1 + num2)
elif (op == '-'):
    print(num1 - num2)
elif (op == '*'):
    print(num1 * num2)
elif (op == '/'):
    # If zero
    if (num2 == 0):
        print("Cant divide by 0, please choose a different number.")
    else:
        print(num1 / num2)
# Check if non of the valid operators were chosen
else:
    print("Not a valid operator, please try again.")