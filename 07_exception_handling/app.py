
#! handling error in python 
#? we can use ecception error handling in python by using python
x = input('Enter the number you want to print table:')
try:
    print(f'the Number you type {x}')
    for i in range(1,11):
        print(f'{x} X {i} = {int(x)*i}')
except Exception as e:
    print(f'the error is {e}')
    print(e)
    
