"""
SETS:
VERY SIMILAR TO SETS LEARNT IN MATHS
COLLECTION OF UNORDERED ITEMS
EACH ELEMENT IN SET IS UNIQUE AND IMMUTABLE
NO INDEXING OR SLICING BUT WE CAN ACCESS ELEMENTS
USE {}
ALL DATA TYPPES CAN BE STORED EXCEPT LIST AND DICTIONARY AS THEY ARE MUTABLE
SETS METHODS ALSO AVAILABLE
"""

# Q1. CREATE A SET WITH INT,FLOAT,STR,TUPLES and print its length
set1 = {("KRISH","HIYU","VERO"), 5.8, 5.3, 5}
print(set1)
print(type(set1))
print(len(set1),"\n")

# Q2. CREATE AN EMPTY SET AND ADD VALUES
set2 = {}
print(set2)
print(type(set2))           # CONFIRMS THAT USING {} WE CREATED EMPTY DICT
set3 = set()
print(set3) 
print(type(set3))           # CONFIRMS THAT USING SET() WE CREATED EMPTY SET

set3.add(20)                 # INSERTING ELEMENTS
set3.add("KRISH")
set3.add(5.8)
set3.add(("PROGRAMMING", "PROBLEM SOLVING"))
print(set3,"\n")

# Q3. USE REMOVE(), POP(), CLEAR(), UNION() AND INTERSECTION  METHODS
set3.remove(20)             # REMOVES 20
print(set3)
set3.pop()                  # REMOVES ANY RANDOM ELEMENT
print(set3)
set3.clear()                # CLEARS/ DELETES ALL ELEMENTS AND GIVES EMPTY SET
print(set3)
set4 = {1,2,3,5.8}
print(set4.union(set1))     # GIVES SET4 + SET5
print(set4.intersection(set1))      # GIVES COMMON ELEMENTS IN SET4 AND SET1 I.E. 5,8
