#def-return-class.py
#def: It is used to define a function in Python.

#return: It is used within a function to specify the value that the function should return.

#class: It is used to define a class, which is a blueprint for creating objects in object-oriented programming.

# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Using the function
result = greet("Alice")
print(result)

# Defining a class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

# Creating an instance of the class
my_dog = Dog("Buddy", "Labrador")

# Accessing class attributes and methods
print(f"My dog's name is {my_dog.name} and it says {my_dog.bark()}.")
