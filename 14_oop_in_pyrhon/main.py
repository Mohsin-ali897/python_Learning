
#! object oriented programming
#?  class and instance are fundamental concepts in Object-Oriented Programming (OOP).
#? Class:
#* A class is a blueprint for creating objects.    
#* It defines attributes (variables) and methods (functions) that the objects created from the class will have.

# class Student:
#     name = 'elbert Einstein',
#     age = 24



#? instance:
#* An instance (or object) is an individual entity created from a class.
#* It has its own unique values for the attributes defined in the class. 

# s1 = Student()
# print(s1.name)
# print(s1.age)


#? constructor
#* A constructor is a special method in a class that is automatically called when a new instance (object) of the class is created. In Python, the constructor is defined using the __init__() method.  

#? Purpose of a Constructor:
#* Initializes the attributes of the object.
#* Ensures that an object has the necessary properties when it is created.
#* Can take arguments to assign values to instance variables.

class Cars():
    def __init__(self, model='v8 series', color='blue',name='unknown'):
        print('hello I,am a Car construtor')
        self.name = name
        self.model = model
        self.color = color

toyota = Cars()
toyota1 = Cars('v12','red', 'Buggati')
print(toyota.model)
print(toyota1)
print(type(toyota1))
