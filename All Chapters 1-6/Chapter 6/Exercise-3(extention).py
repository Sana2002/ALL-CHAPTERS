# - Allow the user to keep entering values until they enter Q to quit.
# - Handle incorrect input

import operator
import math

def add(x, y):
    return operator.add(x, y)

def subtract(x, y):
    return operator.sub(x, y)

def multiply(x, y):
    return operator.mul(x, y)

def divide(x, y):
    if y != 0:
        return operator.truediv(x, y)
    else:
        return "Cannot divide by zero."

def modulus(x, y):
    if y != 0:
        return operator.mod(x, y)
    else:
        return "Cannot calculate modulus with zero divisor."

def check_greater(x, y):
    return operator.gt(x, y)

def display_menu():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("Enter 'Q' to quit")

def get_user_choice():
    while True:
        user_input = input("Enter your choice (1-6 or Q to quit): ").upper()
        if user_input == 'Q':
            return user_input
        try:
            choice = int(user_input)
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'Q' to quit.")

def get_user_inputs():
    while True:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            return x, y
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    while True:
        display_menu()
        user_choice = get_user_choice()

        if user_choice == 'Q':
            break

        user_inputs = get_user_inputs()

        result = (user_choice, *user_inputs)

        if isinstance(result, bool):
            print(f"The result is: {result}")
        else:
            print(f"The result of the operation is: {result}")
