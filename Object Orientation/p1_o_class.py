# Ways to declare a class -

class Company:
    company_type="Service Based" # attribute # class variable
    print(company_type)

    def __init__(self):
        self.location="Bangalore" # location is instance var which can be accessed by object
        print(self.location)
    def get_name(obj_ref): # methods # instance methods        print(obj_ref.name)
        print("It is applicable from python 3.2 version below that not applicable")

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Constructor", self.name, self.age)
p1=Person("arjun", 25)
# p1.name="Arjun"
# p1.age=25
# p1.city="Bangalore"
# print(p1.age, p1.name, p1.city)
p2=Person("yatish", 25)
p3=Person("santosh",25)

# class Emp(): # object is hidden inside this bracket
#     pass
    

# class Emp(object): # object is the superclass
#     pass # define to empty block
#     print("It is applicable on 2.7 or 3.2 version object is the superclass.")

# # [Note; there is no specific use of using print inside class it's like normal execution]

# # Rules- class name can be small capital or title

# initialization or creation of object
# print(Company.company_type)
# infosys=Company()
# print(infosys.location)
# print(c1.name)
# print(Company().name) # obj is the reference variable which is pointing to the object of Emp class
# print(obj.name)
# obj.get_name()
# Emp() This is creating object of Emp class

# class Emp():
#     # class level 
#     # It can be accessed by calsss name or object.
#     name="Kanki" # class variable or static variable

    
# e=Emp.name
# print(e)
# print(Emp.name)

# class people:
#     # constructor - Automatically called at initialization of object
#     def __init__(self): # self is not keyword it's a parameter name, it can be anything.
#         # use self is for better understanding

#         self.age=20 # declaring one variable, Declaring any variable inside constructor is instance variable

# # creation of object of class people
# peo_1=people() # while calling the contructor reference variable always passed as first argument. 
# # people(peo_1)
# # So need to use 1 parameter at the definataion to catch the argument
# # print(people.age) # can not access variable using classname
# print(peo_1.age) 

# # we have parameterized init method

class Area:
    breadth=20 # class variable - Can be accessed using cls name or obj name
    def __init__(self, breadth=40): # default constructor
        self.length=20 # instance varible
        self.breadth=breadth
        print("Object Initialization ", self) # Object Initialization  <__main__.Area object at 0x00000197C5706A50>
        

# outside of class
a=Area() # instantiation of class Area and passing a as argument to the constructor
print(f"permimeter - {a.length} * {a.breadth}")

# To resolve this issue - while printing self 
#  o/p - <__main__.Area object at 0x00000197C5706A50>

# use magic method __str__ which is present in object class

# Python class have only one init method.
# Python does not support method overloading like Java; instead, only the last defined method is kept, and the first one is ignored.

# class Perimeter:

#     # def __init__(self):
#     #     print("object initialization")
    
#     # __str__- Display object in some readable format
#     # overriding this dunder method
    
#     # By default any variable inside class is public
#     def __init__(self, length):
#         self.breadth=30 # decalring instance variable & assigning value 30 to instance variable breadth
#         self.length=length # declaring instnace variable self.length=20

#     def __str__(self):
#         return f"Object Initialization {self.length} * {self.breadth}"

# p=Perimeter(20)
# print(p) # Prininting object reference - __str__ automatically called
# # We can call __str__ explicityly as well
# print(p.__str__())
# print(p.breadth)
# print(2*(p.breadth+p.length))

class Car:
    speed = 300
    def __init__(self):
        self.color="red" # decalring instance variable and assigning value red to instance variable color

c=Car()
print(c.color)
print(Car.color)

# # Modification of instance variable
# c.color="orange"
# print(c.color)

# # Modification of class variable

# Car.speed=4000
Car.color="purple"
print(Car.color)
c.speed=400
# print(Car.speed)
# print(c.speed)