class Human():
    def __init__(self):
        print("Human constructor")

class Employee(Human):
    def __init__(self):
        print("Employee constructor")

    def display(self):
        pass


class Manager(Employee, Human):
    def __init__(self):
        super().__init__()
        print("Manager constructor")

m=Manager()