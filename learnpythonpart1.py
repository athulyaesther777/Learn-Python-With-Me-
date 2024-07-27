#Here we know the how we make use of python

print("Hello World")
#Here we can Arithematics and Boolean
name = "Alice"
age = "25"
Height = 5.6
is_student = True
print("name",name)
print("Age",age)
a = 3
b =4
print("sum",a+b)
count = 0
while count < 5:
      print("Count:". count)
      count += 1

#Its how the function works
def greet(name):
      return f"Hello ,{name}!"

#This is how list works

print(greet("Alice"))
fruits = ["apple","banana", "cherry"]
print("First fruit:",fruits[0])
fruits.append("orange")
print("Fruits after adding orange:" , fruits)
fruits.remove("banana")
print("Fruits after removing banana:", fruits)

#Here is how we can use the for loop

for fruits in fruits:
        print("Fruits:", fruits)
for i in range(5):
        print("iteration:", i)

 #making use of data types

character_name = "obedh"
character_age = 5
Is_male = True

print("His name is " +character_name+",")
print("and he is " + str(character_age) +" years old,")

if Is_male:
    print("He is a boy.")
else:
    print("She is a girl.")


character_name = "Luke"
character_age = "2"

print("" +character_name+" loves to play football,")
print("But now he is only "+character_age+" years old to play in any professional level.")

