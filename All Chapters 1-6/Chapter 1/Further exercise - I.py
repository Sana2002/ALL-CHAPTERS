# Write a program that calculates the number of seconds in a day.
# Hint: Ask user to enter number of days, Convert days into hours, hours to minutes, minutes to seconds

# Function to calculate seconds in a given number of days
def calculate_seconds_in_days(days):
    # Constants for conversions
    hours_in_a_day = 24
    minutes_in_an_hour = 60
    seconds_in_a_minute = 60

    # Calculate seconds
    seconds = days * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute

    return seconds

# Ask user to enter the number of days
try:
    days = float(input("Enter the number of days: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Calculate and display the result
seconds_in_days = calculate_seconds_in_days(days)
print(f"\nThere are {seconds_in_days} seconds in {days} days.")
