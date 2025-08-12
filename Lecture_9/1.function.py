# Function is a block of code or statements that can be used again and again without code redundancy.
"""
Two types of functions:

1. Built-in Functions:
   - Predefined in Python.
   - Can be used directly without defining them.
   - Examples: print(), len(), type(), range(), input(), int(), etc.

2. User-defined Functions:
   - Created by the programmer using the `def` keyword.
   - Used to perform custom or repetitive tasks.
   - Example:

     def function_name(parameters):
    # function body (code block)

"""

# 1. Built-in functions are defined in the sibling folder



# 2. User-define funtion
# -------- without paramaters -------- 
def greet():
    print("Hello, World!")

# Calling the function
greet() 
greet() 
greet() 


# -------- with paramaters -------- 
def sum_func(a,b):
    sum = a + b
    print("Sum is:", sum)

# sum_func()  # TypeError: sum_func() missing 2 required positional arguments: 'a' and 'b'
sum_func(5,10)  # Output: 15

result = sum_func(5,10)  # Output: 15 
print(result)  # Output: None


# -------- with parameters and return value -------- 
def sum_func_2(a,b):
    sum = a + b
    print("Sum is:", sum)
    return sum

result2 = sum_func_2(5,10)  # Output: Sum is: 15 
print(result2)  # Output: Sum is: 15


# -------- with default parameters and return value -------- 
def sum_func_3(a, b=5):
    sum = a + b
    print("Sum is:", sum)
    return sum

sum_func_3(2)  # Output: Sum is: 7
