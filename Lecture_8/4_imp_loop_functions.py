# There are 3 most commonly used built-in function that are used in loops.
"""
1. len() 
2. range() : 
3. enumerate() :
"""

# 1. len() : returns the lenght of iterables i.e list, string, etc. 
# Covered before.


# 2. range(start=0, stop*, step=1) : returns an iterable of numbers from start to stop (excluding stop). Commonly used for looping a spec no. of times. 
print( range(5))   # Output: range(0, 5)
print( range(2, 7))   # Output: range(2, 7)
print( range(0, 10, 2))   # Output: range(0, 10, 2)

# Above outputs can be directly iterate but this is the more pure version of outputs we got by `Type Casting`
print(list(range(5)))         # Output: [0, 1, 2, 3, 4]
print(list(range(2, 7)))      # Output: [2, 3, 4, 5, 6]
print(list(range(0, 10, 2)))  # Output: [0, 2, 4, 6, 8]

# for loop example
for i in range(5):
    print(i)

# Output: 0
#         1
#         2
#         3
#         4



# 3. enumerate(iterable*, start=0) : lets us loop over a sequence while keeping track of the index, returning pairs of index and value as an enumerate object 
fruits = ["apple", "banana", "cherry"]

print(enumerate(fruits))  # Output: <enumerate object at 0x0000024AB4DE9C10>
print(list(enumerate(fruits)))  # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

for index, fruit in enumerate(fruits):
    print(index , fruit)

# Output: 0 apple
#         1 banana
#         2 cherry
