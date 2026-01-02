# Problem Statement1
# 
class Person:
    def __init__(self, name, age, ssn):
        self.name = name             # Public attribute
        self._age = age              # Protected attribute
        self.__ssn = ssn             # Private attribute (Name mangled)

    def _display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"SSN: {self.__get_ssn()}")  # Accessing private via getter method

    def __get_ssn(self):  # Private method can be accesed by 
        return f"***-**-{self.__ssn[-4:]}"  # Masked SSN


class Employee(Person):
    def __init__(self, name, age, ssn, employee_id, salary):
        super().__init__(name, age, ssn)   # Using super() to call parent constructor
        self.employee_id = employee_id     # Public attribute
        self._salary = salary              # Protected attribute

    def show_employee(self):
        print(f"\n[Employee Details]")
        self._display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self._salary}")
        print(f"{self._age}")
        print(f"{self.name}")
        # print(f"{self.__ssn}") # Private cannot be accessible


# Create an instance
emp = Employee("Rahul", 30, "123-45-6789", "E101", 90000)

# Accessing public member
print(emp.name)         # Accessible
print(emp.employee_id)  # Accessible

# Accessing protected member (should be avoided directly)
print(emp._age)         # Technically accessible, but not recommended
print(emp._salary)

# Trying to access private member directly
try:
    print(emp.__ssn)    # Will raise AttributeError
except AttributeError as e:
    print("\nAccessing private attribute raised error:", e)

# Using method to access private data
emp.show_employee()

# Statement2

class University():
    def __init__(self, name,email, id_number):
        self.name=name
        self._email=email
        self.__id_no=id_number

    def _get_member_details(self):
        return self.name, self._email
    
    def __generate_masked_id(self):
        return f"******- {self.__id_no[-1:-5:-1]}"
    
    def get_masked_id(self):
        return self.__generate_masked_id()

    
class Student(University):
    def __init__(self, name, email, id_number, student_id, cgpa,fees_due):
        super().__init__(name, email, id_number)
        self.student_id=student_id
        self._cgpa=cgpa
        self.__fees_due=fees_due

    def show_student_info(self):
        print("[Student Details]")
        print(self._get_member_details())
        print(self.student_id)
        print(self._cgpa)
        self.__getfees_due()

    def update_cgpa(self,new_cgpa):
        if int(new_cgpa)>=0 and int(new_cgpa)<=10:
            self.cgpa=new_cgpa

    def __getfees_due(self):
        return self.__fees_due


class Professor(University):
    def __init__(self, name, email, id_number, professor_id, salary, research_grants):
        super().__init__(name, email, id_number)
        self.professor_id=professor_id
        self._salary=salary
        self.__research_grants=research_grants

    def show_professor_info(self):
        print("[Professor Details]")
        self._get_member_details()
        self.professor_id
        self._salary
        self.__research_grant_amount()

    def increase_salary(self, percentage):
        self.__salary=int(self.__salary)+(percentage/100)

    def __research_grant_amount(self):
        return self.__research_grants
    
s=Student("Veer", "veer012@gmail.com", "1234550985","s1023-5","56", "120000")
s.show_student_info()
s.update_cgpa("25")
# s.fees_due()