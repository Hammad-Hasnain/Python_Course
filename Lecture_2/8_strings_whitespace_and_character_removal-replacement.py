# -------------------- Whitespace and Character Removal/Replacement Methods --------------------

# 1. strip(): Removes leading and trailing whitespace or specified characters
str1 = "   Hello World!   "
# Removes leading and trailing whitespace
updatedStr1 = str1.strip()
print(updatedStr1)  # Output: "Hello World!"

# Using strip() with specified characters (removes 'H' and '!') doesn't check order of argumented string
str1b = "!!!Hello World!!!"
updatedStr1b = str1b.strip("H!")
print(updatedStr1b)  # Output: "ello World"



# 2. lstrip(): Removes leading whitespace or specified characters, doesn't check order of argumented string
str2 = "   Hello World!   "
# Removes whitespace from the beginning (left side)
updatedStr2 = str2.lstrip()
print(updatedStr2)  # Output: "Hello World!   "

# Using lstrip() with specified characters (removes only from start)
str2b = "xxHello World"
updatedStr2b = str2b.lstrip("x")
print(updatedStr2b)  # Output: "Hello World"



# 3. rstrip(): Removes trailing whitespace or specified characters, doesn't check order of argumented string
str3 = "   Hello World!   " 
# Removes whitespace from the end (right side)
updatedStr3 = str3.rstrip()
print(updatedStr3)  # Output: "   Hello World!"

# Using rstrip() with specified characters (removes only from end)
str3b = "Hello Worldyyy"
updatedStr3b = str3b.rstrip("y")
print(updatedStr3b)  # Output: "Hello World"



# 4. replace(old, new, count): Replaces occurrences of a substring, count: optional, -ve values means all occurences will be replaced.
str4 = "apple-banana-apple"
# Replaces all occurrences of "apple" with "orange"
updatedStr4 = str4.replace("apple", "orange")
print(updatedStr4)  # Output: "orange-banana-orange"

# Replaces only first occurrence
updatedStr4b = str4.replace("apple", "orange", 1)
print(updatedStr4b)  # Output: "orange-banana-apple"



# 5. removeprefix(prefix): Removes a specified prefix if present
str5 = "unhappy"
# Removes the prefix "un" if it exists
updatedStr5 = str5.removeprefix("un")
print(updatedStr5)  # Output: "happy"

# If prefix not found, returns original string
updatedStr5b = str5.removeprefix("dis")
print(updatedStr5b)  # Output: "unhappy"



# 6. removesuffix(suffix): Removes a specified suffix if present
str6 = "playing"
# Removes the suffix "ing" if it exists
updatedStr6 = str6.removesuffix("ing")
print(updatedStr6)  # Output: "play"

# If suffix not found, returns original string
updatedStr6b = str6.removesuffix("ed")
print(updatedStr6b)  # Output: "playing"
