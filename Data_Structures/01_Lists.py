"""
LISTS:
EQUIVALENT TO ARRAYS IN C 
BUILT IN DATA TYPE THAT STORESA SET OF VALUES
CAN STORE VALUES OF DIFFERENT DATA TYPE I.E. INT FLOAT STR 
EXAMPLE : marks = [54,56,78]        
          student = ["krish","87","Surat"]
          student [0] = "Arjun"
INDEXING AND SLICING IS ALLOWED IN LISTS WITH END INDEX ISNT INCLUDED
LISTS ARE MUTABLE / CHANGABLE IN PY BUT STRINGS ARE NOT
LISTS ALSO HAVE FUNCTIONS CALLED LISTS METHODS
EXAMPLES : APPEND(), SORT(), SORT(REVERSE=TRUE), REVERSE(), INSERT (INDEX,ELEMENT)
           REMOVE(), POP()
IN LISTS, USE METHOD FIRST THEN PRINT BUT IN STR WE CAN USE FUNCTION AND PRINT TOGETHER
"""

# Q1. make a list of name marks city; print it; access its 3rd index; print its length
marks = ["krish",96,"surat","hiyu",89,"surat"] 
print(marks)
print(marks[3])
print(len(marks))
print("\n")

# Q2. CHANGE THE NAME HIYU TO HEADACHE IN THE LAST LISY
marks [3] = "HEADACHE"
print(marks)
print("\n")

# Q3. USE APPEND, SORT, REVERSE SORT, REVERSE, INSERT, REMOVE, POP METHODS IN A LIST
list = [10,40,20,50,30]
list.append(60)     # 60 ADDED AS LAST ELEMENT
print(list)
list.sort(reverse=True)     # LIST IN DESCENDING ORDER
print(list)
list.sort()         # LIST IN ASCENDING ORDER
print(list)
list.reverse()      # LIST IN REVERSE ORDER
print(list)         
list.insert(3,70)   # ADDED 70 AS 3RD ELEMENT
print(list)
list.remove(70)     # REMOVES '70' FROM LIST
print(list)
list.pop(5)         # REMOVES ELEMENT FROM THE 5TH INDEX
print(list)
print("\n")
 
# Q4. TAKE 4 MOVIES FROM USER, MAKE A LIST AND PRINT IT
movie1 = input("ENTER MOVIE : ")
movie2 = input("ENTER MOVIE : ")
movie3 = input("ENTER MOVIE : ")
movie4 = input("ENTER MOVIE : ")
movies = []
movies.insert(0,movie1)
movies.insert(1,movie2)
movies.insert(2,movie3)
movies.insert(3,movie4)
print(movies)

# Q5. PRINT A LIST WITH USER INPUTS 
n =  int(input("enter length of list = "))
list1 = []
for ele in range(1,n+1):
    i = int(input("enter number  = "))
    list1.append(i)


print(list1,"\n")



# Q6. CHECK IF THE LIST CONTAINS PALINDROME OF ELEMENTS
list1 = ["krish", 5, 5, "KRish"]
if (list1[0] == list1[3]):
    if(list1[1] == list1[2]):
        print("PALINDROME")
    else:
        print("NON PALINDROME")
else:
    print("NON PALINDROME")
