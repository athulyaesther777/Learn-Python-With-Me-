height = 1.90  # Height in meters
weight = 90    # Weight in kilograms

# Calculate BMI (Body Mass Index)
bmi = weight / height ** 2

# Print the calculated BMI
print(bmi)  # Output: 24.930747922437675 (Exact BMI value)

# Convert BMI to an integer
print(int(bmi))  # Output: 24 (BMI rounded down to the nearest integer)

# Round the BMI to the nearest integer
print(round(bmi))  # Output: 25 (BMI rounded to the nearest whole number)

# Round the BMI to 7 decimal places
print(round(bmi, 7))  # Output: 24.9307479 (BMI rounded to 7 decimal places)
