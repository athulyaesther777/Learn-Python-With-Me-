import random  # Import the random module to use random functions

# Initialize an empty list to store the password components
password_list = []

# Loop to add the specified number of random letters to the password list
for length in range(1, letter + 1):  
    random_letter = random.choice(letters)  # Select a random letter from the list of letters
    password_list.append(random_letter)  # Append the random letter to the password list

# Loop to add the specified number of random numbers to the password list
for length in range(1, number + 1):  
    random_number = random.choice(numbers)  # Select a random number from the list of numbers
    password_list.append(random_number)  # Append the random number to the password list

# Loop to add the specified number of random special characters to the password list
for length in range(1, spcl_char + 1):  
    random_symbol = random.choice(spcl_chars)  # Select a random special character from the list
    password_list.append(random_symbol)  # Append the random special character to the password list

# Print the password list before shuffling
print(password_list)  # This shows the order of letters, numbers, and special characters before shuffling

# Shuffle the password list to randomize the order of characters
random.shuffle(password_list)

# Print the password list after shuffling
print(password_list)  # This shows the order of characters after shuffling

# Initialize an empty string to store the final password
password = ""

# Loop through the shuffled password list and concatenate each character to the password string
for length in password_list:
    password += length  # Add each character to the password string

# Print the final generated password
print(password)  # This prints the final, randomized password
