"""

PATTERNS : 
- USING LOOPS AND NESTED LOOPS, WE PRINT ANY SYMBOL OR SET OF NUMBERS IN A PATTERN ON OUR SCREEN
- PATTERN QUESTIONS ARE TRICKY AND VERY IMPORTANT FOR PROPER UNDERSTANDING OF LOOPS
- GENERALLY WE USE A FOR LOOP INSIDE A FOR LOOP
- TRICK :-
    1). OUTER LOOP SHOULD RUN AS MANY TIMES AS THE NUMBER OF ROWS
    2). INNER LOOP SHOULD TAKE CARE OF WHAT TO PRINT IN EACH ROW

- PRINT() IS USED TO GO TO NEXT LINE
- CHR() IS A BUILT-IN PYTHON FUNCTION FOR CONVERTING AN INT TO CHR ACCORDING TO ASCII VALUES
    EXAMPLE : CHR(97) = 'a'

- FORWARD INNER LOOPS  : I=1/I=0 TO I+1/I       (++)
- BACKWARD INNER LOOPS : I+1/I TO 1/0           (--)
"""
print("\n")

# Q1. CREATE PATTERN IF N = 4, [1 2 3 4--1 2 3 4--1 2 3 4--1 2 3 4]
N = int(input("ENTER N : "))                # USER INPUT
for i in range(1,N+1):                      # CREATING OUTER LOOP FOR NO. OF ROWS
    for j in range(1,N+1):                  # CREATING INNER LOOP FOR PRINTING N NUMBERS
        print(j, end = " ")                 # COMMAND TO PRINT NUMBERS TO N
    print()                                 # TO GO TO NEXT
print("\n")

# Q2. CREATE PATTERN IF N = 4, [1 2 3 4--5 6 7 8--9 10 11 12--13 14 15 16 ] 
N = int(input("ENTER N : "))                # USER INPUT
a = 1
for i in range(1,N+1):                      # CREATING OUTER LOOP FOR NO. OF ROWS
    for j in range(1,N+1):                  # CREATING INNER LOOP FOR PRINTING N NUMBERS
        print(a, end = " ")                 # COMMAND TO PRINT NUMBERS TO N
        a = a + 1
    print()                                 # TO GO TO NEXT
print("\n")

# Q3. CREATE PATTERN IF N = 4, [* * * *--* * * *--* * * *--* * * *]
N = int(input("ENTER N : "))
for i in range(1,N+1):                      # CREATING OUTER LOOP FOR NO. OF ROWS
    for j in range(1,N+1):                  # CREATING INNER LOOP FOR PRINTING N NUMBERS
        print("*", end = " ")               # COMMAND TO PRINT '*' N TIMES
    print()                                 # TO GO TO NEXT
print("\n")

# Q4. CREATE PATTERN IF N = 4, [A B C D--A B C D--A B C D--A B C D]
N = int(input("ENTER N : ")) 
for i in range(N):
    for j in range(N):
        print(chr(65+j), end = " ")            # CHR(65+J) USED TO PRINT EACH CHARACTER
    print()
print("\n")

# Q5. CREATE PATTERN IF N = 4, [A B C D--E F G H--I J K L--M N O P]
N = int(input("ENTER N : ")) 
for i in range(N):
    for j in range(N):
        print(chr(65+i*N+j), end = " ")        # I*N TO CONTINUE CHARACTER AFTER EACH LINE
    print()
print("\n")

# Q6. CREATE PATTERN IF N = 4, [*--* *--* * *--* * * *]
N = int(input("ENTER N : ")) 
for i in range(N):
    for j in range(i+1):                        # I+1 AS NO. OF STARS IN EACH LINE = LINE NO.
        print("* ", end = " ")
    print()
print("\n")

# Q7. CREATE PATTERN IF N = 4, [1--1 2--1 2 3--1 2 3 4]
N = int(input("ENTER N : ")) 
for i in range(1,N+1):                          # (1,N+1) TO INCLUDE N AS NTH LINE
    for j in range(1,i+1):                  # (1,I+1) TO START FROM 1 AND NOT 0
        print(j, end = " ")     
    print()
print("\n")

# Q8. CREATE PATTERN IF N = 4, [1--2 2--3 3 3--4 4 4 4]
N = int(input("ENTER N : ")) 
a = 1
for i in range(1,N+1):
    for j in range(1,i+1):
        print(a, end = " ")
    a = a + 1                               # TO PRINT SAME NUMBERS IN ENTIRE LINE
    print()
print("\n")

# Q9. CREATE FLOYD'S TRIANGLE IF N = 4, [1--2 3--4 5 6--7 8 9 10]
N = int(input("ENTER N : ")) 
a = 1
for i in range(1,N+1):
    for j in range(1,i+1):
        print(a, end = " ")                 
        a = a + 1                           # TO PRINT NEXT CONTINOUS NUMBER ON THE NEXT LINE
    print()
print("\n")

# Q10. CREATE PATTERN IF N = 4, [A--A B--A B C--A B C D]
N = int(input("ENTER N : ")) 
for i in range(N):
    for j in range(i+1):                  # (I+1) AS NO. OF CHARACTERS IN EACH LINE = LINE NO.
        print(chr(65+j), end = " ")
    print()
print("\n")

# Q11. CREATE PATTERN IF N = 4, [A--B B--C C C--D D D D]
N = int(input("ENTER N : ")) 
for i in range(N):
    for j in range(i+1):
        print(chr(65+i), end = " ")        # CHR(65+I) AS WE NEED SAME CHARACTER IN EACH LINE 
    print()
print("\n")

# Q12. CREATE PATTERN IF N = 4, [A--B C--D E F--G H I J]
N = int(input("ENTER N : ")) 
a = 0
for i in range(N):
    for j in range(i+1):
        print(chr(65+a), end = " ")        # CHR(65+A) TO PRINT DIFFERENT CHARACTERS 
        a = a + 1                          # A = A + 1 TO PRINT NEXT CHARACTERS
    print()
print("\n")   

# Q13. CREATE PATTERN IF N = 4, [1--2 1--3 2 1--4 3 2 1]
N = int(input("ENTER N : "))
for i in range(1,N+1):
    for j in range(i,0,-1):                # (I,0,-1) TO RUN LOOP BACKWARDS 
        print(j, end = " ")
    print()
print("\n")

  

