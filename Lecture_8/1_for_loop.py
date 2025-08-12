# A `for` loop iterates over a sequence (like a list, tuple, set, dictionary, or string), executing a block of code once for each item.
# Syntax: 
"""
for item in sequence:
    # code to be executed for each item
"""

# 1. Iterating over List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple
#         banana
#         cherry



# 2. Iterating over String
for letter in "Python":
    print(letter)
# Output: P
#         y
#         t
#         h
#         o
#         n



# 3. Iterating over Tuple
numbers = (1, 2, 3)
for num in numbers:
    print(num)
# Output: 1
#         2
#         3



# 4. Iterating over Set
colors = {'red', 'green', 'blue'}
for color in colors:
    print(color)

# Output: red  (order may vary)
#         green
#         blue



# 5. Iterating over Dictionary
person = {'name': 'Alice', 'age': 30}

# --------- Loop through keys --------- 
for key in person:
    print(key)

# Output: name
#         age


# --------- Loop through values --------- 
for value in person.values():
    print(value)

# Output: Alice
#         30


# --------- Loop through key-value pairs --------- 
for item in person.items():
    print(item)

# Output: ('name', 'Alice')
#         ('age', 30)



#  *** for with else clause