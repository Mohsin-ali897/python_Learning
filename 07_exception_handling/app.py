
#! handling error in python 
#? we can use ecception error handling in python by using python
# x = input('Enter the number you want to print table:')
# try:
#     print(f'the Number you type {x}')
#     for i in range(1,11):
#         print(f'{x} X {i} = {int(x)*i}')
# except Exception as e:
#     print(f'the error is {e}')
#     print(e)
# except ValueError as ve:
#     print(ve)

#* we can handle multiple error using exception handling
# try:
#     x = input('enter the index number:')
#     a = [23,45,67,89]
#     print(a[int(x)])
# except Exception as e:
#     print('the error is',e)
# except IndexError as ie:
#     print('the error is',ie)
    
#* finally keyword is always executed whether try or catch block is executed or not and it is always irrespected return keyword
def num():
    try:
        x = input('enter the number:')
        y = [11,22,33,44,55,]
        print(y[int(x)])
        return 'try block is executed'
    except IndexError as ie:
        print(ie)
        return 'except block is executed'
    # #? in this case following print statement is not executed because of return keyword in these case we can use finally keyword to exceute specific line of code or operation function is return or not exp given below 
    # print('code running successfully')
    finally:
        print('code running successfully')
        
res = num()
print(res)
