# Q.51  How Many Basic Types Of Functions Are Available In Python? 

'''
There are three types of functions in Python:

Built-in functions:
These are functions that are pre-defined in the Python interpreter. Some examples of built-in functions are print(), len(), and abs().

User-defined functions:
These are functions that are defined by the user. User-defined functions can take any number of arguments and can return any type of value.

Lambda functions:
Lambda functions are a type of anonymous function. They are smaller and simpler than user-defined functions and are often used for one-off tasks.

'''
###############################################################################################################################################

# Q.52 How can you pick a random item from a list or tuple?

# import random
# items = ('vishal', "brijesh", "smit", "Sharma" )
# i = random.choice(items)
# print(i)

###############################################################################################################################################

# Q.53 How can you pick a random item from a range.

# import random
# y=random.randrange(1,10)
# print(y)

#############################################################################################################################################

# Q.54  How will you set the starting value in generating random numbers?

# import random

# here we will use randrange functions to generating start value in random numbers 

# y= random.randrange(1,10)
# print(y)

#############################################################################################################################################

# Q.55 How will you randomizes the items of a list in place?

# here we can randomizes the items via convert list into set. and set returns list with unorder data.

############################################################################################################################################

# Q.56  Write a Python program to read a random line from a file. 

# import random
# lines = open('file.txt').read().splitlines()
# random_line =random.choice(lines)
# print(random_line)

############################################################################################################################################

# Q.57  Write a Python program to convert degree to radian.

# import math

# degrees = (input('Enter Degree Number: '))
# radians = degrees * (math.pi / degrees)
# print("Radians:", radians)

###########################################################################################################################################

# Q.58  Write a Python program to calculate the area of a trapezoid.

# a = float(input("Enter value for a branch: "))
# b = float(input("Enter value for b branch: "))
# h= float(input("Enter value for height: "))

# A=(1/2)*(a+b)*h

# print(A)

##########################################################################################################################################################

# Q. 59 Write a Python program to calculate the area of a parallelogram.

# b = float(input("Enter value for base: "))
# h= float(input("Enter value for height: "))

# A = b*h

# print(A)

##########################################################################################################################################################
#Q. 60  Write a Python program to calculate surface area and volume and area of a cylinder.
# import math


# radius = float (input("enter the radius of cylinder "))
# height = float (input("enter the height of cylinder "))

# surface_area = 2 * math.pi * radius * (radius + height)

# volume = math.pi * radius ** 2 * height

# print("The surface area of the cylinder is: ",surface_area)
# print("The volume of the cylinder is: ",volume)

