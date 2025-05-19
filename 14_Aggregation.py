#Create a class Department and a class Employee. 
#Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # Will hold references to Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Department: {self.dept_name}")
        for emp in self.employees:
            print(f"- Employee: {emp.name}")

emp1 = Employee("Ali")
emp2 = Employee("Sara")

dept = Department("IT")

dept.add_employee(emp1)
dept.add_employee(emp2)

dept.show_employees()
