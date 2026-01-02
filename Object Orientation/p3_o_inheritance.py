# Inheritance - Accessing the property of another class.
# Inheritance is a fundamental object-oriented programming (OOP) concept that allows a child class (subclass) to inherit attributes
#  and methods from a parent class (superclass).
#  This promotes code reusability and modularity.
'''
Types of Inheritance -

Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance
'''
'''-----------------------------------------------TYPES OF INHERITANCE--------------------------------------------------------------''' 

# Single Inheritance - Child class inherit property from one parent class.

# class Parent:

#     def __init__(self):
#         print("object initialization of Parent")

#     def show(self):
#         print("This is Parent class")

# class Child(Parent):

#     # def __init__(self):
#     #     print("object initialization of child")

#     def display(self):
#         print("This is Child class")

# # Creating an object of Child
# obj = Child()
# print(obj) # it will call child constructor, if init is not present in child then it only it will call parent
# obj.show()    # Inherited from Parent
# obj.display() # Defined in Child

'''---------------------------------------------------------------------------------------------------------------------------------'''

# # Muliple Inheritance - A child class inherits from multiple parent classes.

# class Father:
#     # def __init__(self):
#     #     print("Father initialization")
#     def father_feature(self):
#         print("Feature from Father")

# class Mother:
#     def __init__(self):
#         print("Mother initialization")
#     def mother_feature(self):
#         print("Feature from Mother")

# class Child(Father, Mother):
#     # def __init__(self):
#     #     print("Child initialization")
#     def child_feature(self):
#         print("Feature from Child")

# obj = Child()
# print(obj) # if child constructor not present it will execute 1st parent constructor, 
# # if 1st and child not there only then only 2nd parent class constructor
# obj.father_feature()
# obj.mother_feature()
# obj.child_feature()

'''---------------------------------------------------------------------------------------------------------------------------------'''

# Multilevel Inheritance - A child class inherits from a parent class, and another child class inherits from it.

class Grandparent:
    def __init__(self):
        print("Grandpapa object")
    def grandparent_feature(self):
        print("Feature from Grandparent")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Papa object")
    def parent_feature(self):
        print("Feature from Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child object")
    def child_feature(self):
        super().parent_feature()
        print("Feature from Child")

obj = Child()
# print(obj) # if child constructor is not there, it will execute parent, if parent and child not there then grandparent 
# obj.grandparent_feature()
# obj.parent_feature()
obj.child_feature()

'''---------------------------------------------------------------------------------------------------------------------------------'''

# Hierarchical Inheritance - Multiple child classes inherit from a single parent class.

class Parent:
    def parent_feature(self):
        print("Feature from Parent")

class Child1(Parent):
    def child1_feature(self):
        print("Feature from Child1")

class Child2(Parent):
    def child2_feature(self):
        print("Feature from Child2")

obj1 = Child1()
obj1.parent_feature()
obj1.child1_feature()

obj2 = Child2()
obj2.parent_feature()
obj2.child2_feature()

'''---------------------------------------------------------------------------------------------------------------------------------'''

# Hybrid Inheritance (Combination of multiple types) -A mix of different types of inheritance.

class A:
    def __init__(self):
        print("A object")
    def featureA(self):
        print("Feature from A")

class B(A):  # Single Inheritance
    def featureB(self):
        print("Feature from B")

class C(A):  # Hierarchical Inheritance
    def __init__(self):
        print("C object")
    def featureC(self):
        print("Feature from C")

class D(B, C):  # Multiple Inheritance
    def featureD(self):
        print("Feature from D")

obj = D()
print(obj) # if d, b, c constructor not present then will execute A constructor
obj.featureA()
obj.featureB()
obj.featureC()
obj.featureD()