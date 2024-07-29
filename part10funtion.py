                     # Part 10: Functions

# Defining a basic function
# We use the 'def' keyword to define a function
def say_hello():
    print("Hello Dear User!")

# Here we don't have any outputs yet because we haven't called the function
# To see the output, you need to call the function
print("Up")                # Output: Up
say_hello()                # Output: Hello Dear User!
print("Down")              # Output: Down

# Defining a function with one parameter
# The function takes a parameter 'Name' and uses it in the print statement
def say_hello(Name):
    print("Hello Dear " + Name)

# Calling the function with different arguments
say_hello("Alice")         # Output: Hello Dear Alice
say_hello("Bob")           # Output: Hello Dear Bob
say_hello("Charlie")      # Output: Hello Dear Charlie

# Defining a function with multiple parameters
# The function takes two parameters: 'Name' and 'age'
def say_hello(Name, age):
    print("Hello Dear " + Name + " . Are you " + age + " ?")

# Calling the function with different arguments
say_hello("Alice", "25")   # Output: Hello Dear Alice . Are you 25 ?
say_hello("Bob", "30")     # Output: Hello Dear Bob . Are you 30 ?
say_hello("Charlie", "35") # Output: Hello Dear Charlie . Are you 35 ?

# Defining a function with type conversion
# The function takes two parameters: 'Name' and 'age'
# Here, we convert 'age' to a string to concatenate it with other strings
def say_hello(Name, age):
    print("Hello Dear " + Name + " . Are you " + str(age) + " ?")

# Calling the function with different arguments
say_hello("Alice", 25)     # Output: Hello Dear Alice . Are you 25 ?
say_hello("Bob", 30)       # Output: Hello Dear Bob . Are you 30 ?
say_hello("Charlie", 35)   # Output: Hello Dear Charlie . Are you 35 ?
