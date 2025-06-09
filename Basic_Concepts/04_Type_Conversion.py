# converting dataypes of a single variables
# two types of conversions in py

# 1. type conversion
# interpreter does it for us automatically
a = 2
b = 4.25

c = a + b # int, float are different values but interpreter automatically takes float as superior 
print(c)  # 6.25

# 2. type casting
# we have to do it manually
# ex : if we try to add str and float it will give error, in that case we do type casting which is done manually

c = int("3") # initially str, using int() function we converted str to int
d = 2.5 # float

print (c + d) # 3 + 2.5 = 5.5
