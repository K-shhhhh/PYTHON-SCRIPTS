"""

PRIVATE ATTRIBUTES/METHODS :
MEANT TO BE USED ONLY WITHIN THE CLASS 
NOT ACCESSIBLE FROM OUTSIDE THE CLASS
DETAILS THAT ARE PUBLICALLY AVAILABLE, CAN BE MANUPILATED VERY EASILY
USE 2 UNDERSCORES (__) TO MAKE ATTRIBUTES OR METHODS PRIVATE

SYNTAX TO MAKE PRIVATE :
    DEF __INIT__(SELF, OBJ1.ATTR, OBJ2.ATTR)
    SELF.__OBJ1.ATTR  = OBJ1.ATTR
    SELF.__OBJ2.ATTR  = OBJ2.ATTR
"""
print("\n")

# Q. WAP OF A CUSTOMER WHOSE ACC_NO IS ACCESSIBLE BUT PASSWORD IS PRIVATE

class Account:                                          # CREATE CLASS

    def __init__(self, acc_no, acc_password):           # DEF CONSRUCTOR WITH OBJ1/OBJ2
        self.acc_no = acc_no                            # LINK OBJ1
        self.__acc_password = acc_password              # LINK PRIVATE OBJ2

    def prnt_pass(self):                                # DEF PRINT METHOD                    
        print(self.__acc_password)                      # COMMAND

C1 = Account("12345","ABCDE")                           # USER INPUT ON OBJ1,OBJ2
print(C1.acc_no)                                        # PRINT OBJ1
print(C1.prnt_pass(),"\n")                              # PRINT OBJ2 BY CALLING METHOD
print(C1.acc_password)                                  # PRINT OBJ2 DIRECTLY, CAUSES ERROR

# Q2. GIVE AN EXAMPLE OF PRIVATE METHOD

class greetings:                                        # CREATE CLASS
    
    def __hello(self):                                  # CREATE PRIVATE METHOD
        print("HELLO")                                  # "HELLO"

    def welcome(self):                                  # CREATE METHOD2
        self.__hello()                                  # ACCESSING METHOD1

G1 = greetings()                                        # CREATE OBJ
print(G1.welcome(),"\n")                                # PRINT "HELLO" BY CALING METHOD2 
print(G1.__hello())                                     # PRINT "HELLO" DIRECTLY, ERROR

