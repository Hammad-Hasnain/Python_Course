# ------------------------------ String Searching and Finding Methods ------------------------------
"""
| Method         | Required Arguments  | Optional Arguments        | Default Values of Optional Args         |
|----------------|---------------------|----------------------------|------------------------------------------|
| count()        | substring           | start=0, end=len(str)      | start=0, end=length of string            |
| find()         | substring           | start=0, end=len(str)      | start=0, end=length of string            |
| rfind()        | substring           | start=0, end=len(str)      | start=0, end=length of string            |
| index()        | substring           | start=0, end=len(str)      | start=0, end=length of string            |
| rindex()       | substring           | start=0, end=len(str)      | start=0, end=length of string            |
| startswith()   | prefix              | start=0, end=len(str)      | start=0, end=length of string            |
| endswith()     | suffix              | start=0, end=len(str)      | start=0, end=length of string            |

Notes:
- All methods require the substring/prefix/suffix as a mandatory argument.
- 'start' and 'end' are optional and behave like string slicing: str[start:end].
- If 'end' is omitted, it checks/searches to the end of the string.
- index() and rindex() raise ValueError if the substring is not found.
- find() and rfind() return -1 if not found.
"""


# 1. count(substring, start=0, end=len(string))
#    Returns the number of non-overlapping occurrences of a substring.
str1 = "hello world, hello python"
updatedStr1 = str1.count("hello")
print(updatedStr1)  # Output: 2



# 2. find(substring, start=0, end=len(string))
#    Returns the lowest index (first occurrence ) where the substring is found. Returns -1 if not found.
str2 = "hello world, hello python"
updatedStr2 = str2.find("hello")
print(updatedStr2)  # Output: 0

updatedStr2_not_found = str2.find("java")
print(updatedStr2_not_found)  # Output: -1



# 3. rfind(substring, start=0, end=len(string))
#    Returns the highest index (last occurrence ) where the substring is found. Returns -1 if not found.
str3 = "hello world, hello python"
updatedStr3 = str3.rfind("hello")
print(updatedStr3)  # Output: 13

updatedStr3_not_found = str3.rfind("java")
print(updatedStr3_not_found)  # Output: -1


# 4. index(substring, start=0, end=len(string))
#    Like find(), but raises ValueError if the substring is not found.
str4 = "hello world, hello python"
updatedStr4 = str4.index("world")
print(updatedStr4)  # Output: 6

# Uncomment below to see the error
# updatedStr4_error = str4.index("java")   # ❌ err => ValueError: substring not found.



# 5. rindex(substring, start=0, end=len(string))
#    Like rfind(), but raises ValueError if the substring is not found.
str5 = "hello world, hello python"
updatedStr5 = str5.rindex("hello")
print(updatedStr5)  # Output: 13

# Uncomment below to see the error
# updatedStr5_error = str5.rindex("java")   # ❌ err => ValueError: substring not found.



# 6. startswith(prefix, start=0, end=len(string))
#    Returns True if the string starts with the specified prefix.
str6 = "hello world, hello python"
updatedStr6 = str6.startswith("hello")
print(updatedStr6)  # Output: True



# 7. endswith(suffix, start=0, end=len(string))
#    Returns True if the string ends with the specified suffix.
str7 = "hello world, hello python"
updatedStr7 = str7.endswith("python")
print(updatedStr7)  # Output: True
