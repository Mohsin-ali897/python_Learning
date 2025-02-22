fruite_set = {'apple', 'banana','apple', 'cherry', 'mango', 'orange', 'grape', 'kiwi'}
# num = set(1, 2, 2, 3, 4)
# num_set = set({1,3,5,2,3,2})
# print((num_set))
# print(set)
s1 = {1,2,3}
s2 = {3,4,5}
# print(s1.union(s2))
# print(s1)
# print(s1.intersection(s2))

# s1.update(s2)
s3 = s1.difference_update(s2)
# print(s3)
# print(s1)

cites = {'Lagos', 'Abuja', 'Kano', 'Kaduna', 'Port Harcourt', 'Ibadan'}
cites1 = {'Lagos', 'Abuja', 'Kano', 'Kaduna', 'Port Harcourt', 'Ibadan', 'Enugu', 'karachi', 'Lahore'}
# cites3 = cites.symmetric_difference(cites1)
cites3 = cites.symmetric_difference_update(cites1)
# print(cites.difference(cites1))
# print(cites3)
# print(cites1.union(cites))