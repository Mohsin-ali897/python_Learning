
#! global and local variable 
#? Global variable
#? A variable decleared in a parent scope is called global variable and child can also access within it their scope 
#? Local Variable
#? A variable decleared in a child scope is called local variable and parent can not access within it their scope 

x = 10
def greet():
    #? The global keyword in Python is used to modify a variable that is defined outside the current function's scope. It allows functions to update global variables instead of creating local ones.
    global x 
    x = 30
    # print(x)

greet()
print(x)

x = 10  # Global variable

def update_x():
    global x  # Declare x as global
    x = 20    # Modify the global variable
    print("Inside function, x =", x)

update_x()
print("Outside function, x =", x)










