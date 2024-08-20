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
        print("You need to pay $10")  # If the person is older than 18, they need to pay $10

    # Check if the person's age is less than 18 but greater than or equal to 14
    elif age_of_the_person < 18:
        print("You need to pay $5")  # If the person is younger than 18, they need to pay $5
else:
    # If the person is shorter than 150 cm, they can't enter
    print("Sorry! Not this time.")

# Another example to calculate BMI and provide feedback
weight = 52  # Weight in kilograms
height = 1.62  # Height in meters
bmi = weight / (height ** 2)  # Calculate BMI

# Check if the BMI is less than 18.5
if bmi < 18.5:
    print("You are underweight")  # If BMI is below 18.5, the person is underweight

# Check if the BMI is between 18.5 and 24.9
elif 18.5 <= bmi < 25:
    print("Your BMI is normal")  # If BMI is between 18.5 and 24.9, the person has normal weight

# Check if the BMI is 25 or higher
elif bmi >= 25:
    print("Sorry, you are overweight")  # If BMI is 25 or higher, the person is overweight
else:
    # This block will never be reached because all BMI values are covered above
    print("What?")
