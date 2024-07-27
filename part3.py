                          #Numbers

print(777) #output: 777
print(-77) #output: -7
print(2+5) #output: 7
 # as per this you can test , and it will return the right answer

print(3+6-2)   #output: 7
print(3*(6-4)) #output: 6
print(3*6-4)   #output: 14(bodmass rule )

the_num = "7"
print(the_num)      #output: 7
print(str(the_num)) #output: 7
print(str(the_num)+ " is my lucky number") #output: 7 is my lucky number

# print (the_num) + " is lucky" gives unsupported operand type(s) for +: 'NoneType
#know about how importand the brackets are
#while placing numbers in quotes the code take it as a str

the_num1 = -17
# print(abs(the_num)) TypeError: bad operand type for abs(): 'str'
# to resolve issues we avoid using quotes for numbers
#here we use abs that is absolute value of the number

print(abs(the_num1)) #output: 17

#here we use power that is 4 power of 5
print(pow(4,5))      #output: 1024


print(max(1,2,3,4,5,6,7)) #output: 7
print(min(1,2,3,4,5,6,7)) #output: 1
print(round(9.89))        #output: 10
print(round(8.50))        #outpt: 8

#before moving on while doing such operations we can use (math)
#we used the from math import otherwise we might get trouble with error
#to use external codes and advanced maths

from math import*
the_num2 = 4
#here it take out the lower number in case of any decimal number
print(floor(4.8)) #output: 4
print(floor(4.3)) #output: 4

#here we use (ceil) that take out the higher number in case of any decimal number
print(ceil(4.2))  #output: 5
print(ceil(4.8))  #output: 5

#square root of a number
print(sqrt(56))   #output: 7.483314773547883
print(sqrt(49))   #output: 7


                








