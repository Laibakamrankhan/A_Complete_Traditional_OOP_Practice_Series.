#Create a class Product with a private attribute _price.
#Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  
    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            print("Setting price...")
            self._price = value
        else:
            print("Price cannot be negative.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price
p = Product(100)
print(p.price)  

p.price = 150    # Setting price...

p.price = -10    # Price cannot be negative.

del p.price      # Deleting price...
