class Employee:
    '''Details of Employee'''
    company_name="Apple"
    location="Bangalore"
    def __init__(self, sal):
        self.sal=sal
        print(self.sal*2)

    def display(self):
        print(f"Salary:{self.sal}")

    @classmethod
    def show(cls):
        print(f"Collge name is {cls.company_name}")

    @staticmethod
    def get_location():
        print(f"{Employee.location}")
e=Employee(2000)
print(isinstance(e,Employee)) # True
print(getattr(e,'sal')) # 2000 # salary=2000
print(setattr(e, 'sal', 5000)) # set salary=5000
print(getattr(e,'sal')) # 5000 
print(hasattr(e,'sal')) # True
delattr(e,'sal') # 
# print(getattr(e,'sal')) # 
print(__doc__)

print(Employee.show())
Employee.company_name="Microsoft"
print(Employee.show())
print(e.get_location())

        