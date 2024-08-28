# Initialize the first list with some elements
list1 = [1, 2, 2, 5]

# Initialize the second list with some elements
list2 = [1, 2, 3, 2, 6]

# Combine list1 and list2 into a single list
list3 = list1 + list2

# Print the combined list with duplicates
print(list3)  # Output: [1, 2, 2, 5, 1, 2, 3, 2, 6]

# Initialize an empty list to store unique elements
unique_list = []

# Iterate over each item in the combined list
for item in list3:
    # Check if the item is not already in the unique_list
    if item not in unique_list:
        # If not, append it to unique_list
        unique_list.append(item)

# Print the list with unique elements only
print(unique_list)  # Output: [1, 2, 5, 3, 6]
