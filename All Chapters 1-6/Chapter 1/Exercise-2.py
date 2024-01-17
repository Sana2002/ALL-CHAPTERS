# Write a program that evaluates the following calculations for two int numbers obtained from the user and outputs the results to the console:

# ```Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%)```

# Prompt user for two integer numbers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform calculations
sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2

# Check if the second number is zero before performing division
if num2 != 0:
    quotient_result = num1 / num2
    remainder_result = num1 % num2
else:
    quotient_result = "Undefined (division by zero)"
    remainder_result = "Undefined (division by zero)"

# Output results to the console
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
print(f"Remainder: {remainder_result}")
