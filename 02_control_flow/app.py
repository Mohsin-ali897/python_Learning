# name = ['mohsin', 'ahmed', 'baksh']
# for name in name:
#     print(f'hello how are you {name}')

# a = 1
# while a < 10:
#     print(f'a is {a}')
#     a += 1
    
#! printing table  
# for i in range(1,11):
#     print(f'''
# ============== Table of {i} ==========
#           ''')
#     for j in range(1,11):
#         print(f'''     {i} X {j} = {j*i} ''')

#! searching number in tuple
# num = (1,23,45,67,78,89,90,43,27) 
# x = 45
# ind = 0
# print(len(num))
# while ind < len(num):
#     if num[ind] == 27:
#         print(f'Number is find in index {ind}')
#         break
#     else:
#         print(f'number {x} is not found {ind}')
#     # print(ind)
#     ind += 1
#! continue keyword in loops
# i = 0
# while i < 7:
#     if i == 3:
#         i += 1
#         continue  # it is used to skip the current iteration
#     print(i)
#     i += 1
# name = 'mohsin ali'
# for char in name:
#     print(char)

#! build a function to generate a giving argument table from 1 to 20
# def table_generator(table:int, str:int, end:int):
#     for i in range(str,end):
#         print(f'{table} X {i} = {table*i}')
# table_generator(2, 5, 10)   
#? in range function we have three arguments range(start?, end, step?)
# for i in range(1,23,2):
#     print(i)
#! pass statement in python
#? pass is a null statement that does anything and used as a placeholder for future code
# for j in range(1,10): #? for exaple
#     pass
# print('hello')
#? question solving WAP that print a sum of natural number using loop
n = 5
sum = 0
i = 0
while i <= n:
    sum += i
    i +=1
print(f'sum of {n} = {sum}')
#? question solving WAP that print a factorial of natural number using loop
n = 5
sum = 1
i = 1
while i <= n:
    sum *= i
    i +=1
print(f'sum of {n} = {sum}')

#? for loop with else statement  
for i in range(5):
    if (i == 3):
        print(i)
else:
    print('i is not found')
    
#! shortHand if else statement 
a = 20,
b = 20,
print('a is greater than b') if a > b else print('b is greather than a') if b > a else print('a is equal to b') if a == b else print('all condition is not satisfied')

num1 = 20,
num2 = 30,
num3 = 10
# print('num1 is bigger than num2') if num1 > num2 else ''
# print('num1 is bigger than num2') if num1 > num2 else print('hello') if num2 > num1 else ''
num3 = 200 if num1 > num2 else num3
print(num3)

