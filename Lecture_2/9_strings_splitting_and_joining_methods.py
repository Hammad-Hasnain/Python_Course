# ------------------------------ Splitting and Joining Methods ------------------------------

# 1. split(sep=None, maxsplit=-1): Splits the string into a list of substrings using a separator.
str1 = "apple,banana,cherry"
# Splits by comma
splitStr1 = str1.split(",")
print(splitStr1)  # Output: ['apple', 'banana', 'cherry']

# Using maxsplit to split only once
splitStr1b = str1.split(",", 1)
print(splitStr1b)  # Output: ['apple', 'banana,cherry']

# Default split (splits on any whitespace)
str1c = "one two   three"
splitStr1c = str1c.split()
print(splitStr1c)  # Output: ['one', 'two', 'three']



# 2. rsplit(sep=None, maxsplit=-1): Same as split(), but starts splitting from the right.
str2 = "apple,banana,cherry"
# Splits from the right with maxsplit=1
splitStr2 = str2.rsplit(",", 1)
print(splitStr2)  # Output: ['apple,banana', 'cherry']

# No sep provided, splits on whitespace from the right
str2b = "one two   three"
splitStr2b = str2b.rsplit(None, 1)
print(splitStr2b)  # Output: ['one two', 'three']



# 3. splitlines(keepends=False): Splits a string into a list of lines.
str3 = "Line1\nLine2\nLine3"
# Without keeping newline characters
splitStr3 = str3.splitlines()
print(splitStr3)  # Output: ['Line1', 'Line2', 'Line3']

# Keeping newline characters
splitStr3b = str3.splitlines(keepends=True)
print(splitStr3b)  # Output: ['Line1\n', 'Line2\n', 'Line3']



# 4. join(iterable): Joins elements of an iterable using the string as a separator.
words = ["apple", "banana", "cherry"]
# Join with comma
joinedStr1 = ",".join(words)
print(joinedStr1)  # Output: "apple,banana,cherry"

# Join with space
joinedStr2 = " ".join(words)
print(joinedStr2)  # Output: "apple banana cherry"

# Join with hyphen
joinedStr3 = "-".join(words)
print(joinedStr3)  # Output: "apple-banana-cherry"