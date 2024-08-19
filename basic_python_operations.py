# Accessing elements from a string using negative and positive indexing
print("Hello"[-4])  # Output: e (Negative indexing: -4 gives the second character from the start)
print("Hello"[1])   # Output: e (Positive indexing: 1 gives the second character)
print("Hello"[3])   # Output: l (Positive indexing: 3 gives the fourth character)

# Basic arithmetic operations
print(123 + 345)  # Output: 468 (Addition of two integers)

# String concatenation
print("123" + "453")  # Output: 123453 (Concatenation of two strings)

# Large numbers can be written with underscores in Python for readability
print(873_062_382)  # Output: 873062382 (Underscores are ignored in numeric literals)

# Floating point addition
print(2904.4 + 589.6)  # Output: 3494.0 (Addition of two floating-point numbers)

# Boolean value output
print(True)  # Output: True (Prints the Boolean value True)

# Checking the length of a string
print(len("Esther"))  # Output: 6 (Length of the string "Esther")

# Print the 'len' function itself
print(len)  # Output: <built-in function len> (Prints the built-in len function)

# Checking the length of another string
print(len("esther"))  # Output: 6 (Length of the string "esther")

# Demonstrating type checking in Python
print(type("hello"))  # Output: <class 'str'> (Type of "hello" is a string)
print(type(123))      # Output: <class 'int'> (Type of 123 is an integer)
print(type(True))     # Output: <class 'bool'> (Type of True is a Boolean)
print(type(44.7))     # Output: <class 'float'> (Type of 44.7 is a floating-point number)

# Type conversion from string to integer
int("123")  # Converts the string "123" to an integer 123
print(int("123") + int("111"))  # Output: 234 (Addition after converting strings to integers)

# Example of input and error handling
user = input("Enter your place:")  # Takes user input
length = len(user)  # Calculates the length of the input string
print("Number of the letters in your name :")  # Output: Number of the letters in your name :
print(type(length))  # Output: <class 'int'> (Type of 'length' is an integer)
print(type(user))    # Output: <class 'str'> (Type of 'user' is a string)
print("Number of the letters in your name :" + str(length))  # Output: Number of the letters in your name :<length>

# BMI calculation
height = 177  # Height in centimeters
weight = 90   # Weight in kilograms
bmi = weight / (height / 100) ** 2  # Corrected BMI calculation with height in meters
print(bmi)  # Output: 28.73 (Calculated BMI value)
