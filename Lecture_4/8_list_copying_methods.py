# Python method for copying list
"""
Rules:
  → Immutable elements (like numbers, strings) are safely copied
  → Mutable elements (like lists, dicts) are shared, not duplicated
"""
# copy() :  creates a shallow copy of a list.
#  With Immutable Elements
a = [1, 2, 3]
b = a.copy()
b[0] = 100
print(a)  # Output: [1, 2, 3] 
print(b)  # Output: [100, 2, 3]

#  With Mutable Elements (Shallow Copy Problem)
a = [[1, 2], 3, 4]
b = a.copy()
b[0][0] = 999
print(a)  # Output:  [[999, 2], 3, 4]  changed
print(b)  # Output:  [[999, 2], 3, 4]



#  --------- Deep Copy via copy Module --------- 
import copy

a = [[1, 2], 3, 4]
b = copy.deepcopy(a)
b[0][0] = 999

print(a)  # [[1, 2], 3, 4]  unchanged
print(b)  # [[999, 2], 3, 4]