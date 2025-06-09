"""
FOR LOOP
VERY DIFFERENT FROM FOR LOOP IN C
THESE ARE USED FOR SEQUENTIAL TRAVERSAL I.E. MOVING IN A DEFINITE ORDER 
GENERALLY USED FOR TRAVERSING IN LIST, STRING, TUPLES, SETS

SYNTAX:
FOR 'ELEMENT' IN 'LIST':
    STATEMENT
    UPDATION

SYNTAX WITH ELSE:
FOR 'ELEMENT' IN 'LIST' :
    STATEMENT
    UPDATION
ELSE:
    STATEMENT WHEN LOOP ENDS

RANGE() IS A FUNCTION THAT RETURNS NUMBERS FROM 0 TO A SPECIFIED NUMBER WITH INCREMENTS BY 1 BY DEFAULT
WE CAN DECIDE THE STARTING POINT, STOP POINT AND STEP SIZE BY HOW MUCH FOR A RANGE
EXAMPLE : RANGE(5) = 0,1,2,3,4
          RANGE(4,10,2) = 4,6,8

"""

# Q1. PRINT A LIST CONSISTING OF INT, STR, FLOAT, TUPLE, SET
list = [1,2.1,"KRISH",("HIYU","VARNIKA"),{"CHACHU,CHACHI"}]
for value in list:
    print(value,type(value))
print("\n")

# WE CAN USE THIS FOR LOOP FOR LISTS, STRINGS, TUPLES, SETS

# Q2. PRINT A LIST WITH USER INPUTS 
n =  int(input("enter length of list = "))
list1 = []
for ele in range(1,n+1):
    i = int(input("enter number  = "))
    list1.append(i)


print(list1,"\n")


# Q3. SEARCH FOR A NUMBER X IN A TUPLEU SING FOR LOOP
list1 = (1,2,3,4,5,6,7,8,9,10)
x = int(input("enter number = "))
index = 0
for val in list1:
    if (x == val):
        print("number found at index",index)
        break
    index = index + 1
print("\n")

# Q4. PRINT ALL ODD NUMBERS FROM 0 TO 100 USING RANGE FUNCTION     
for ele in range(1,100,2):       # 1 = START, 10 = END, 2 = STEP SIZE
    print(ele) 
print("\n")         

# Q5. PRINT MULTIPLICATION TABLE OF A NUMBER X USING RANGE 
x = int(input("enter a number = "))
for val in range(x,x*11,x):         
    print(val)
print("\n")

# Q6. FIND THE FACTORIAL OF FIRST N NUMBERS
n = int(input("enter a number = "))
i = 1
for element in range(1,n+1):        # START = 1, END = N+1 AS WE NEED THE NTH VAUE
    i = i * element                 # WE ACCESS THE ELEMENT IN RANGE I.E. 1,2,3...
print(i)