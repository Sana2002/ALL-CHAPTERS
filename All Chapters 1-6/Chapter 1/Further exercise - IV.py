# Write Python Program to Count the Number of Times an Item Appears in the List

# ```staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]```

# (Hint: For each item in the list consider it as a key, and the number of times these items appear will be its associated value)

# Given list
staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary", "Anmol", "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

# Initialize an empty dictionary to store the counts
item_counts = {}

# Count the occurrences of each item in the list
for item in staff:
    if item in item_counts:
        item_counts[item] += 1
    else:
        item_counts[item] = 1

# Display the counts
print("Item Counts:")
for item, count in item_counts.items():
    print(f"{item}: {count}")
