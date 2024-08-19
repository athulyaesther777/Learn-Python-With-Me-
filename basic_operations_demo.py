# String Indexing
print("Hello"[-4])  # Output: e (Negative indexing to access the second character from the start)
print("Hello"[1])   # Output: e (Positive indexing to access the second character)
print("Hello"[3])   # Output: l (Positive indexing to access the fourth character)

# Arithmetic Operations
print(123 + 345)  # Output: 468 (Addition of two integers)

# String Concatenation
print("123" + "453")  # Output: 123453 (Concatenation of two strings)

# Large Numbers
print(873_062_382)  # Output: 873062382 (Underscores are used for better readability)

# Floating Point Addition
print(2904.4 + 589.6)  # Output: 3494.0 (Addition of two floating-point numbers)

# Boolean Value
print(True)  # Output: True (Boolean value output)

# Checking Length of a String
print(len("Esther"))  # The length of the string "Esther" is calculated but not printed
print(len)  # Output: <built-in function len> (Prints the len function itself)
print(len("esther"))  # Output: 6 (Length of the string "esther")

# Demonstrating Type Checking
print(type("hello"))  # Output: <class 'str'> (Type of "hello" is string)
print(type(123))      # Output: <class 'int'> (Type of 123 is integer)
print(type(True))     # Output: <class 'bool'> (Type of True is boolean)
print(type(44.7))     # Output: <class 'float'> (Type of 44.7 is floating-point number)

# Type Conversion
int("123")  # Converts the string "123" to an integer 123
print(int("123") + int("111"))  # Output: 234 (Addition of two integers converted from strings)

# Example of Error Handling in Comments
# print("Number of the letters in your name :" + len(int(input("Enter your place:"))))
# This line is commented out as it would cause an error due to attempting to add an integer to a string.

# User Input and Length Calculation
user = input("Enter your place:")  # User is prompted to input their place
length = len(user)  # Length of the input string is calculated
print("Number of the letters in your name :")  # Prompts the user for their name's length
print(type(length))  # Output: <class 'int'> (Type of length is integer)
print(type(user))    # Output: <class 'str'> (Type of user input is string)
print("Number of the letters in your name :" + str(length))  # Output: Number of the letters in your name:<length>
