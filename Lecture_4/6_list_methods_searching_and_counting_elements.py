# Python methods for searching and counting elements/items
"""
 Rules:
   index(): valid range → start < stop  &  searches forward only
"""

# 1. index(element, start=0, end=len(list)) :  returns the position of the first occurrence of a specified value.
numbers = [10, 20, 30, 20, 40] 
index = numbers.index(20) 
print(index)  # Output: 1

# negative indexes
index2 = numbers.index(20,-6,-1)  # Output: 1

# if value isn't found
# index2 = numbers.index(20,-6,-1)  #❌er=> ValueError: 3 is not in list



# 2. count(value) :   returns the number of times a specified value appears in a list otherwise 0.
mixed_list = [1, "apple", True, "apple", 1] 
count_apple = mixed_list.count("apple")
print(count_apple)  # Output: 2