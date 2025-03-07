
#! object oriented programming
#?  class and instance are fundamental concepts in Object-Oriented Programming (OOP).
#! Class:
#* A class is a blueprint for creating objects.    
#* It defines attributes (variables) and methods (functions) that the objects created from the class will have.

# class Student:
#     name = 'elbert Einstein',
#     age = 24



#! instance OR object:
#* An instance (or object) is an individual entity created from a class.
#* It has its own unique values for the attributes defined in the class. 

# s1 = Student()
# print(s1.name)
# print(s1.age)


#! constructor
#* A constructor is a special method in a class that is automatically called when a new instance (object) of the class is created. In Python, the constructor is defined using the __init__() method.  

#? Purpose of a Constructor:
#* Initializes the attributes of the object.
#* Ensures that an object has the necessary properties when it is created.
#* Can take arguments to assign values to instance variables.

class Cars():
    manufactura = 'Made by Japan' #? it is a same data for all cars so we can store it as a class attribute so it can not occupied space for every single object (instance) creatine time
    def __init__(self, model='v8 series', color='blue',name='unknown'):
        print('hello I,am a Car construtor')
        self.name = name
        self.model = model
        self.color = color
    
    #! Method in classes
    #*  Object-Oriented Programming (OOP) in Python, a method is a function that is defined inside a class and operates on instances of that class. There are three main types of methods in Python OOP:
    #! Instance Method
    #* Operates on an instance of the class.
    #* The first parameter is always self, which refers to the instance.
    #* Can access and modify instance attributes.
    
    #? it is a method of a class 
    def car_model(self):
        print(f'The model of a Car is {self.model}')
    
    #! static method
    #*A static method is a method inside a class that does not depend on instance variables (self) or class variables (cls). It behaves like a regular function but is logically related to the class.  
    @staticmethod
    def greet():
        print(f'hello Dear Customer how are you')
    
    #? Key Features of Static Methods
    #* ✅ Does not modify the instance (self) or class (cls).
    #* ✅ Defined using the @staticmethod decorator.
    #* ✅ Can be called on the class itself or an instance.
    #* ✅ Typically used for utility functions related to the class. 
    
    
    
    
    #! private Method
    #? A private method in Python is a method that is intended to be used only within the class and not accessible directly from outside the class.
      

   

toyota = Cars()
toyota1 = Cars('v12 Series','red', 'Buggati')
# print(toyota.model)
# print(toyota1.manufactura)
model = toyota1.car_model()
print(model)
# print(type(toyota1))

#! private attribute
#? A private attribute in Python is an attribute (variable) that is intended to be used only within the class and cannot be accessed directly from outside the class. 

class Account:
    def __init__(self, account, password):
        self.__password = password
        self.account = account
    def reset_pass(self):
        print(self.__password)
        new_pass = str(input('Enter New password'))
        self.__password = new_pass
        print(self.__password)

#* ✔ Private attributes start with __ (double underscore).
#* ✔ They cannot be accessed directly outside the class.
#* ✔ They can be accessed using name mangling (_ClassName__attribute), but this is not recommended.
#* ✔ Use getters and setters to safely access and modify private attributes.
#* ✔ Encapsulation helps protect sensitive data and maintain control over class properties.
#* Would you like to explore encapsulation or another OOP concept further? 🚀


acc1 = Account('Mohsin Ali', '12345')
print(acc1.account)
# print(acc1.reset_pass())


#! Use Case of Private Attributes 
#  Encapsulation – Prevents direct modification of sensitive data.
# 🔹 Security – Protects critical attributes from accidental changes.
# 🔹 Data Validation – Ensures controlled access via getter/setter methods.


#? For Example 
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.__balance}")
#         else:
#             print("Invalid deposit amount!")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
#         else:
#             print("Invalid withdrawal amount!")

#     def get_balance(self):  # Getter method
#         return self.__balance

# # Creating an object
# account = BankAccount(1000)
# account.deposit(500)  # ✅ Works
# account.withdraw(200)  # ✅ Works

# # print(account.__balance)  # ❌ AttributeError: 'BankAccount' object has no attribute '__balance'
# print(account.get_balance())  # ✅ Works (Accessing private attribute safely)





