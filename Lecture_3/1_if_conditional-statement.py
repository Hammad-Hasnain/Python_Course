# Note: In Python, indentation (usually 4 spaces or 1 tab) defines code blocks and incorrect indentation will cause an IndentationError.

# `if` is a conditional statement that allows the program to take a decision when a condition is fulfilled (True).
# Syntax:
"""
if condition:
    code block if condition is True
"""

age = 22

# Way 1: With parentheses (optional in Python)
if (age > 18):
    print(age)  # Output: 22

# Way 2: Without parentheses (cleaner and more Pythonic)
if age > 18:
    print(age)  # Output: 22

# Way 3: One-liner (not recommended for multi-line blocks)
if age > 18: print(age)  # Output: 22


# ------------------------------ What if we compare string with number  ?? 🤔💭 ------------------------------
"""
age2 = '22'
if age2 > 18 : print('Eligible for vote') # err => TypeError: '>' not supported between instances of 'str' and 'int'
"""

# ------------------------------ Let's take user age for comparison  🤔💭 ------------------------------

# Way 1 – Convert input directly inside int() and use it
userAge = int(input("Enter your age: "))  # input() returns string; int() converts it to integer
if userAge > 18:
    print("Eligible for vote")  # Output: 'Eligible for vote' if condition is True

# Way 2 – Store input first, then convert in a separate step
userAge = input("Enter your age again: ")
convertedUserAge = int(userAge)
if convertedUserAge > 18:
    print("Eligible for vote")  # Output: 'Eligible for vote' if condition is True
