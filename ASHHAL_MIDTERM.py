# ASHHAL AHMED
# MID_TERM EXAM


# Q1 - Write a Python program to do arithmetical operations addition and division.

FIRST_NUMBER=int(input("ENTER FIRST_NUMBER "))
SECOND_NUMBER=int(input("ENTER SECOND_NUMBER "))
SUM=FIRST_NUMBER+SECOND_NUMBER
print("The addition of",FIRST_NUMBER,"AND",SECOND_NUMBER,"=",SUM)

# #division
DIVIDENT=int(input("ENTER FIRST_NUMBER"))
DIVISOR=int(input("ENTER SECOND_NUMBER"))
DIVIDE=DIVIDENT/DIVISOR
print("The DIVISION of",DIVIDENT,"AND",DIVISOR,"=",DIVIDE)

# #Q2 - Write a Python program to find the area of a triangle
Base_of_triangle=int(input("ENTER FIRST_NUMBER "))
height_of_triangle=int(input("ENTER SECOND_NUMBER "))
Area_of_triangle=1/2*Base_of_triangle*height_of_triangle
print("The Area_of_triangle ",Area_of_triangle)

#Q3 - Write a Python program to convert Celsius to Fahrenheit.

celcius=int(input("enter temeperature in celcius "))
Fahrenheit=9/5*celcius+32
print(celcius,"is equal to",Fahrenheit,"degree")

#Write a Python program that return all datatypes that we discussed in the class.

value1=int(input("enter the number "))
print("the datatype of ",value1,"is",type(value1))

value2=float(input("enter the DECIMAL "))
print("the datatype of ",value2,"is",type(value2))

value3="ASHHAL"
print("the datatype of ",value3,"is",type(value3))

value4=True
print("the datatype of ",value4,"is",type(value4))
