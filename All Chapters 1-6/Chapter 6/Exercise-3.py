# Write a program that will display the following calculator menu 
# ```
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Modulus
# 6. Check greater number
# ```
# The program will prompt the user to choose the operation choice (from 1 to 6). Then it asks the user to input values for the calculation. The program outputs the results of the calculation.Use operator module functions

import operator

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

def get_user_choice():
    try:
        choice = int(input("Enter your choice (1-6): "))
        if 1 <= choice <= 6:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            return get_user_choice()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_choice()

def get_user_inputs():
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        return x, y
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_user_inputs()

def perform_calculation(choice, x, y):
    if choice == 1:
        result = add(x, y)
    elif choice == 2:
        result = subtract(x, y)
    elif choice == 3:
        result = multiply(x, y)
    elif choice == 4:
        result = divide(x, y)
    elif choice == 5:
        result = modulus(x, y)
    elif choice == 6:
        result = check_greater(x, y)

    return result

if __name__ == "__main__":
    display_menu()
    user_choice = get_user_choice()
    user_inputs = get_user_inputs()

    result = perform_calculation(user_choice, *user_inputs)

    if isinstance(result, bool):
        print(f"The result is: {result}")
    else:
        print(f"The result of the operation is: {result}")
