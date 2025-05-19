#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name.
#Show that it affects all instances.

class Bank:
    # Class variable (shared by all objects)
    bank_name = "International Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    # Show account info
    def show_info(self):
        print(f"{self.account_holder} has an account at {Bank.bank_name}")


acc1 = Bank("Ali")
acc2 = Bank("Ayesha")

acc1.show_info()   
acc2.show_info()  

# Change the bank name
Bank.change_bank_name("National Bank")


acc1.show_info()   
acc2.show_info()   
