# `recursion` is a programming technique where a function calls itself to solve a problem
"""
Two main parts:
1. Base Case: This is the condition that stops the recursion.
2. Recursive Step: This is where the function calls itself
"""

def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive step
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120