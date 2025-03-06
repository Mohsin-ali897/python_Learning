
#! import is used to bring external modules (built-in, third-party, or user-defined) into your script. This allows you to use pre-written functions, classes, and variables from other files without rewriting code. 

#? You can import a module using: 
import math  # Imports the entire math module
print(math.sqrt(16))  # Output: 4.0


#? Instead of importing the whole module, you can import only what you need but it is not recommended for absolute biggener bcz it is cause error 

from math import sqrt, pi
# print(sqrt(25))  # Output: 5.0
# print(pi)  # Output: 3.141592653589793

#? Importing with an Alias
import numpy as np
# arr = np.array([1,2,3,4])
# print(arr) 

#! Importing Everything (*) 
#? You can import all functions from a module, but it's not recommended (may cause naming conflicts).


from math import *
# print(sin(0))  # Output: 0.0


#! Importing a Custom (User-Defined) Module
import module_file  #* import user defined module
from module_file import greet, name
# module_file.greet() 
print(greet())
print(name)


