# For the array a = [20,23,82,40,32,15,67,52] print the output of following
# - find the indices of even numbers
# - Sort the array
# - Slice elements from index 3 to the end of the array
# - Slice elements from index 0 to index 4
# - print [32 15 67] using negative slicing

# Given array
a = [20, 23, 82, 40, 32, 15, 67, 52]

# Find the indices of even numbers
even_indices = [i for i, num in enumerate(a) if num % 2 == 0]
print("Indices of even numbers:", even_indices)

# Sort the array
sorted_array = sorted(a)
print("Sorted array:", sorted_array)

# Slice elements from index 3 to the end of the array
slice_1 = a[3:]
print("Slice from index 3 to the end:", slice_1)

# Slice elements from index 0 to index 4
slice_2 = a[0:5]
print("Slice from index 0 to index 4:", slice_2)

# Print [32, 15, 67] using negative slicing
negative_slice = a[-5:-2]
print("Negative slicing to get [32, 15, 67]:", negative_slice)
