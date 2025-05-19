#Create a class Employee with:
#a public variable name,
#a protected variable _salary, and
#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self , name , salary , ssn):
        self.name = name  #public
        self._salary = salary #protected
        self.__ssn = ssn #private
    

emp1 = Employee("Ali", 50000, "123-45-6789")

# Access public variable
print("Name:", emp1.name)         #Works 

# Access protected variable
print("Salary:", emp1._salary)    #Works but meant for internal use

# Access private variable
print("SSN:", emp1.__ssn)         #AttributeError: 'Employee' object has no attribute '__ssn'

