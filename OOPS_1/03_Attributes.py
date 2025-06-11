"""

ATTRIUTES : 
THE DATA OR STATE OF OBJECT, IT CAN BE VAR OR METHODS THAT BELONG TO A CLASS
EXAMPLE : NAME, MARKS ETC
TYPES OF ATTRIBUTES :-
    
    1. CLASS ATTRIBUTES : COMMON FOR ALL OBJECTS (1 TIME FOR ALL OBJ)
    EXAMPLE : COLLEGE NAME, CITY ETC
    WE DEFINE IT BEFORE INIT FUNCTION USING _
    EXAMPLE : COLLEGE_NAME = "PSB ACADEMY" (SHOWS COLLEGE NAME IS COMMON FOR ALL)
    
    2. OBJECT ATTRIBUTES : DIFFERENT FOR EACH OBJECT (N TIMES FOR N OBJ)
    EXAMLE : NAME, MARKS, HIEGHT ETC
    TO LINK OBJECT ATTRIBUTES, WE USE . 
    EXAMPLE : SELF.NAME = NAME (SHOWS NAME IS AN OBJ ATTR LINKED WITH SELF)

    PRECIDENCE OF OBJ.ATTR > CLASS.ATTR     
"""
print("\n")

# Q. MAKE A CLASS WITH 2 STUDENTS IN PSB ACADEMY
class students:
    college_name = "PSB ACADEMY"                # STORED ONLY ONCE
    name = "anonymous"                          # NAME AS CLASS.ATTR

    def __init__(self, name):                   # STORED 2 TIMES
        self.name = name                        # NAME AS OBJ.ATTR

s1 = students("KRISH")
print(s1.name, s1.college_name)                 # PRINT USING OBJECT

s2 = students("HIYU")
print(s2.name, students.college_name)           # PRINT USING CLASS