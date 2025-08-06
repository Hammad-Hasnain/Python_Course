# Python methods for modifyng order of elements/items

# 1. reverse() : reverses the original list. 
numbers = [10, 20, 30, 40, 50]

numbers.reverse()
print(numbers)



# 2. sort(reverse=False) : 
numbers = [4, 2, 8, 1, 6]

numbers.sort()
print(numbers) # Output: [1, 2, 4, 6, 8]

# Sorting in Descending Order
numbers.sort(reverse=True)
print(numbers) # Output: [8, 6, 4, 2, 1]

# For strings:
words = ["banana", "apple", "cherry", "date"] 
words.sort() 
print(words) # Output: ['apple', 'banana', 'cherry', 'date']

# Custom Sorting with the key Parameter, syntax: list.sort(key=function)
# ---------- Sorting with key:Built-in functions ----------  
words.sort(key=len)
print(words)

names = ['Anna', 'bob', 'Charlie']
# Case-sensitive sort
names.sort()  
print(names) # Output: ['Anna', 'Charlie', 'bob']
# Case-insensitive sort
names.sort(key=str.lower) # Output: ['Anna', 'bob', 'Charlie']
print(names)


# ---------- Sorting with key:Lambda functions ---------- 
# ---------- Sorting with key:User-define functions ---------- 
