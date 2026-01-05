# Create an abstract class using abc module. 
# Implement abstract methods in child classes. 
# Create a program where abstract class enforces method implementation. 
# Design an abstraction for payment systems (CreditCard, UPI, NetBanking). 
# Create an abstract class with both abstract and non-abstract methods.

from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")
        
class UPI(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")

        
class NetBanking(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using NetBanking")

payments=[CreditCard(), UPI(), NetBanking()]

for p in payments:
    p.pay(1000)


# Implement __str__() and __repr__() methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Aastha", 25)

print(p)        # uses __str__
print(repr(p))  # uses __repr__

# __str__() → user-friendly
# __repr__() → developer/debugging representation

# Create a class method to track number of instances.
# Demonstrate the difference between instance, class, and static methods.
# Modify class variables using class methods.

# Write a static method for utility functionality.
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(10, 20))  # 30


# A static method is a method that:
# Belongs to a class, not to an object (instance)

# Does not use:
# instance variables (self)
# class variables (cls)
# Works like a normal function, but is logically grouped inside a class
# Static methods are mostly used for utility/helper functionality.

# @staticmethod - This is a decorator
# It tells Python:
# “This method does NOT need access to instance (self) or class (cls) data”
# So add() behaves like a plain function, but lives inside the class.

# Create a factory method using class methods.
# A factory method returns an object based on input.

class Payment:
    def __init__(self, method):
        pass

    @classmethod
    def create_payment(cls, method_type):
        if method_type.lower()=="creditcard":
            return cls("Credit Card") #cls("Credit Card") is the same as: Payment("Credit Card")
        elif method_type.lower()=="netbanking":
            return cls("Net Banking")
        elif method_type.lower()=="upi":
            return cls("UPI Payment")
        else:
            raise "Invaid payment method"
        
p1=Payment.create_payment("CreditCard")
# print(p1.method)
