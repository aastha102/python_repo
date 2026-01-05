# Inheritance (IS-A relationship)

class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):   # Car IS-A Engine (not always logical)
    def drive(self):
        print("Car is driving")

c = Car()
c.start()
c.drive()

# Car is not really an Engine
# Tight coupling
# Hard to change later

# Composition (HAS-A relationship)

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def drive(self):
        self.engine.start()
        print("Car is driving")

c = Car()
c.drive()

# Loose coupling
# More flexible
# Real-world modeling

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, emp):
        self.employee = emp   # Aggregation

emp1 = Employee("Supriya")
dept = Department(emp1)

print(dept.employee.name) #Employee can exist without Department.

# Aggregation means:
# Object can exist independently
# Shared ownership
