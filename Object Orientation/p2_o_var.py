# Private Variable - __var

# Program about private variables.
class Income:
    __contributers=30 # private attribute class var

    # Constructor
    def __init__(self):
       # declaring private instance variable
       self.__salary=20

    # instance Method public
    def __get_salary(self):
        return self.__salary
    
    def modify(self):
        self.__salary=40

 # guest area   
i=Income()
print("Private var")
print(i.get_salary())
# print(i.__salary)
# print(i.get_salary()) 
# i.modify()
# # print(i.salary)
# print(i.get_salary())

# Private variable

# private variale can not be access directly outside of class.
# print(Income.__contributers) # op- AttributeError: type object 'Income' has no attribute '__contributers'
# We can access private variable only inside of class.
# we can modify private variable only inside of class.
# We can access private variable outside of class through public method.
# We can modify private variable only inside of class.

# Use double underscores (__var) to define private variables.
# Direct access to private variables is restricted, but Python uses name mangling to store them as _ClassName__var.
# Always use getter (get_balance()) and setter (deposit()) methods to access and modify private data.

'''
In Object-Oriented Programming (OOP), the term used to hide private variables is called Encapsulation.
Encapsulation is the principle of restricting direct access to an object's data and only allowing controlled access through methods.
This protects data integrity and prevents unintended modifications.
'''

# Public Variable - By default public

class Income:
    contributers=30

    def __init__(self):
       # declaring private instance variable
       self.salary=20

    def get_salary(self):
        return self.salary, Income.contributers
    
    def modify(self):
        self.salary=40
    
i=Income()
i.get_salary()
print(i.get_salary()) 
i.modify()
print(i.get_salary())
print(i.salary)
print(Income.contributers)

# Public variable
# Unlike private variables (__var), public variables do not undergo name mangling (_Class__var).
# This means they can be accessed directly without any special syntax.
# Public variables can be accessed and modified from both inside and outside the class.
# Public variables are inherited by child classes without restrictions

'''
In Object-Oriented Programming (OOP), 
a public variable refers to an attribute that is accessible from outside the class without any restrictions.

'''

# Static Variable - Static variables (also called class variables) are shared across all instances of a class. 
# They belong to the class itself, not individual objects.

class Society:
    # static or class variable
    name="Vylage"

    def __init__(self): # object refence as perameter
        pass

    @ staticmethod # This is satic method. so here object is not passed.
    def get_data():
        return Society.name
    
    @classmethod # Static method
    def getdata(cls): # class reference as parameter
        return f"{cls.name}, {type(cls.name)}"
    
# we can access with class name or object name bothways.
# We can modify outside class using class name or object name.
# we can access inside or outside the class.
# we can modify inside or outside of class.

    
s=Society()
print(s.name)
print(Society.name)
Society.name="Blidge" # using class name
print(s.get_data()) # accessing static method
s.name="Pretege"
print(s.getdata()) # accessing instance method


# Protected Variable
# protected variables are indicated by a single underscore (_) before the variable name.
#  This is a convention, not a strict enforcement.
#  It suggests that the variable is intended for internal use within a class and its subclasses,
#  but it can still be accessed from outside the class if needed.

class Parent:
    def __init__(self):
        self._protected_var = 42  # Protected variable

class Child(Parent):
    def show(self):
        print(f"Protected variable: {self._protected_var}")

# Creating objects
obj = Child()
obj.show()  # Accessing within subclass

# Accessing outside class (not recommended, but possible)
print(obj._protected_var)  