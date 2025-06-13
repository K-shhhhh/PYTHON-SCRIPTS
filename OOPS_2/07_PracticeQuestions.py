# Q1. DEF A "CIRCLE" CLASS TO CREATE A CIRCLE WITH RADIUS USING CONSTRUCTOR. ALSO DEF AREA() AND PERIMETER() METHODS AS WELL

class Circle :

    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return (22/7) * (self.rad * self.rad)
    
    def perimeter(self):
        return (22/7) * self.rad * 2
    
c1 = Circle(21)
print("AREA =",c1.area())
print("PERIMETER =",c1.perimeter(),"\n")

# Q2. DEF A "EMPLOYEE" CLASS WITH ATTR ROLE, DEPT AND SAL. ALSO DEF SHOWDETAILS() METHOD. 

class Employee:

    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showdetails(self):
        print("ROLE :",self.role)
        print("DEPARTMENT :",self.dept) 
        print("SALARY :",self.sal)

e1 = Employee("INTERN", "IT", "5000")
e1.showdetails()
print("\n")

# Q3. USING Q2, DEF A "ENGINEER" CLASS THAT INHERITS ATTR FROM EMPLOYEE AND HAS ADDITION ATTR NAME & AGE

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "SOFTWARE", "80,000")

    def SHOWDETAILS(self):
        print("NAME =",self.name)
        print("AGE :", self.age)

E1 = Engineer("KRISH", "20")
E1.showdetails()
E1.SHOWDETAILS()
print("\n")

# Q4. DEF A CLASS "ORDER" WHICH STORES ITEM & PRICE. USE A DUNDER FUNCTION TO CONVEY THAT ORDER1 > ORDER2 IF PRICE OF ORDER1 > PRICE OF ORDER2

class Order:

    def __init__(self, item, price):
        self.item = item 
        self.price = price

    def __gt__(self,o2):
        return self.price > o2.price
    
o1 = Order("Chocoloates","Rs. 300")
o2 = Order("Ice-Cream","Rs. 200")
print(o1 > o2)


