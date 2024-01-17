# The program should display the following calculator menu:
# ```
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Modulus
# ```
# The program will prompt the user to choose the operation choice (from 1 to 5). Then it asks the user to input values for the calculation. The program outputs the results of the calculation. The program should end by asking if the user would like to perform another calculation or not.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot find modulus with zero divisor"

while True:
    # Display the calculator menu
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    # Prompt user for the operation choice
    choice = input("Enter your choice (1 to 5): ")

    # Validate the user input
    if not choice.isdigit() or not (1 <= int(choice) <= 5):
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue

    # Prompt user for input values
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the chosen operation
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = modulus(num1, num2)

    # Display the result
    print(f"Result: {result}")

    # Ask if the user wants to perform another calculation
    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        print("Exiting the calculator. Goodbye!")
        break
