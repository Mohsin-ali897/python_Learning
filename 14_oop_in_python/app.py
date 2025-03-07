# import math
# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     #? now create a method to print average of marks
#     def avg_mark(self):
#         sum = 0
#         for value in self.marks:
#             sum = sum + value
#         # print(f'Hi, {self.name} you,r Average Score is {sum/len(self.marks)}')
#         print(f'Hi, {self.name} you,r Average Score is {sum/len(self.marks)}')
        
# s1 = student('name', [34,89,45,45,564])
# # print(s1.marks)
# print(s1.avg_mark())
# print(math.floor(231/13))
# print((231/13))
#! assignment to 
#? create a class called account with two attributes balaance and acccount number 
#? create method for credit, debt, and check balance
class account:
    def __init__(self, name, balance):
        self.Acc_name = name
        self.balance = balance
        
    #? method for credit 
    def credit_balance(self,deposit_amount ):
        self.balance += deposit_amount
        print(f'you Current balace is {self.balance}')
    #? method for check balance 
    # def debt_balance(self, debt):
    #     self.balance -= debt
    def debt_balance(self):
        debt = int(input('enter Ammount To Witdrawl'))
        self.balance -= debt
        print(f'\n you,r Total Balace After Withdrawl {self.balance}')
    #? method for  debt 
    def check_balance(self):
        return print(f'\n you,r Current Balance is {self.balance}')
my_acc = account('Mohsin Ali', 23000)
print(my_acc.Acc_name)
print(my_acc.balance)
my_acc.credit_balance(2000)
print(my_acc.balance)
my_acc.debt_balance()
print(my_acc.balance)
my_acc.check_balance()
print(my_acc.check_balance())




