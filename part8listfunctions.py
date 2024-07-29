                     # List Functions

Number = [1, 6, 7, 9, 2]
Countries = ["Germany", "Italy", "Ireland", "London", "Australia"]
print(Countries)  # Output: ['Germany', 'Italy', 'Ireland', 'London', 'Australia']

Countries.extend(Number)
# Extends the list by adding elements from another list
print(Countries)  # Output: ['Germany', 'Italy', 'Ireland', 'London', 'Australia', 1, 6, 7, 9, 2]

Countries.append("South Africa")
# Appends an element to the end of the list
print(Countries)  # Output: ['Germany', 'Italy', 'Ireland', 'London', 'Australia', 1, 6, 7, 9, 2, 'South Africa']

Countries.insert(7, "Sharja")
# Inserts an element at the specified position
print(
    Countries)  # Output: ['Germany', 'Italy', 'Ireland', 'London', 'Australia', 1, 6, 'Sharja', 7, 9, 2, 'South Africa']

Countries.remove("Italy")
# Removes the first occurrence of a value
print(Countries)  # Output: ['Germany', 'Ireland', 'London', 'Australia', 1, 6, 'Sharja', 7, 9, 2, 'South Africa']

Countries.clear()
# Clears all elements from the list
print(Countries)  # Output: []

# To remove only the last data we can use pop
Countries = ["Germany", "Italy", "Ireland", "London", "Australia"]
Countries.pop()
print(Countries)  # Output: ['Germany', 'Italy', 'Ireland', 'London']

# To know the index number of any value of the list
print(Countries.index("Ireland"))  # Output: 2

Countries = ["Germany", "Italy", "Ireland", "London", "Germany", "Italy", "Ireland", "London", "Germany", "Italy",
             "Ireland", "London", "Germany", "Italy", "Ireland", "London", "Germany", "Italy", "Ireland", "London",
             "Germany", "Italy", "Ireland", "London", "Australia"]
# To know how many times a particular word repeats in the list
print(Countries.count("Germany"))  # Output: 6

# To make another list which contains the same inputs
Countries2 = Countries.copy()
print(
    Countries2)  # Output: ['Germany', 'Italy', 'Ireland', 'London', 'Germany', 'Italy', 'Ireland', 'London', 'Germany', 'Italy', 'Ireland', 'London', 'Germany', 'Italy', 'Ireland', 'London', 'Germany', 'Italy', 'Ireland', 'London', 'Germany', 'Italy', 'Ireland', 'London', 'Australia']

# Sorting of numbers
Number.sort()
# Sorts the list in ascending order
print(Number)  # Output: [1, 2, 6, 7, 9]

Countries.sort()
# Sorts the list in ascending order
print(
    Countries)  # Output: ['Australia', 'Germany', 'Germany', 'Germany', 'Germany', 'Germany', 'Ireland', 'Ireland', 'Ireland', 'Ireland', 'Ireland', 'Italy', 'Italy', 'Italy', 'Italy', 'Italy', 'London', 'London', 'London', 'London', 'London']

# If we want the list in descending order
Number.reverse()
# Reverses the elements of the list
print(Number)  # Output: [9, 7, 6, 2, 1]

Countries.reverse()
# Reverses the elements of the list
print(
    Countries)  # Output: ['London', 'London', 'London', 'London', 'London', 'Italy', 'Italy', 'Italy', 'Italy', 'Italy', 'Ireland', 'Ireland', 'Ireland', 'Ireland', 'Ireland', 'Germany', 'Germany', 'Germany', 'Germany', 'Germany', 'Australia']
