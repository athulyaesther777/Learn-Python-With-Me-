# Modulo operator
print(5 % 3)  # Outputs the remainder when 5 is divided by 3 (Result: 2)
print(5 // 3)  # Outputs the integer division of 5 by 3 (Result: 1)

# Let's go through some more examples
print(8 // 7)  # Outputs the integer division of 8 by 7 (Result: 1)
print(8 % 7)   # Outputs the remainder when 8 is divided by 7 (Result: 1)
print(24 % 3)  # Outputs the remainder when 24 is divided by 3 (Result: 0)
print(24 // 3)  # Outputs the integer division of 24 by 3 (Result: 8)

# Let's check it with a problem
# Prompt the user to enter a number to check if it's even or odd
num = int(input("Enter a number to check whether it is even or odd:\n"))

# Use the modulo operator to determine if the number is even or odd
if num % 2 == 0:
    print(f"The number  {num} is even.")
else:
    print(f"The number {num} is odd.")

# Another way to check the modulo of the number (i.e., the remainder)
print(f"The modulo of {num} divided by 2 is ", num % 2)

# Such a way it continues...
