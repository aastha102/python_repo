#------------------------------------------------- Object Orientations -------------------------------------------------------------# 

'''
Docstring for OOPs - Encapsulation, Datahiding, Inheritance, Name Mangling,
'''


# Write a program to count the number of objects created for a class.

class C:
    count=0

    def __init__(self):
        C.count=C.count+1

c0=C()
c1=C()
c2=C()
print(f"Total object created : {C.count}")

# Create a class with private variables and access them using getter and setter methods.
# Implement data hiding using name mangling.

class P:
    def __init__(self):
        self.__code=102 # internaly becomes self._P.__code # python does not have any private variable, Can acheive through name mangling

    def get_code(self):
        return self.__code
    
    def set_code(self, code):
        if self.__code==102:
            self.__code=code
p=P()
p.set_code
# print(p._P.__code)

# Write a class where salary cannot be set to a negative value.
# Create a class with read-only attributes.

class Account:
    def __init__(self, salary):
        self.__salary=0
        self.set_salary(salary)

    def set_salary(self, salary):
        if salary>0:
            self.__salary=salary
        else:
            print("Negative salary cannot set")

    def get_salary(self):
        return self.__salary

a=Account(1000)
print(a.get_salary())
# p.__salary # read only

# key points -
# Always initialize attributes in __init__
# Setter must not leave object in invalid state
# Getter should return, not print
# Printing inside getter is bad design


# Validate input data inside setter methods.

class Student:
    def __init__(self,marks):
        self.__marks=1
        self.set_marks(marks)

    def set_marks(self, marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("Invalid Marks")
    def get_marks(self):
        return self.__marks

s=Student(100)
print(s.get_marks())

# Create a base class Vehicle and a derived class Car.
# Override a method in a child class.
# Implement single inheritance.
# Use super() to call a parent class constructor.
# Implement multilevel inheritance.

class Vehicle:
    def __init__(self, speed):
        self._speed=speed

    def show_speed(self):
        print(f"Vehicle Speed {self._speed}")

class Car(Vehicle):
    def __init__(self, speed, mileage):
        self.mileage=mileage
        super().__init__(speed)

    def show_speed(self):
        print(f"Car speed {self._speed}")
        return super().show_speed()
    
class BMW(Car):
    def __init__(self, speed, mileage):
        super().__init__(speed, mileage)


v=Vehicle(500)    
c=Car(1000, 500)
c.show_speed()

# Implement multiple inheritance.
# Resolve method name conflict in multiple inheritance.
# Create a program demonstrating hierarchical inheritance.
              
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    def show(self):
        super().show()   # follows MRO
        print("Class C")

class D(C):
    pass

obj = C()
obj.show()

# Check the order of method resolution (MRO).

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())
#  [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# Write a program demonstrating method overriding.

class Animal:
    def sound(self):
        print("Animal makes a bark")

class Dog(Animal):
    def sound(self):
        print("Dog Barks") 


# Create two classes with the same method name but different behavior. 

class Scanner:
    def show(self):
        print("Scanning")

class Printer:
    def show(self):
        print("Printing")

# Implement polymorphism using function arguments. 

class Car:
    def move(self):
        print("Car Moves")
    
class Bike:
    def move(self):
        print("Bike moves")

def transport(Vehicle):
    Vehicle.move()

transport(Bike())
transport(Car())

# Demonstrate operator overloading.
# Overload + operator for a custom class. 
 
class Salary:
    def __init__(self, amount):
        self.amount=amount

    def __add__(self, other):
        return self.amount+other.amount

s1=Salary(10000)
s2=Salary(20000)
print(s1+s2)

# Write a program using duck typing. 
# Duck typing - it depends on behaviour not type - If it walks like a duck and quacks like a duck, it is a duck.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------#
# What is Duck Typing?
# Duck typing is a programming concept where the type of an object is determined by its behavior (methods and properties), not by its class or inheritance.
# “If it walks like a duck and quacks like a duck, it is a duck.”

# In Python:
# You don’t check an object’s type
# You check whether it supports the required operation
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Laptop:
    def work(self):
        print("Laptop is working")

class Human:
    def work(self):
        print("Human is working")

def do_work(entity):
    entity.work()

l = Laptop()
h = Human()

do_work(l)
do_work(h)

# | Feature              | Duck Typing | Polymorphism (Inheritance) |
# | -------------------- | ----------- | -------------------------- |
# | Requires inheritance | ❌ No        | ✅ Yes                      
# | Type checking        | Runtime     | Compile / Runtime          |
# | Flexibility          | High        | Medium                     |
# | Coupling             | Loose       | Tight                      |

# Use polymorphism with inheritance.

class Shape:
    def area(self):
        print("Calculating area")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle = length * width")

class Circle(Shape):
    def area(self):
        print("Area of Circle = π * r * r")

shapes = [Rectangle(), Circle()]

for shape in shapes:
    shape.area()
# Same method area() → different implementations
