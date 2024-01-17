try:
    # Get the file name or path from the user
    file_name = input("Enter the file name or path: ")

    # Read data from the file and convert valid lines to a list of integers
    numbers = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            try:
                number = int(line)
                numbers.append(number)
            except ValueError:
                print(f"Skipping non-integer value: {line}")

    # Output the valid values in integer format
    for number in numbers:
        print(number)

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#Make a sentences.txt