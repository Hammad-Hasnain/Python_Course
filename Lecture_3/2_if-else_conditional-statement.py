# Note: In Python, indentation (usually 4 spaces or 1 tab) defines code blocks and incorrect indentation will cause an IndentationError.

# `if-else` is a conditional statement in Python that allows the program to make a decision based on whether a condition is True or False.
# Syntax:
"""
if condition:
    #code block if condition is True
else:
    #code block if condition is False
"""

userAge = int(input('Enter your age.'))

if userAge >= 18:
    print("✅ Eligible")
else:
    print("❌ Not Eligible")
    