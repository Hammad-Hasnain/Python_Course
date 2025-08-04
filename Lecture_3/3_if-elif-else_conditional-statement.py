# Note: In Python, indentation (usually 4 spaces or 1 tab) defines code blocks and incorrect indentation will cause an IndentationError.

# if-elif-else is a conditional control structure in Python that allows the program to make decisions based on multiple conditions.
# The if block runs if the first condition is True.
# The elif (short for "else if") block runs if its condition is True and all previous conditions were False.
# The else block runs if none of the above conditions are True.
# Syntax:
"""
if condition1:
    # code block if condition1 is True
elif condition2:
    # code block if condition2 is True (only if condition1 is False)
else:
    # code block if all above conditions are False

"""

userAge = int(input('Enter your age: '))

if userAge < 0:
    print("⚠️ Invalid age")
elif userAge >= 18:
    print("✅ Eligible")
else:
    print("❌ Not Eligible")
