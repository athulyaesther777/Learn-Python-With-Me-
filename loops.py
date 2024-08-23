# List of colors
Colors = ["red", "yellow", "orange", "blue"]

# Loop through each color in the Colors list
for color in Colors:
    print(color)  # Print the current color
    print(color + " fruit")  # Print color followed by "fruit"
    print(Colors)  # Print the entire Colors list

# Print the Colors list after the loop ends
print(Colors)

# List of numbers
numbers = [23, 33, 44, 56, 12, 34, 45, 67]

# Calculate the sum of numbers using sum() function
num = sum(numbers)
print(num)

# Manually calculate the sum using a loop
sum = 0
for number in numbers:
    sum += number
print(sum)

# Print the maximum and minimum values in the numbers list
print(max(numbers))
print(min(numbers))

# Find the maximum number manually
max_num = 0
for number in numbers:
    if number > max_num:
        max_num = number

# Print the maximum number found
print(max_num)
