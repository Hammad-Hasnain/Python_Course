# ------------------------------ String Property Checking Methods ------------------------------

# 1. isalnum(): Returns True if all characters are alphanumeric.
str1 = "Python3"
updatedStr1 = str1.isalnum()
print(updatedStr1)  # Output: True



# 2. isalpha(): Returns True if all characters are alphabetic.
str2 = "Python"
updatedStr2 = str2.isalpha()
print(updatedStr2)  # Output: True



# 3. isascii(): Returns True if all characters are ASCII.
str3 = "Hello123"
updatedStr3 = str3.isascii()
print(updatedStr3)  # Output: True



# 4. isdecimal(): Returns True if all characters are decimal digits('0' to '9').
str4 = "123456"
updatedStr4 = str4.isdecimal()
print(updatedStr4)  # Output: True



# 5. isdigit(): Returns True if all characters are digits.
str5 = "123456"
updatedStr5 = str5.isdigit()
print(updatedStr5)  # Output: True



# 6. isidentifier(): Returns True if the string is a valid Python identifier.
str6 = "variable_name"
updatedStr6 = str6.isidentifier()
print(updatedStr6)  # Output: True



# 7. islower(): Returns True if all cased characters are lowercase. Ignores non-letter characters (like digits, punctuation, symbols).)
str7 = "hello"
updatedStr7 = str7.islower()
print(updatedStr7)  # Output: True



# 8. isnumeric(): Returns True if all characters are numeric.
str8 = "Ⅻ"  # Roman numeral 12 (numeric, but not decimal)
updatedStr8 = str8.isnumeric()
print(updatedStr8)  # Output: True



# 9. isprintable(): Returns True if all characters are printable.
str9 = "Hello World!"
updatedStr9 = str9.isprintable()
print(updatedStr9)  # Output: True



# 10. isspace(): Returns True if all characters are whitespace.
str10 = "   \t\n"
updatedStr10 = str10.isspace()
print(updatedStr10)  # Output: True



# 11. istitle(): Returns True if the string is in title case.
str11 = "Hello World"
updatedStr11 = str11.istitle()
print(updatedStr11)  # Output: True

# 12. isupper(): Returns True if all cased characters are uppercase.  Ignores non-letter characters (like digits, punctuation, symbols).)
str12 = "HELLO WORLD"
updatedStr12 = str12.isupper()
print(updatedStr12)  # Output: True
