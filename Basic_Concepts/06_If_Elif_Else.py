# IF - ELIF - ELSE
"""
SYNTAX : 

if(condition):
    statement1
elif(condition):
    statement2
else:
    statmentN
 
If condition checks everytime, elif condition checks when if condition is false
indentation = giving proper spacing like in python

NESTING IF-ELSE : WRITING IF STATEMENT INSIDE IF STATEMENTS AND SO ON
EXAMPLE: 
IF(CONDITION1):
    IF(CONDITION2):
        PRINT(CONDITION2 STATEMENT):
    ELSE:
        PRINT(CONDITION1 STATEMENT)
ELSE:
    PRINT(ELSE STATEMENT)
"""

# Q1. WAP TO TELL WHETHER WE CAN GET LICENSE OR NOT
age = int(input("enter your age = "))
if (age >= 18):
    if (age > 80):
        print("not eligible")
    else:
        print("you are eligible")
else:
    print("not eligible")
print("\n")

# Q2. WAP TO MAKE A TRAFFIC SIGNAL MANUAL
colour = input("enter colour of the signal = ")
if (colour == "red"):
    print("stop")
elif (colour == "yellow"):
    print("wait")
elif (colour == "green"):
    print("go")
else:
    print("invalid input")
print("\n")

# Q3. WAP TO GRADE STUDENTS ON THE BASIS OF THEIR MARKS
marks = int(input("enter your marks = "))
if (marks >= 90):
    print("A-GRADE")
elif (marks >= 80):
    print("B-GRADE")
elif (marks >= 70):
    print("C-GRADE")
elif (marks >= 60):
    print("D-GRADE")
elif (marks >= 50):
    print("E-GRADE")
else:
    print("invalid input")
print("\n")

# Q4. PRINT SALARY > 15000 ,IF THE DEPARTMENT IS IT, GIVE 1000 BONUS ELSE CUT 1000
name = input("enter your name : ")
sal = int(input("enter your salary : "))
dept = input("enter your department : ")

if (sal >= 15000):
    if (dept == "IT"):
        sal = sal + 1000
        print("name =",name)
        print("department =",dept)
        print("updated salary =",sal)
    else:
        sal = sal - 1000
        print("name =",name)
        print("department =",dept)
        print("updated salary =",sal)
elif (sal < 15000):
    print("salary too low")
print("\n")

# Q5. CHECK IF THE NUMBER IS ODD OR EVEN
num = int(input("enter number = "))
if (num % 2 == 0):
    print("EVEN NUMBER")
else:
    print("ODD NUMBER")
print("\n")

# Q6. FIND GREATEST OF 3 NUMBERS
num1 = int(input("enter number = "))
num2 = int(input("enter number = "))
num3 = int(input("enter number = "))

if (num1 > num2 and num1 > num3):
    print("GREATEST NUMBER =",num1)
elif (num2 > num1 and num2 > num3):
    print("GREATEST NUMBER=",num2)
else:
    print("GREATEST NUMBER=",num3)
print("\n")

# Q7. NUMBER IS MULTIPLE OF ANOTHER NUMBER X
num4 = int(input("enter number = "))
if (num % 7 == 0):
    print("MULTIPLE OF SEVEN")
else:
    print("NOT A MULTIPLE OF SEVEN")
