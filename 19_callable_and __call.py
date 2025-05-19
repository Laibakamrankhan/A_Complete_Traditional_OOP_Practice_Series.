#Create a class Multiplier with an **init**() to set a factor. 
#Define a **call**() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # store the multiplier factor

    def __call__(self, value):
        return value * self.factor

times1 = Multiplier(3)

print(callable(times1))  


result = times1(10)
print("10 multiplied by 3 is:", result)  
