
#! Rising custom error 
#? In Python, you can raise a custom error using the raise keyword along with a custom exception class that inherits from Python’s built-in Exception class. 
# x = int(input('enter the number:'))
# if (x < 9 and x > 2 ):
#     print(x)
# else:
#     raise ValueError('number should between 2 to 9') 


name = input('enter the name:')
if(name=='quit'):
    print(f'you are enter {name}')
else:
    raise ValueError(f'you are entered {name}')