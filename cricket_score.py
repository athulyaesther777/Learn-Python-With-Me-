runs = 0  # Initialize runs to 0
over = 1.0  # Initialize over to 1.0 (floating-point number)
is_winning = True  # Boolean value indicating if the player/team is winning

# Update runs by adding 5
runs += 5

# Print the updated runs
print(runs)  # Output: 5 (after adding 5 to initial 0)

# Print the type of the runs variable
print(type(runs))  # Output: <class 'int'> (runs is of integer type)

# Print a string with the runs value using type conversion
print("Your runs are " + str(runs))  # Output: Your runs are 5

# Using an f-string to embed variables into a string
print(f"In {over} over(s), you took {runs} run(s) and your winning status is {is_winning}.")
# Output: In 1.0 over(s), you took 5 run(s) and your winning status is True.
