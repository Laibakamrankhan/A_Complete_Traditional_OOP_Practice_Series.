#Create a class Engine and a class Car. Use composition by passing an 
#Engine object to the Car class during initialization. Access a method of the Engine class via the Car class

class Engine:
    def start(self):
        print("Engine is starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine  

    def start_car(self):
        print("Car is ready to start.")
        self.engine.start()  # Access Engine's method via Car


my_engine = Engine()
my_car = Car(my_engine)
my_car.start_car()
