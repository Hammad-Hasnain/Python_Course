# len() function is used to find the length of a list (i.e., the number of elements it contains), just like with strings.

fruits = ['apple', 'banana', 'cherry']
print(len(fruits))  # Output: 3



# ------------------------------ What if we try to find the length of a list using the index number ?? 🤔💭 ------------------------------
print(len(fruits[0]))  # Output: 5 (fruits[0] is 'apple' →  a string, so len('apple') = 5)
print(len(fruits[1]))  # Output: 6 
print(len(fruits[2]))  # Output: 6 
# print(len(fruits[3]))  # ❌err => IndexError: list index out of range 
