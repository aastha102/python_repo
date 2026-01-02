# class with constructor
class Person:
    def __init__(self):
        self.name="Vijay"
        self.age=20
    def display(self):
        print(f"{self.name} and {self.age}")
    
    def __str__(self):
        return self.name
    
    def __call__(self):
        return self.name

p=Person()
p.display()
print(p)
print(p())
print(callable(p))

# Encapsulation

class BankAccount:
    def __init__(self, AC_holder):
        self.ac_holder=AC_holder
        self._balance=100

    def balance_check(self):
        return self._fetch_bank_balance()

    def _fetch_bank_balance(self):
        return self._balance
    
    def deposit_balance(self, amt):
       self._balance=self._balance+amt
       return self._balance


ba=BankAccount("Govind")
print(ba.balance_check())
print(ba.deposit_balance(1000))
print(ba.balance_check())

# Inheritance

class Animal:
    def category(self):
        print(f"Animal")

class Dog(Animal):
    def speak(self):
        print(f"Bark")

print(Dog().speak())
print(Dog().category())

# Polymorphism

class Shape:
    radius=2
    @classmethod
    def area(cls):
        return cls.radius

class Circle(Shape):

    def area(self):
        return 3.14*self.radius**2

class Rectangle(Shape):
    @staticmethod
    def area():
        return 2*314*Shape.radius
    
c=Circle()
print(c.area())
r=Rectangle()
print(r.area())

# Abstract class
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):  # Concrete class implementing the abstract method
    def start(self):
        print("Car started")

v = Car() # v=Vehicle() # cannot instantiate abstract class
v.start() 

# Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return self.x+self.y+other.x+other.y
    
p1=Point(10, 20)
p2=Point(10,20)
print(p1+p2)

#Static Method and Class Method
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        print(f"This is class: {cls.__name__}")

print(MathUtils.add(5, 10))
MathUtils.info()

# Property decorator - The @property decorator is used to convert a method into a read-only attribute.
# Without @property: emp.full_name()  # You call it like a method
# With @property: emp.full_name  # You access it like an attribute
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"

    @full_name.setter
    def full_name(self, name):
        self.fname, self.lname = name.split(" ")

    @full_name.deleter
    def full_name(self):
        self.fname = None
        self.lname = None

emp = Employee("John", "Doe")
print(emp.full_name)     # John Doe

emp.full_name = "Jane Smith"   # Calls setter
print(emp.fname)         # Jane
print(emp.lname)         # Smith

del emp.full_name        # Calls deleter
print(emp.fname)         # None