# Write code to prompt the user to input her/his name and age and print these details on the screen. Find the length of the name and also the age of the user after one year.
# The format of text should look like the sample output below.
# (Use title() function)
# ```
# Hello, user!
# What is your name?
# alpha s
# What is your age?
# 22
# It is good to meet you, Alpha S
# The length of your name is:
# 5
# You will be 23 in a year

# Prompt user for name
name = input("Hello, user!\nWhat is your name?\n").title()

# Prompt user for age
age = int(input("What is your age?\n"))

# Print personalized greeting
print(f"It is good to meet you, {name}")

# Calculate and print the length of the name
name_length = len(name)
print(f"The length of your name is:\n{name_length}")

# Calculate and print the age after one year
age_after_one_year = age + 1
print(f"You will be {age_after_one_year} in a year")
