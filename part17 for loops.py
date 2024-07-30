
                  # For Loop


# It iterates over a sequence and executes a block of code for each item

# Loop through each character in a string
for words in "FUN TIME":
    print(words)

"""
output:
F
U
N

T
I
M
E
"""

# Loop through each item in a list
mates = ["Esther", "Elizer", "Abel", "Charlie"]
for mate in mates:
    print(mate)

"""
output:
Esther
Elizer
Abel
Charlie
"""

# Loop through a range of numbers
for number in range(12):
    print(number)

"""
output:
0
1
2
3
4
5
6
7
8
9
10
11
"""

# Loop through a specific range of numbers
for number in range(7, 12):
    print(number)

"""
output:
7
8
9
10
11
"""

# Loop with conditional statements
for index in range(5):
    if index == 0:
        print("First Number")
    else:
        print("Next Number")

"""
output:
First Number
Next Number
Next Number
Next Number
Next Number
"""
