                  #Basic Game Building


# The word to guess
the_word = "Football"
# Variable to store the user's guess
guess = ""

# Loop until the user guesses the correct word
while guess != the_word:
    guess = input("Enter the word:")

print("Congratulations! You won.")


"""

output : eg

Enter the word:run
Enter the word:love
Enter the word:football
Enter the word:Football
Congragulations !  You won .

"""


# The word to guess
the_word = "Football"
# Variable to store the user's guess
guess = ""
# Counter for the number of guesses
guess_count = 0
# Limit on the number of guesses
guess_limit = 5
# Flag to check if the user is out of guesses
out_of_guesses = False

# Loop until the user guesses the correct word or runs out of guesses
while guess != the_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter the word:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry, you lost.")
else:
    print("Congratulations! You won.")


"""
output : eg 1
Enter the word:hd
Enter the word:sj
Enter the word:Football
Congragulations !  You won .


output : eg 2
Enter the word:time
Enter the word:love
Enter the word:fun
Enter the word:Top
Enter the word:food
Sorry you lost.

"""