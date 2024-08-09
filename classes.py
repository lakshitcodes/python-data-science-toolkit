# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it.Almost everything in python is object.


# Create class
class User:
    # Constructor
    def __init__(self, name,email,age):
        self.name = name
        self.email = email
        self.age=age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age+=1

# Extend class
class Customer(User):
    #Constructor
    def __init__(self,name,email,age):
        self.name=name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self,amount):
        self.balance= amount

# Init Object
lakshit = Customer("Lakshit Jain","lakshit@mail.com",20)

lakshit.has_birthday()
lakshit.setBalance(300)
print(lakshit.balance)
