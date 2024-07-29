# Return Statement

# Function without a return statement
def square(number):
    number * number  # This line calculates the square but does not return it

print(square(5))     # Output: None

"""
Explanation:
The `square` function calculates the square of the number but does not return any value.
In Python, if a function does not explicitly return a value, it returns `None` by default.
"""

# Function with a return statement
def square(number):
    return number * number  # This line returns the square of the number

print(square(5))     # Output: 25

"""
Explanation:
The `square` function calculates the square of the number and returns it.
The `return` statement sends the result back to the caller, and `print` displays it.
"""

# Function to calculate the cube of a number
def cube(number):
    return number * number * number  # This line returns the cube of the number

print(cube(5))      # Output: 125

"""
Explanation:
The `cube` function calculates the cube of the number and returns it.
The `return` statement allows the result to be used elsewhere, and `print` displays it.
"""

# Function with calculation but without a return statement, and an extra print statement
def cube(number):
    number * number * number  # This line calculates the cube but does not return it
    print("Hello Guys")       # This line prints "Hello Guys" but does not affect the return value

print(cube(5))      # Output: Hello Guys
                   # Output: None

"""
Explanation:
The `cube` function calculates the cube of the number but does not return it.
It prints "Hello Guys" but the function itself returns `None` by default.
"""

# Function with a return statement and unreachable code
def cube(number):
    return number * number * number  # This line returns the cube of the number
    print("Hello Guys")              # This line is never executed

print(cube(5))      # Output: 125

"""
Explanation:
The `cube` function calculates the cube of the number and returns it.
The `return` statement exits the function, so any code after it (e.g., the print statement) is not executed.
"""
