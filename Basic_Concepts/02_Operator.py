# 1. arithmetic operators (+,-,*/%/**)

a = 18 # assignment oprator '=' used
b = 7
c = 5

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)  # called modulo operator, gives us the remainder 
print(a**b) # called power operator, gives us result of a power b 

# 2. relational operators (==,!=,>,<,>=,<=), always boolean values returned
    
print(a==b)     #false
print(a!=b)     #true
print(a>b)      #true
print(a<b)      #false

# 3. assignment operators (=,+=,-=,*=, /=, %=,**=)
#  when 2 arithmatic operators are combined, the order is very important as that shows the sequence of operations

num = 10

num +=10 # num = num + 10, num = 20
print (num)

num -=10 # num = num - 10, num = 10
print(num)

num *=10 # num = num * 10, num = 100 
print(num)

num /=10 # num = num / 10, num = 10.0
print(num)

num %=10 # num = num % 10, num = 0
print(num) 

num = 10 

num **=10 # num = num ** 10 = num = 10 ** 10
print(num)

# 4. logical operators (not, and, or), works on boolean values

print(not False)    # true
print(not True)     # false

print((a > 5) and (b > 5))  # gives true only when both conditions are true

print((a == b) or (a > b))   # gives true as second condition is true
