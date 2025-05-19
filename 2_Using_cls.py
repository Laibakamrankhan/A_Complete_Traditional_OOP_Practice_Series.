#Create a class Counter that keeps track of how many objects have been created. 
#Use a class variable and a class method with cls to manage and display the count.

class Counter:
    #variable to keep track of object count
    count = 0

    def __init__(self):
        #Increment the class variable 
        Counter.count += 1

    @classmethod
    def show_count(cls):
        # Class method to display the current count
        print(f"Total objects created: {cls.count}")

a = Counter()
b = Counter()

Counter.show_count()