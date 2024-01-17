# Write a Python program to print the asterisk pattern shown below ( hint : Use print statements)
# ```
#      *
#     ***
#    *****
#   *******
#  *********     
# ```

# Function to print a pattern
def print_pattern(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Ask the user to enter the number of rows for the pattern
try:
    rows = int(input("Enter the number of rows for the pattern: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Print the pattern
print_pattern(rows)
