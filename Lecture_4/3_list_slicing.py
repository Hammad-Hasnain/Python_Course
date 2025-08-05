# `List slicing` is a powerful feature that allows you to access or extract a portion (a "slice" or sublist) of a list.
# Syntax:
#       list_name[start:stop:step]
"""
Parameters:
*   start: The index where the slice begins (inclusive). If omitted, it defaults to the beginning of the list (index 0).
*   stop: The index where the slice ends (exclusive). This means the element at this index is **not** included. If omitted, it defaults to the end of the list.
*   step: An optional number indicating the interval between elements. The default is 1, meaning every element is included.

Rules:
*   start < stop is needed for positive steps (forward: L → R )
*   start > stop is needed for negative steps (backward L ← R )
"""

# A sample list
# +ve →      0         1         2        3        4
fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']
# -ve →     -5        -4        -3       -2       -1


# *** Basic Slicing ***
# Slicing from index 1 to 3 (excluding 4)
print(fruits[1:4])  # Output: ['banana', 'cherry', 'mango']

# Slice from start to index 2 or omit starting index 
print(fruits[:3])  # Output: ['apple', 'banana', 'cherry']

# Slice from index 2 to end or omit ending index 
print(fruits[2:])  # Output: ['cherry', 'mango', 'grape']

# Full slice (copy of list)
print(fruits[:])  # Output: ['apple', 'banana', 'cherry', 'mango', 'grape']

# Slice with negative indexes
print(fruits[-3:-1])  # Output: ['cherry', 'mango']



# *** Slicing with a Step ***
print(fruits[::2])     # ['apple', 'cherry', 'grape'] → every 2nd item
print(fruits[1:4:2])   # ['banana', 'mango'] → every 2nd item from index 1 to 3

print(fruits[-2:-5:1]) # Output: []
print(fruits[-2:-5:-1]) # Output: ['mango', 'cherry', 'banana']


#   Reversing a list using slicing
print(fruits[::-1])  # Output: ['grape', 'mango', 'cherry', 'banana', 'apple']