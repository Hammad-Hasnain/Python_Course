# Nested statement means a statement inside another statement.
# e.g. an if statement placed inside another if or else block is a nested if statement.

# General syntax: totally mutable for `elif` as well.
"""
if condition1:
    # code block if condition1 is True
    if condition2:
        # code block if both condition1 and condition2 are True
    else:
        # code block if condition1 is True but condition2 is False
else:
    # code block if condition1 is False
"""

# *** Write a program to verify user login credentials. ***

# Predefined username and password
correct_username = "user123"
correct_password = "pass123"

# Take input from user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check credentials
if username == correct_username:
    if password == correct_password:
        print("✅ Login successful! Welcome,", username)
    else:
        print("❌ Incorrect password.")
else:
    print("❌ Username not found.")