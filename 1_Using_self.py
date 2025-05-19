#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. 
# Add a method display() that prints student details.

#creating Class
class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
#using display method
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.marks}")
#creating object
s1 = Student("laiba" , 90)
s1.display()
