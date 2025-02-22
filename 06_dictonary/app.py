student_detail:dict = {
    "name":'mohsin ali',
    'fName':'abdul majeed',
    'roll num':355900,
    'is_student':True
}
# print(student_detail['is_student'])
#? if you want your programme not throw error if value is not found so use this method 
print(student_detail.get('class'))
#? otherwise this method is used to get value of a specific  
# print(student_detail['class'])
# for key in student_detail.keys():
#     # print(f'the corresponding value of a keys {key} is {student_detail[key]}')
#     pass
# for value in student_detail.items():
#     print(value)

ep1 = {
    1:11,
    2:22,
    3:33,
    4:44
}
ep2={
    5:55,
    6:66
}
ep1.update(ep2)
# print(ep1.items())
# print(type( ep1.items()))

#! for remove item
#? for delete one specific item 
# ep1.pop(3)
#? for deleting  items from end of a dictionary
# ep1.popitem() 
# print(ep1)

#? for removing all key values pairs in dictionary
# ep1.clear()
# print(ep1) 








