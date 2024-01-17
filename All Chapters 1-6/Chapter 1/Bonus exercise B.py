# ```locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']```

# - Print the list and find the length of the list
# - Use sorted() to print your list in alphabetical order without modifying the actual list.
# - Show that your list is still in its original order by printing it.
# - Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
# - Show that your list is still in its original order by printing it again.
# - Use reverse() to change the order of your list.
# - Print the list to show that its order has changed.
# - Use sort() to change your list so it’s stored in alphabetical order.
# - Print the list to show that its order has been changed.
# - Use sort() to change your list so it’s stored in reverse alphabetical order.
# - Print the list to show that its order has changed.

# Original list
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

# Print the list and find the length
print("Original List:", locations)
print("Length of the List:", len(locations))

# Use sorted() to print the list in alphabetical order without modifying the actual list
sorted_list = sorted(locations)
print("Sorted List (Alphabetical):", sorted_list)

# Print the original list to show it's still in its original order
print("Original List (After Sorted):", locations)

# Use sorted() to print the list in reverse alphabetical order without changing the original order
reverse_sorted_list = sorted(locations, reverse=True)
print("Sorted List (Reverse Alphabetical):", reverse_sorted_list)

# Print the original list to show it's still in its original order
print("Original List (After Reverse Sorted):", locations)

# Use reverse() to change the order of the list
locations.reverse()
print("Reversed List:", locations)

# Use sort() to change the list to alphabetical order
locations.sort()
print("Sorted List (Alphabetical):", locations)

# Use sort() to change the list to reverse alphabetical order
locations.sort(reverse=True)
print("Sorted List (Reverse Alphabetical):", locations)
