print("\nHey what's up guys\n")
# Output: 
# Hey what's up guys

input("You know this is called an input function and you should say something to this sentence otherwise this section "
      "wont close .\nThis is a prompt for the user so what's on your mind now ?")
# This prompts the user to enter something. No specific output except the text prompt.

print(" Hello " + input("What is your name ") + "!")
# The prompt asks for the user's name, and then it prints "Hello <name>!".
# Output (example): 
# What is your name: John
# Hello John!

name = input("Enter your name :")
# Prompts the user to enter their name.

print(" Hey dear " + name)
# Output (example): 
# Hey dear John

print(name)
# Outputs the value of `name`.
# Output (example): 
# John

Ram = int(input("Enter Ram's number :"))
# Prompts the user to enter a number for `Ram`.

print(len(input("Enter Ram's number :")))
# Prompts the user to enter another number, but this time it calculates and prints the length of the input.
# Output (example): 
# Enter Ram's number: 12345
# 5

print(Ram)
# Outputs the value of `Ram`.
# Output (example): 
# 12345

print(len(name))
# Outputs the length of the `name` string.
# Output (example): 
# 4 (if name is "John")

Raj = input("What's your fav food")
# Prompts the user to enter their favorite food.

length = len(Raj)
# Stores the length of the `Raj` string in the `length` variable.

print(length)
# Outputs the length of the `Raj` string.
# Output (example): 
# 5 (if food is "Pizza")

animal_1 = "cat"
animal_2 = "dog"

# Swapping between two
temp = animal_1
animal_1 = animal_2
animal_2 = temp
# This swaps the values of `animal_1` and `animal_2`.
# After swapping, `animal_1` will be "dog" and `animal_2` will be "cat".
