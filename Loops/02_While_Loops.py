"""
WHILE LOOPS

SYNTAX :-
WHILE CONDITION:
    STATEMENT
    UPDATION

NEVER CREATE INFINTE LOOP

"""

# Q1. PRINT "HELLO" 10 TIMES
i=1
while i<=10:
    print("HELLO")
    i = i+1
print("\n")

# Q2. PRINT MULTIPLICATION TABLE OF A NUMBER X
x = int(input("enter number = "))
i = 1
while i <= 10:
    print(x * i)
    i =i+1 
print("\n")

# Q3. PRINT THE SERIES OF SQUARES FROM 1 TO 10
num = 1
a = 1
i = 1
while i <= 10:
    print(a)
    num = num + 1 
    a = num * num
    i = i + 1
print ("\n")

# Q4. ENTER A SERIES OF NUMBERS IN A TUPLE AND SEARCH FOR A NUMBER X
tup1 = (10,20,30,40,50)
num = int(input("enter number = "))
i = 0
while i < len(tup1):
    if (tup1[i] == num) :
        print("NUMBER FOUND AT INDEX", i)
        break
    else :
        print("finding")
    i = i + 1
print("\n")

# Q5. FIND SUM OF FIRST N NUMBERS
n = int(input("enter number = "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)
