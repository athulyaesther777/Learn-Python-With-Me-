# Welcome message for the rides
print("Welcome to our Wondering Land of Rides")

# Asking the user for their height in centimeters
height_of_person = int(input("How tall are you in centimeters?\n"))

# Check if the person's height is 150 cm or taller
if height_of_person >= 150:
    # If the height condition is met, ask for the person's age
    age_of_the_person = int(input("How old are you?\n"))

    # Nested if-else structure based on age
    # Checking if the person's age is less than 14 or greater than 65
    if 14 > age_of_the_person or age_of_the_person > 65:
        print("No entry")  # If the person is too young or too old, they can't enter
    # Check if the person's age is greater than 18
    elif age_of_the_person > 18:
        person = int(input("Do you need a photo with the ticket? say 1 for yes / 2 for no "))
        ticket = 10
        ticket_and_photo = 15
        if person == 1:
            print(f"You need to pay ${ticket_and_photo} for ticket with  photo ")
        elif person == 2:
            print(f"pay ${ticket} for ticket ")
    # Check if the person's age is less than 18 but greater than or equal to 14
    elif age_of_the_person < 18:
        person = int(input("Do you need a photo with the ticket? say 1 for yes / 2 for no "))
        ticket = 5
        ticket_and_photo = 15
        if person == 1:
            print(f"You need to pay ${ticket_and_photo} for ticket with  photo ")
        elif person == 2:
            print(f"pay ${ticket} for ticket ")
else:
    # If the person is shorter than 150 cm, they can't enter
    print("Sorry! Not this time.")

# also we can do like

# Welcome message for the rides
print("Welcome to our Wondering Land of Rides")

# Asking the user for their height in centimeters
height_of_person = int(input("How tall are you in centimeters?\n"))

# Check if the person's height is 150 cm or taller
if height_of_person >= 150:
    # If the height condition is met, ask for the person's age
    age_of_the_person = int(input("How old are you?\n"))

    # Initialize the bill
    bill = 0

    # Nested if-else structure based on age
    # Checking if the person's age is less than 14 or greater than 65
    if 14 > age_of_the_person or age_of_the_person > 65:
        print("No entry")  # If the person is too young or too old, they can't enter

    # Check if the person's age is greater than 18
    elif age_of_the_person > 18:
        bill = 10

    # Check if the person's age is less than 18 but greater than or equal to 14
    else:
        bill = 5

    # Ask if the user wants a photo
    photo = input("Enter y for yes and n for no if you want a photo: ")
    if photo == "y":
        bill += 3

    # Display the final bill
    print(f"Your bill is ${bill}")

else:
    # If the person is shorter than 150 cm, they can't enter
    print("Sorry! Not this time.")


