# Advanced Calculator

# Get the first number from the user
num1 = float(input("Enter the first number:"))

# Get the operator from the user
operator = input("Enter the operator: ")

# Get the second number from the user
num2 = float(input("Enter the second number:"))

# Perform the calculation based on the operator
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

# Output examples

"""
Enter the first number:75
Enter the operator: 2
Enter the second number:9
Invalid operator
"""

"""
Enter the first number:56
Enter the operator: +
Enter the second number:21
77.0
"""

"""
Enter the first number:8
Enter the operator: /
Enter the second number:7
1.1428571428571428
"""

"""
Enter the first number:45
Enter the operator: *
Enter the second number:32
1440.0
"""
