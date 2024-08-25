import random  # Import the random module for generating random choices

print("Welcome to our PASSWORD GENERATOR ..........!")

# List of uppercase and lowercase letters
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# List of digits
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# List of special characters
spcl_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
              '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
              '_', '`', '{', '|', '}', '~']

# Prompt the user to input the desired number of letters, numbers, and special characters
letter = int(input("How many letters do you want?\n"))
number = int(input("How many numbers do you want?\n"))
spcl_char = int(input("How many special characters do you want?\n"))

# Initialize an empty string for the password
password = ""

# Add the specified number of random letters to the password
for length in range(1, letter + 1):  # Loop for the number of letters
    random_letter = random.choice(letters)  # Choose a random letter from the list
    password += random_letter  # Add the random letter to the password

# Add the specified number of random numbers to the password
for length in range(1, number + 1):  # Loop for the number of numbers
    random_number = random.choice(numbers)  # Choose a random number from the list
    password += random_number  # Add the random number to the password

# Add the specified number of random special characters to the password
for length in range(1, spcl_char + 1):  # Loop for the number of special characters
    random_symbol = random.choice(spcl_chars)  # Choose a random special character from the list
    password += random_symbol  # Add the random special character to the password

# Print the final generated password
print(password)
