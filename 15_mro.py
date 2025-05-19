#Create four classes:
#A with a method show(),
#B and C that inherit from A and override show(),
#D that inherits from both B and C.
#Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("Show method in A")

class B(A):
    def show(self):
        print("Show method in B")

class C(A):
    def show(self):
        print("Show method in C")

class D(B, C):
    pass

d = D()
d.show()
print(D.mro())

