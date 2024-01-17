# Write a program that implements a while loop. This program should ask the user if they would like to continue and use the while loop to keep looping as long as they enter the letter Y. Once the while loop has terminated output the number of times it is executed.

# Initialize a counter
count = 0

# Start the while loop
while True:
    user_input = input("Do you want to continue? (Y/N): ").upper()

    # Check if the user wants to continue
    if user_input == 'Y':
        count += 1
    elif user_input == 'N':
        break  # Exit the loop if the user enters 'N'
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

# Output the number of times the loop has executed
print(f"The loop was executed {count} times.")
