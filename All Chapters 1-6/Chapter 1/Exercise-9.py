# Create an integer list and perform following operations
# - Create an int list with 10 values
# - Output the list using a for loop
# - Output the highest and lowest value
# - Sort the elements in ascending order
# - Sort the elements in descending order
# - Append two elements 
# - Print the list after appending

# Create an int list with 10 values
integer_list = [23, 56, 12, 87, 45, 34, 67, 9, 21, 78]

# Output the list using a for loop
print("Original List:")
for num in integer_list:
    print(num, end=" ")

# Output the highest and lowest value
highest_value = max(integer_list)
lowest_value = min(integer_list)
print(f"\nHighest Value: {highest_value}")
print(f"Lowest Value: {lowest_value}")

# Sort the elements in ascending order
integer_list.sort()
print("Sorted List (Ascending):", integer_list)

# Sort the elements in descending order
integer_list.sort(reverse=True)
print("Sorted List (Descending):", integer_list)

# Append two elements
integer_list.append(99)
integer_list.append(11)

# Print the list after appending
print("List after Appending:", integer_list)
