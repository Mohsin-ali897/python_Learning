
#! Define a function power(base, exponent=2) that returns the base raised to the power of the exponent. If no exponent is provided, it should return the square of the base.

# def power(base:int, exponent=2):
#     return base ** exponent
# num1 = power(2,3)
# print(num1)
#! Write a function calculate(a, b) that returns the sum, difference, product, and quotient of two numbers.

# def calculate(a,b):
#     sum = a+b;
#     difference = a-b;
#     product = a*b;
#     quotation = a // b
#     print(f'the sum of {a} and {b} = {sum} \n, the difference of {a} and {b} = {difference} \n')
# result = calculate(12,45)
# print(result)
#! Implement a recursive function factorial(n) that returns the factorial of a given number n.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     res = n * factorial(n - 1)
#     return res
# fac2 = factorial(5)
# print(fac2)

#! lumda function
#? A lambda function in Python is an anonymous, single-line function that can take any number of arguments but has only one expression.
# square = lambda a: (a**5) 
# print(square(2)) 