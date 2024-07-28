
                   # basiccalculator

#we use # for single comments  and """ this fore more than one comments


number1 = input("Enter your first number:")
number2 = input("Enter your second number:")
result1 =  number1 + number2
print(result1)

#output1
""""
eg:1 
Enter your first number:3
Enter your second number:5
35
here we got the wrong answer , so let us try different 
"""

number3 = input("Enter your third number:")
number4 = input("Enter your fourth number:")
result2 =  int(number3) + int(number4)
print(result2)

#output2
""""
eg:2 
Enter your third number:7
Enter your fourth number:7
14
now look here while we gave int , our calculation has done in the proper way.
"""

#output3
"""
eg:3
Enter your third number:4.5
Enter your fourth number:7
here we got an error 
Traceback (most recent call last):
    result2 =  int(number3) + int(number4)
               ^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '4.5'
beacuse here we use int (integer) that cant operate with decimal values
"""

number5 = input("Enter your fifth number:")
number6 = input("Enter your sixth number:")
result3 =  float(number5) + float(number6)
print(result3)

#output4
"""
eg:4
Enter your fifth number:4
Enter your sixth number:5
9.0
here we used the numbers float which can deal with both integers and decimal numbers .
"""

#output5
"""
eg:5
Enter your fifth number:3.5
Enter your sixth number:7.2
10.7
so here we see how float works with decimal number.
"""

#we can change the sign as we want we can use +,-.*,/ all this instead of the given symbol ,
#lets look a example

number7 = input("Enter your seventh number:")
number8 = input("Enter your eighth number:")
result4 =  float(number7) / float(number8)
print(result4)

#output
"""
eg:6
Enter your seventh number:70
Enter your eighth number:10
7.0
"""

#output
"""
eg:7
Enter your seventh number:30.7
Enter your eighth number:2.1
14.619047619047619
"""
#so now we see how it works , we can addd more input options and operations as per us



number9 = input("Enter your nineth number:")
number10 = input("Enter your tenth number:")
number11 = input("Enter your eleventh number:")
number12 = input("Enter your twelve number:")
number13 = input("Enter your thirteen number:")
number14 = input("Enter your fourteen number:")
result5 =  float(number9) + float(number10) - float(number11) * float(number13) / float(number14)
print(result5)


#output
"""
eg:8
Enter your nineth number:3
Enter your tenth number:5
Enter your eleventh number:2
Enter your twelve number:8
Enter your thirteen number:4
Enter your fourteen number:10.2
7.215686274509804
"""