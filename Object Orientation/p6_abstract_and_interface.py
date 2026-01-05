# ------------------------------------------------------------------------------------------------------------------#
 
# Abstraction means showing only what is necessary and hiding how it is done.

# Real-world example:
# When you drive a car, you only use:
# Steering
# Accelerator
# Brake

# You do not know how the engine internally works.
# That hiding of internal details is abstraction.

# Python provides abstraction using:
# Abstract Base Classes (ABC)
# Abstract Methods
# These are available in the abc module.

# A class that:
# Cannot be instantiated (object cannot be created)
# Contains at least one abstract method
# Used as a blueprint for child classes

# A method that:
# Has only declaration
# No implementation in the parent class
# Must be implemented in the child class

# Reduces complexity
# Improves security
# Makes code easy to maintain
# Forces correct structure
# Helps in large projects

# ------------------------------------------------------------------------------------------------------------------#

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


# Can We Achieve Abstraction Without ABC?
# Yes (but not enforced):

class Animal:
    def sound(self):
        raise NotImplementedError


# But ABC is the correct & recommended way

# Interface contains only abstract methods
# Implemented using ABC
# Child class must implement all methods
# Multiple interfaces allowed
# Cannot create object of interface

class PrinterInterface(ABC):
    @abstractmethod
    def print_data(self):
        pass

class ScannerInterface(ABC):
    @abstractmethod
    def scan(self):
        pass

class AllInOne(PrinterInterface, ScannerInterface):
    def print_data(self):
        print("Printing data")

    def scan(self):
        print("Scanning data")

device = AllInOne()
device.print_data()
device.scan()

