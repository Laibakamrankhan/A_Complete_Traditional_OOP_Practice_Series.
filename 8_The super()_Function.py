#Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person :
    def __init__(self , name):
        self.name = name

class Teacher(Person):
    def __init__(self, name , subject ):
        self.subject = subject
        super().__init__(name)
    def show(self):
        print(f"Teacher Name: {self.name}  Subject: {self.subject}")
 
Teacher1 = Teacher("youtube" , "All subject")
Teacher1.show()