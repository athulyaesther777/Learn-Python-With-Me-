                        # If statement

                        
"""
What is an if statement?

1) I go to my room 
If I am alone (condition)
I play with my PlayStation.

2) I hang around with my friends
If we are four,
We go to the nearby cafe.
Otherwise, if we are more than four,
We go to the ice cream parlour.

3) I go to McDonald's
If I am hungry,
I order Burger and Fries.
Otherwise, if I am a bit hungry,
I order Chicken nuggets.
Otherwise,
I order only fries.
"""

# Basic if statement
is_doctor = True
if is_doctor:
    print("You are a doctor")  # Output: You are a doctor

# No output since is_doctor is False
is_doctor = False
if is_doctor:
    print("You are a doctor")

# Print statement will execute since is_doctor is True
is_doctor = True
if is_doctor:
    print("You are an Engineer")  # Output: You are an Engineer

# if-else statement
is_doctor = True
if is_doctor:
    print("You are a doctor")
else:
    print("You are not a doctor")  # Output: You are a doctor

is_doctor = False
if is_doctor:
    print("You are a doctor")
else:
    print("You are not a doctor")  # Output: You are not a doctor

# if statement with 'or' condition
is_doctor = True
is_tall = True
if is_doctor or is_tall:
    print("You are a doctor or otherwise you are tall")
else:
    print("You are not a doctor nor tall")  # Output: You are a doctor or otherwise you are tall

is_doctor = False
is_tall = True
if is_doctor or is_tall:
    print("You are a doctor or otherwise you are tall")
else:
    print("You are not a doctor nor tall")  # Output: You are a doctor or otherwise you are tall

is_doctor = False
is_tall = False
if is_doctor or is_tall:
    print("You are a doctor or otherwise you are tall")
else:
    print("You are not a doctor nor tall")  # Output: You are not a doctor nor tall

# if statement with 'and' condition
is_doctor = True
is_tall = True
if is_doctor and is_tall:
    print("You are a tall doctor")
else:
    print("You are not a doctor nor tall or both")  # Output: You are a tall doctor

is_doctor = True
is_tall = False
if is_doctor and is_tall:
    print("You are a tall doctor")
else:
    print("You are not a doctor nor tall or both")  # Output: You are not a doctor nor tall or both

# if-elif-else statement
is_doctor = True
is_tall = True
if is_doctor and is_tall:
    print("You are a tall doctor")
elif is_doctor and not(is_tall):
    print("You are a short doctor")
else:
    print("You are not a doctor nor tall or both")  # Output: You are a tall doctor

is_doctor = False
is_tall = True
if is_doctor and is_tall:
    print("You are a tall doctor")
elif is_doctor and not(is_tall):
    print("You are a short doctor")
else:
    print("You are not a doctor nor tall or both")  # Output: You are not a doctor nor tall or both

is_doctor = True
is_tall = False
if is_doctor and is_tall:
    print("You are a tall doctor")
elif is_doctor and not(is_tall):
    print("You are a short doctor")
else:
    print("You are not a doctor nor tall or both")  # Output: You are a short doctor

is_doctor = True
is_tall = True
if is_doctor and is_tall:
    print("You are a tall doctor")
elif is_doctor and not(is_tall):
    print("You are a short doctor")
elif not(is_doctor) and is_tall:
    print("You are tall")
else:
    print("You are not a doctor nor tall")  # Output: You are a tall doctor

is_doctor = True
is_tall = False
if is_doctor and is_tall:
    print("You are a tall doctor")
elif is_doctor and not(is_tall):
    print("You are a short doctor")
elif not(is_doctor) and is_tall:
    print("You are tall")
else:
    print("You are not a doctor nor tall")  # Output: You are a short doctor

is_doctor = False
is_tall = True
if is_doctor and is_tall:
    print("You are a tall doctor")
elif is_doctor and not(is_tall):
    print("You are a short doctor")
elif not(is_doctor) and is_tall:
    print("You are tall")
else:
    print("You are not a doctor nor tall")  # Output: You are tall

is_doctor = False
is_tall = False
if is_doctor and is_tall:
    print("You are a tall doctor")
elif is_doctor and not(is_tall):
    print("You are a short doctor")
elif not(is_doctor) and is_tall:
    print("You are tall")
else:
    print("You are not a doctor nor tall")  # Output: You are not a doctor nor tall

# Examples of conditional statements from the description

# Example 1: Playing with PlayStation if alone
is_alone = True
if is_alone:
    print("I go to my room and play with my PlayStation")  # Output: I go to my room and play with my PlayStation
else:
    print("I won't play with my PlayStation")

is_alone = False
if is_alone:
    print("I go to my room and play with my PlayStation")
else:
    print("I won't play with my PlayStation")  # Output: I won't play with my PlayStation

# Example 2: Hanging around with friends
is_four = True
is_more_than_four = True
if is_four:
    print("We go to the nearby cafe.")  # Output: We go to the nearby cafe.
elif is_more_than_four:
    print("We go to the ice cream parlour")
else:
    print("Go to my room.")

# Example 3: Ordering food at McDonald's
is_hungry = True
is_bithungry = True
if is_hungry:
    print("I will order burger and fries")  # Output: I will order burger and fries
elif is_bithungry:
    print("I order Chicken nuggets")
else:
    print("I order only fries")

is_hungry = False
is_bithungry = True
if is_hungry:
    print("I will order burger and fries")
elif is_bithungry:
    print("I order Chicken nuggets")  # Output: I order Chicken nuggets
else:
    print("I order only fries")

is_hungry = True
is_bithungry = False
if is_hungry:
    print("I will order burger and fries")  # Output: I will order burger and fries
elif is_bithungry:
    print("I order Chicken nuggets")
else:
    print("I order only fries")

is_hungry = False
is_bithungry = False
if is_hungry:
    print("I will order burger and fries")
elif is_bithungry:
    print("I order Chicken nuggets")
else:
    print("I order only fries")  # Output: I order only fries
