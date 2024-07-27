#Strings



print("Football Club")               # Output: Football Club
print("Football\" Club")             # Output: Football" Club
print("Football \n Club")            # Output:
                                     # Football
                                     #  Club
Word = "football"

print(Word + " is my passion")       # Output: football is my passion
print(Word.lower())                  # Output: football
print(Word.upper())                  # Output: FOOTBALL
print(Word.isupper())                # Output: False
print(Word.islower())                # Output: True
print(Word.upper().isupper())        # Output: True
print(Word.upper().islower())        # Output: False
print(len(Word))                     # Output: 8
print(Word[0])                       # Output: f  # the index start with 0
print(Word[7])                       # Output: l
print(Word.index("a"))               # Output: 5
print(Word[-1])                      # Output: l
print(Word.replace("ball", "wear"))  # Output: footwear
print(Word.replace("foot", "My new ")) # Output: My new ball
