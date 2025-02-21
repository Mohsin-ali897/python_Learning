#
#! A set in Python is an unordered, mutable, and unindexed collection of unique elements. Sets are commonly used when you need to store distinct values and perform operations like union, intersection, and difference efficiently.

#?? Creating a Set
s = {1,2,3,2,4,5} 
print(s)

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set
empty_set = set()  # Correct way (using {})
print(type(empty_set))  # Output: <class 'set'>

# Using set() with a list
list_to_set = set([1, 2, 2, 3, 4])
print(list_to_set)  # Output: {1, 2, 3, 4}


#! Properties of Sets
# Unordered: The elements do not maintain a specific order.
# Mutable: You can add or remove elements.
# No Duplicates: Duplicate values are automatically removed.
# Unindexed: You cannot access elements using an index.

duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print(duplicate_set)  # Output: {1, 2, 3, 4, 5}

#! Accessing Elements
#? Since sets are unordered, elements cannot be accessed by index. You can check if an element is present using in.

fruits = {"apple", "banana", "cherry"}

print("apple" in fruits)  # Output: True
print("mango" in fruits)  # Output: False

#! Adding Elements to a Set
#? add() – Adds a single element
fruits.add("mango")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'mango'}

#? update() – Adds multiple elements
fruits.update(["orange", "grape", "kiwi"])
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'mango', 'orange', 'grape', 'kiwi'}

#! Removing Elements from a Set
#? remove() – Removes an element (raises error if not found)
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'mango', 'orange', 'grape', 'kiwi'}

#? discard() – Removes an element (no error if not found)
fruits.discard("banana")  # No error if 'banana' is not present

    
