
# #! =============== Kon bana Ga Crorepati ============
# #? it is a simple price winning game  
# questions = [
#     [
#         'Who is the founder of Facebook',
#         'Elon Mask', 'Bill Gates', 'Jaff Bezos', 'Mark Zecharburge'
#     ],
#     [
#         'Who is the founder of Facebook',
#         'Elon Mask', 'Bill Gates', 'Jaff Bezos', 'Mark Zecharburge'
#     ],
#     [
#         'Who is the founder of Facebook',
#         'Elon Mask', 'Bill Gates', 'Jaff Bezos', 'Mark Zecharburge'
#     ],
#     [
#         'Who is the founder of Facebook',
#         'Elon Mask', 'Bill Gates', 'Jaff Bezos', 'Mark Zecharburge'
#     ],
#     [
#         'Who is the founder of Facebook',
#         'Elon Mask', 'Bill Gates', 'Jaff Bezos', 'Mark Zecharburge'
#     ],
#     [
#         'Who is the founder of Facebook',
#         'Elon Mask', 'Bill Gates', 'Jaff Bezos', 'Mark Zecharburge'
#     ],
#     [
#         'Who is the founder of Facebook',
#         'Elon Mask', 'Bill Gates', 'Jaff Bezos', 'Mark Zecharburge'
#     ],
#     [
#         'Who is the founder of Facebook',
#         'Elon Mask', 'Bill Gates', 'Jaff Bezos', 'Mark Zecharburge'
#     ],
# ] 

# level = [1000,2000,4000,8000,16000,32000,64000,128000]
# money = 0
# # print(questions[0])
# for i in range(1,len(questions)):
#     question = questions[i]
#     print(f'The Question no:{i} for Rs:{level[i]} \n\n {question[0]} \n\n {question[1]}\n\n {question[2]}\n\n {question[3]} \n\n {question[4]}')
#     answer = input('Enter Your Answer :')
#     # print(i)
#     if(answer == question[4]):
#         print(f'congratulation Your Answer is correct \n and you Won {level[i]} Ruppess\n')
#         money = level[i]
#         print(f'your Save Go Home money is Rs: {money}\n')
#         continue
#     elif (answer != question[-1]):
#         print(f'Sorry Your Answer is Wrong')
#         break
# print(f'Your Winning Ammount is Rs:{money}')
