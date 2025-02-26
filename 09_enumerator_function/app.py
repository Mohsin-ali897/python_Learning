
#! emumerator function 
#? What Does Enumerate Do in Python? 
#* Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop. This enumerate object contains a count (from the start, which always defaults to 0) and a value obtained from iterating over the iterable object.


marks = [12,23,34,56,78,89,24]
#? simple method 
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print('56 is founded')
#     index += 1 

#? by using enumerator function
# for ind, mark in enumerate(marks):
#     print(mark)
#     if(ind == 3):
#         print(f'the 56 is found in index {ind}')
#? for changing the enumerate functionn starting point
# enumerate(marks, start=0) 

num = enumerate(marks, start=0) 
print(num)