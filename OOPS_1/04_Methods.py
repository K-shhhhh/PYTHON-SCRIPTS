"""

METHODS : 
- FUNCTIONS THAT BELONG TO OBJECTS
- A CLASS HAS DATA(ATTRITIBUTES) AND METHODS(FUNCTIONS)
- EXAMPLE: STRING METHODS, DICTIONARY METHODS ETC

- WE DEFINE METHODS BELOW OUR CONTRUCTOR IN OUR METHOD, THE FIRST PARAMETER SHALL ALWAYS BE SELF

- SYNTAX : 
    DEF METHOD_NAME(SELF):
        COMMAND

- AFTER THIS WE CREATE OUR OBJECT
- AFTER CREATING OBJECT WE CALL OUR METHODS AND PRINT
- DECORATOR : A METHOD THAT MODIFIES BEHAVIOR OF ANOTHER METHOD
- A DECORATOR IS ALWAYS USED WITH '@'

- TYPES OF METHODS:-
        
        1. INSTANCE/OBJECTS METHODS : 
        - WORK AT OBJECT LEVEL 
        - ALWAYS USE SELF PARAMETER
        - ALWAYS LINKED WITH OBJ.ATTR

        2. STATIC METHODS : 
        - USED WHEN WE DONT WANT TO ACCESS/CHANGE ANY OBJECT/CLASS ATTRIBUTES 
        - GENERALLY USED WHEN SOMETHING DEFAULT IS NEEDED
        - DOESNT USE SELF PARAMETER
        - CANT ACCESS OR MODIFY CLASS STATE & GENERAL UTILITY
        - SYNTAX : 
            CLASS CLASS_NAME:
            @STATIC METHOD         # DECORATOR
                DEF METHOD_NAME 
                COMMANDS

        3. CLASS METHODS : 
        - BOUND TO THE CLASS 
        - TAKES CLASS AS AN IMPLICIT FIRST ARGUEMENT
        - CLASS CLASS_NAME : 
            @CLASSMETHOD            # DECORATOR
                DEF METHOD_NAME(CLS, NAME):
                COMMANDS

- @PROPERTY : A DECORATOR THAT ALLOWS US TO DEFINE METHODS THAN CAN BE ACCESSED LIKE ATTRIBUTES


"""
print("\n")

# Q1. GREET 2 STUDENTS AND SHOW THEIR MARKS USING METHODS

class students:                                    # CREATE CLASS
                
    def __init__(self, name, marks):               # CONSTRUCTOR FUNCTION                  
        self.name = name                           # 1ST OBJ.ATTR                          
        self.marks = marks                         # 2ND OBJ.ATTR

    def welcome(self):                             # DEFINE METHOD1 WITH SELF
        print("WELCOME",self.name)                 # COMMAND

    def get_marks(self):                           # DEFINE METHOD2 WITH SELF
        return self.marks                          # RETURN WALUE IN METHOD2
    
S1 = students("KRISH", 97)                         # CREATE 1ST OBJECT
S1.welcome()                                       # CALLING METHOD1
print("YOUR MARKS ARE",S1.get_marks(),"\n")        # CALLING METHOD2

S2 = students("HIYU", 94)                          # CREATE 1ST OBJECT
S2.welcome()                                       # CALLING METHOD1
print("YOUR MARKS ARE",S2.get_marks(), "\n")             # CALLING METHOD2


# Q2. CREATE A CLASS THAT HAS 2 NAMES & MARKS OF 3 SUBJECTS AS ARGUEMENT IN CONSTRUCTOR. THEN CREATE A METHOD TO PRINT AVERAGE    

class STUDENT:                                                  # CREATE CLASS

    def __init__(SELF, NAME, MARKS):                            # DEF CONSTRUCTOR
        SELF.NAME = NAME                                        # 1ST OBJ.ATTR
        SELF.MARKS = MARKS                                      # 1ST OBJ.ATTR

    @staticmethod                                               # DECORATOR
    def FEEDBACK():                                             # STATIC METHOD
        print("GOOD WORK EVERYONE")                             # COMMAND
    
    def AVG(SELF):                                              # DEF METHOD
        SUM = 0                             
        for ele in SELF.MARKS:                                  # LOOP FOR SUM
            SUM = SUM + ele
        print("MR.",SELF.NAME,",YOUR AVERAGE MARKS ARE",SUM/3)  # COMAND   



S1 = STUDENT("BRUCE WAYNE", [99,98,97])                         # USER INPUT      
S1.NAME = "BATMAN"                                              # CHANGING NAME USING OBJECTS
S1.AVG()                                                        # CALLING METHOD

S2 = STUDENT("TONY STARK", [98,97,96])                          # USER INPUT      
S2.AVG()                                                        # CALLING METHOD

S1.FEEDBACK()                                                   # CALLING STATIC METHOD
print("\n")

# Q3. CREATE ACCOUNT CLASS WITH BALANCE AND ACC.NO, CREATE METHODS FOR DEBIT, CREDIT AND PRINTING BALANCE

class accounts:                                         # CREATE CLASS

    def __init__(self, bal, acc_no):                    # DEF CONSTRUCT FUNCTION
        self.bal = bal                                  # OBJ.ATTR1
        self.acc_no = acc_no                            # OBJ.ATTR2

    def debit(self, amount):                            # DEBIT METHOD
        self.bal -= amount
        print("Rs.", amount, "was debited")
        print("total balance =",self.new_balance())     # CALLING NEW_BALANCE METHOD

    def credit(self, amount):                           # CREDIT METHOD  
        self.bal += amount
        print("Rs.", amount, "was credited")
        print("total balance =",self.new_balance())     # CALLING NEW_BALANCE METHOD

    def new_balance(self):                              # NEW_BALANCE FUNTION
        return self.bal

C1 = accounts(10000, 12345)                             # BALANCE AND ACCOUNT NO.
C1.debit(1000)                                          # DEBIT AMOUNT
C1.credit(2000)                                         # CREDIT AMOUNT
print("\n")


# Q4. CHANGE DEFAULT NAME INSIDE A CLASS THROUGH AN OBJECT USING CLASS METHOD

class Person :                                          # CREATE CLASS

    name = "anonymous"                                  # NAME INPUT                                

    @classmethod                                        # DECORATOR
    def changename(cls, name):                          # CLASS METHOD CREATED
        cls.name = name                                 # LINKED NAME WITH CLASS

p1 = Person()                                           # CREATE OBJECT
p1.changename("KRISH LONGWANI")                         # NAME CHANGED
print(Person.name)                                      # CLASS NAME CHANGED VIA OBJECT P1
print("\n")

# Q5. CALC AVG OF 3 SUBJ, AND THEN IF ONE SUBJ MARKS ARE CHANGED, THE AVG SHOULD MODIFY 

class Subjects:

    def __init__(self, cn, python, git):
        self.cn = cn
        self.python = python
        self.git = git

    @property
    def avg(self):
        return (self.cn + self.python + self.git ) / 3
    
s1 = Subjects (50,60,70)
print("AVERAGE =",s1.avg)

s1.python = 90
s1.cn = 80
print("MODIFIED AVERAGE =",s1.avg)