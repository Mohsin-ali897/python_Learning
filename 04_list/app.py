
#! list
#? A list in Python is a collection data type that is ordered, mutable (changeable), and allows duplicate elements. Lists can store elements of different types, including integers, floats, strings, and even other lists.
fruits = ["apple", "banana", "cherry"]
#? accessing element 
# print(fruits[0])   # Output: apple
# print(fruits[-1])  # Output: cherry

#! Slicing
#? You can retrieve a subset of elements using slicing. 
numbers = [10, 20, 30, 40, 50, 60]

# num = numbers[:4]
# print(num[:2]) 

# print(numbers[1:4])   # Output: [20, 30, 40]  (Index 1 to 3)
# print(numbers[:3])    # Output: [10, 20, 30]  (Start to index 2)
# print(numbers[2:])    # Output: [30, 40, 50, 60] (Index 2 to end)
# print(numbers[::2])   # Output: [10, 30, 50]  (Step of 2)
# print(numbers[::-1])  # Output: [60, 50, 40, 30, 20, 10] (Reverse list)

#! Modifying a List
#? Since lists are mutable, you can modify them.
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
# print(fruits)  # Output: ['apple', 'orange', 'cherry']


#! Adding Elements  
#? append() – Add element at the end
fruits.append('mango')
# print(fruits) 

#? 2. insert() – Add element at a specific position
# fruits.insert(1,'abc') 
# print(fruits)

#? extend() – Merge another list
# fruits.extend(['xyz', 'abc']) 
# print(fruits)


#! Removing Elements
#? remove() – Removes first occurrence of an element
fruits.remove("orange")
print(fruits)  #? Output: ['apple', 'grape', 'cherry', 'mango', 'pineapple', 'papaya']

#? pop() – Removes and returns element at given index (default: last)
# last_fruit = fruits.pop()
# print(last_fruit)  #? Output: papaya
# print(fruits)      #? Output: ['apple', 'grape', 'cherry', 'mango', 'pineapple']


specific_fruit = fruits.pop(2)
print(specific_fruit)  #? Output: cherry
print(fruits)          #? Output: ['apple', 'grape', 'mango', 'pineapple']

#? del – Deletes an element or entire list
del fruits[1]
print(fruits)  #? Output: ['apple', 'mango', 'pineapple']

del fruits     #? Deletes the entire list

#! Sorting and Reversing
#? sort() – Sorts list in place
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  #? Output: [1, 2, 5, 5, 6, 9]

#? Sorting in descending order:
numbers.sort(reverse=True)
print(numbers)  #? Output: [9, 6, 5, 5, 2, 1]


#? sorted() – Returns a sorted copy
numbers = [5, 2, 9, 1, 5, 6]
new_sorted_list = sorted(numbers)
print(new_sorted_list)  # Output: [1, 2, 5, 5, 6, 9] 

#? reverse() – Reverses list in place
numbers.reverse()
print(numbers)  #? Output: [6, 5, 5, 9, 2, 1]

#! List Comprehension
#? List comprehension provides a concise way to create lists.
square_list = [x**2 for x in range(10)]
print(square_list)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  #? Output: [0, 2, 4, 6, 8]

