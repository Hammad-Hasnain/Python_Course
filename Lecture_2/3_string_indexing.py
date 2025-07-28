# Index is the position of each character in string. Starts with 0. i.e.
# 0 = H
# 10 = d

text = 'Hello World'

"""
print(text[0])  # H
print(text[1])  # e
print(text[2])  # l
print(text[3])  # l
print(text[4])  # o
print(text[5])  # (space)
print(text[6])  # w
print(text[7])  # o
print(text[8])  # r
print(text[9])  # l
print(text[10]) # d
"""

# ------------------------------ What if we keep [] it as it is ?? 🤔💭 ------------------------------
# print(text[]) # err => syntax error



# ------------------------------ What if we pass -ve index to [] ?? 🤔💭 ------------------------------
# last char is always at index -1 i.e.
# -1 = d
# -2 = l
# .. .. ..
# -11 = H

"""
print(text[-11])  # H
print(text[-10])  # e
print(text[-9])   # l
print(text[-8])   # l
print(text[-7])   # o
print(text[-6])   # (space)
print(text[-5])   # W
print(text[-4])   # o
print(text[-3])   # r
print(text[-2])   # l
print(text[-1])   # d
"""


# ------------------------------ Can I replace a character in a string using direct indexing like text[5] = '-'? 🤔💭 ------------------------------
"""
text[5] = "-"
print(text) # err => TypeError: 'str' object does not support item assignment
"""