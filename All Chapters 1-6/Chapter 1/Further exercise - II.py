# Write Python Program to Find the Sum of Digits in a Number .For example if enters a number 1234 the result is 1+2+3+4 = 10

# Function to calculate the sum of digits in a number
def sum_of_digits(number):
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits

# Ask user to enter a number
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Calculate and display the result
result = sum_of_digits(num)
print(f"The sum of digits in {num} is: {result}")
