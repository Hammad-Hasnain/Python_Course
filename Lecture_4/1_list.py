# List is a versatile and commonly used `built-in` data type that allows you to store a collection of items in a single variable.
# Key characterstics: Ordered, mutable, allows duplicate values, can contain any data type(Heterogeneous). 
# +ve indexes  start from 0 to nth (left-right)
# -ve indexes  start from nth to -1 (right-left)

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list with mixed data types
mixed_list = ["hello", 10, True, 3.14]

print(numbers)  # Output: [1, 2, 3, 4, 5]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(mixed_list)  # Output: ['hello', 10, True, 3.14]



# Accessing List Items
# +ve indexes 
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

# -ve indexes 
print(fruits[-1])  # Output: cherry

# if index is out of range 
# print(fruits[9])  # ❌err => IndexError: list index out of range



# Modifying List Items
fruits[0] = 'orange'
print(fruits) # Output: ['orange', 'banana', 'cherry']