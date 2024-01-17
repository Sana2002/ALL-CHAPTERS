# Write a program that passes a list as an argument to a function. The function should then calculate the product (values multiplied) of the list values and return this value back to the main program.

def calculate_product(lst):
    result = 1
    for value in lst:
        result *= value
    return result

# Function to demonstrate passing a list as an argument
def main():
    # Example list
    numbers = [2, 3, 4, 5]

    # Call the function with the list as an argument
    product_result = calculate_product(numbers)

    # Display the result
    print(f"The product of the list values is: {product_result}")

# Call the main function
if __name__ == "__main__":
    main()
