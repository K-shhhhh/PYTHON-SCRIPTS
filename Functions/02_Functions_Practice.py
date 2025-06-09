# Q1. Write a function  prints the string "Hello, World!".
def greet():
    print("Hello world!")
greet()
print("\n")

# Q2. ADDITION OF TWO NUMBERS
def add(a,b):
    sum = a + b
    return sum

print(add(2,3),"\n") 

# Q3. TAKE AN INT AS INPUT AND THEN PRINT TRUE IF EVEN ELSE FALSE 
n = int(input("enter number = "))
def even(n):
    if (n%2==0):
        return "EVEN"
    else:
        return "FALSE"
print(even(n),"\n")

# Q4. ENTER 3 NUMBERS AND PRINT THE LARGEST OF THEM
a = int(input("enter number = "))
b = int(input("enter number = "))
c = int(input("enter number = "))
def max(a,b,c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c
print("LARGEST NUMBER =",max(a,b,c),"\n")

# Q5. PRINT FACTORIAL OF N
N = int(input("enter number = "))
def fact(N):
    i = 1
    for element in range(1,N+1):
        i = i * element
    return i
print("FACTORIAL =",fact(N),"\n")

# Q6. REVERSE A STRING
str = input("enter string = ")
n = len(str)
str2 = ""
def rev(str):
    i = 0
    for char in range(0,n):
        str2[i] = str[n]

# Q7. PRINT A LIST AND SUM OF ITS ELEMENTS
list1 = [1,2,3,4,5]
def sum(list1):
    n = 0
    i = 0
    for elements in range(5):
        n = n + list1[i]
        i = i + 1
    return n 
print(sum(list1),"\n")

# Q8. CHECK WHETHER A NUMBER IS A PRIME NUMBER OR NOT
n = int(input("enter a number = "))
def prime(n):
    i = 2
    while i <= n/2:
        if (n % i == 0):
            return "NON - PRIME"
        else:
            return "PRIME"
print(prime(n))

# Q9. PRINT THE FIBONNACI SERIES5
n = int(input("enter n = "))
a = 0
b =1 
c = 0
print(a)
print(b)
list1 = [a,b]
def fib(a,b,c):
    for ele in range(n-2):
        c = a + b
        list1.append(c)
        a = b
        b = c
    return list1
print(fib(a,b,c),"\n")

# Q10. PALINDROME CHECKER
n = int(input("enter n = "))
def palindrome(n):
    pal = 0
    a = 0 
    while a > 10:
        a = n / 10 
        pal = (pal * 10) + a
    return pal
print(palindrome(n))