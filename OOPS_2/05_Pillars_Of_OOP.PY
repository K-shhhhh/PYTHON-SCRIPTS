"""

THERE 4 PILLARS/CORE PRINCIPLES OF OOP PARADIGM:-

1. ABSTRACTION
- HIDING THE IMPLEMENTATION DETAILS OF CLASS, ONLY SHOWING ESSENTIAL FEATURES TO USER
- EXAMPLE: NO NEED TO SHOW HOW THE ENGINES WORK, JUST SHOW THE CAR
- IT BASICALLY INCLUDES  EVERY PROGRAM WE WRITE AS IN OUTPUT, NOT CODING IS VISIBLE

2. ENCAPSULATION
- WRAPPING DATA AND FUNCTIONS INTO A SINGLE OBJECT
- EXAMPLE : BASICALLY ALL OUR CODES WHERE WE USED DATA AND METHODS IN A SINGLE OBJ

3. INHERITANCE
- WHEN ONE CLASS (CHILD) DERIVES THE PROPERTIES AND METHODS OF ANOTHER CLASS (PARENT)
- EXAMPLE : A BUGATTI CAR WILL HAVE ALL THE BASIC FUNCTIONS OF A STANDARD CAR
- TYPES OF INHERITANCE:
    
    A). SINGLE INHERITANCE : 
    - 1 PARENT CLASS --------> 1 CHILD CLASS
    - SYNTAX : CLASS CHILD_CLASS (PARENT_CLASS)

    B). MUTLILEVEL INHERITANCE :
    - 1 PARENT CLASS --------> 1 CHILD(PARENT') CLASS --------> 1 CHILD CLASS
    - THE 3RD CLASS (CHILD) WILL HAVE PROPERTIES OF BOTH THE PREVIOUS CLASSES
    - SYNTAX : SAME AS SINGLE INHERITANCE

    C). MULTIPLE INHERITANCE : 
    - A CHILD CLASS HAS 2 PARENT CLASSES
    - CHILD CLASS WILL HAVE PROPERTIES OF BOTH CLASSES
    - SYNTAX : CLASS CHILD_CLASS (PARENT_CLASS1, PARENT_CLASS2)

- SUPER METHOD : USED TO ACCESS METHODS OF THE PARENT CLASS
- SYNTAX : SUPER().METHOD_NAME(ATTRIBUTE)

4. POLYMORPHISM : (POLY = MANY, MORPH = FORMS)
- OPERATOR OVERLOADING
- WHEN THE SAME OPERATOR CAN HAVE DIFF MEANING ACCORDING TO THE CONTEXT
- EXAMPLE : "+" OPERATOR IS USED FOR DIFFERENT INBUILT CLASSES LIKE :-
  A). ADD FOR INT
  B). CONCATENATION FOR STR
  C). MERGE FOR LISTS, TUPLES ETC

- CONSTRUCTOR FUNCTION (__INIT__) IS ALSO A DUNDER FUNCTION
- DUNDER FUNCTIONS : USED TO DEFINE AN OPERATOR AS PER OUR CONVIENCE
- DUNDER MEANS DOUBLE UNDERSCORE (__)
- MANY DUNDER FUNCTIONS ALREADY EXIST IN PYTHON LIKE :-

    A + B       ADDITION        A.__ADD__(B)
    A - B       SUBTRACT        A.__SUB__(B)
    A * B       MULTIPLY        A.__MUL__(B)
    A / B       DIVIDE          A.__TRUEDIV____(B)
"""

# Q1. SHOW SINGLE LEVEL INHERITANCE

class car:                                      # CREATE CLASS1
    color = "BLACK"                             # INPUT
    
    @staticmethod                               # DECORATOR
    def start():                                # DEF STATIC METHOD
        print("CAR STARTED...")                 # COMMAND

    @staticmethod                               # DECORATOR
    def stop():                                 # DEF STATIC METHOD
        print("CAR STOPPED...")                 # COMMAND

class bugatti(car):                             # CREATE CLASS2 WITH INHERTANCE OF CLASS1

    def __init__(self, name):                   # DEF CONSRUCTOR
        self.name = name                        # LINK OBJ.ATTR

c1 = bugatti("BUGGATI")                         # CREATE OBJ1
print(c1.name, c1.color)                        # PRINTING INPUT OF CLASS1 AND CLASS2
c1.start()                                      # CALLING CLASS1 METHOD
c1.stop()                                       # CALLING CLASS1 METHOD
print("\n")


# Q2. USING Q1, SHOW MULTI LEVEL INHERITANCE AND SUPER METHOD

class Veyron(bugatti):                          # CREATE CLASS3 WITH INHERTANCE OF CLASS2
    def __init__(self, name, top_speed, cost):  # DEF CONSTRUCTOR
        super().__init__(name)                  # USING SUPER TO ACCESS CLASS1 METHOD
        self.top_speed = top_speed              # LINKING OBJ.ATTR
        self.cost = cost                        # LINKING OBJ.ATTR

C1 = Veyron("BUGATTI","250 KM/H", "50 LAKHS")   # CREATE OBJ1 WITH CLASS2 ATTR ASWELL
print(C1.name, C1.color)                        # CALLING CLASS2 & CLASS3 METHOD
print(C1.top_speed)                             # CALLING CLASS3 METHOD
print(C1.cost)                                  # CALLING CLASS3 METHOD
C1.start()                                      # CALLING CLASS1 METHOD
C1.stop()                                       # CALLING CLASS1 METHOD
print("\n")

# Q3. SHOW MULTIPLE INHERITANCE

class A:                                        # CREATE CLASS1
    a = "WELCOME TO CLASS A"                    # COMMAND

class B:                                        # CREATE CLASS1
    b = "WELCOME TO CLASS B"                    # COMMAND

class C(A, B):                                  # CREATE CLASS3 WITH INHERITANCE OF CLASS1 AND CLASS2
    c = "WELCOME TO CLASS C"                    # COMMAND

S1 = C()                                        # CREATE OBJ1
print(S1.a)                                     # PRINT CLASS1 COMMAND
print(S1.b)                                     # PRINT CLASS2 COMMAND
print(S1.c)                                     # PRINT CLASS3 COMMAND
print("\n")

# Q4. CREATE 2 COMPLEX NUMBERS AND HOW THEIR ADDITION AND SUBTRACTION

class Complex:                                  # CREATE CLASS                                

    def __init__(self, real, img):              # DEF CONSTRUCTOR
        self.real = real                        # LINK OBJ.ATTR1
        self.img = img                          # LINK OBJ.ATTR2

    def show(self):                             # DEF SHOW METHOD
        print(self.real,"i +", self.img,"j")    # PRINT COMPLEX NUMBER

    def __add__(self, n2):                      # DEF ADD DUNDER FUNCTION
        newreal = self.real + n2.real           # LOGIC FOR REAL PART      
        newimg = self.img + n2.img              # LOGIC FOR IMG PART
        return Complex(newreal, newimg)         # RETURN LOGIC TO WHOLE CLASS
    
    def __sub__(self, n2):                      # DEF SUB DUNDER FUNCTION               
        newreal = self.real - n2.real           # LOGIC FOR REAL PART
        newimg = self.img - n2.img              # LOGIC FOR IMG PART
        return Complex(newreal, newimg)         # RETURN LOGIC TO WHOLE CLASS


n1 = Complex(10,9)                              # CREATE OBJ1
n1.show()                                       # PRINT OBJ1
n2 = Complex(8,7)                               # CREATE OBJ2
n2.show()                                       # PRINT OBJ2
n3 = n1 + n2                                    # DUNDER ADDITION
n4 = n1 - n2                                    # DUNDER SUBTRACTION
print("ADDITION =", end = " ")
n3.show()                                       # PRINT DUNDER ADDITION
print("\n")
n1.show()
n2.show()
print("SUBTRACTION =", end = " ")               # PRINT DUNDER SUBTRACTION
n4.show()







