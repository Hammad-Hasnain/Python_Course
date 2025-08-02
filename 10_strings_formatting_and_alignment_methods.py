# ------------------------------ Formatting and Alignment Methods ------------------------------

# 1. center(width[, fillchar]): Centers the string within the specified width.
#    Arguments:
#    - width (int): REQUIRED – total width of resulting string
#    - fillchar (str of length 1): OPTIONAL – character to fill with (default is space)
str1 = "hello"

updatedStr1 = str1.center(11)
print(updatedStr1)  # Output: '   hello   '

updatedStr1b = str1.center(11, '*')
print(updatedStr1b)  # Output: '***hello***'

updatedStr1c = str1.center(12, '*') # extra char will be on right.
print(updatedStr1c)  # Output: '***hello****'



# 2. ljust(width[, fillchar]): Left-justifies the string in the given width.
#    Arguments:
#    - width (int): REQUIRED
#    - fillchar (str): OPTIONAL (default: space)
str2 = "left"

updatedStr2 = str2.ljust(10)
print(updatedStr2)  # Output: 'left      '

updatedStr2b = str2.ljust(10, '-')
print(updatedStr2b)  # Output: 'left------'



# 3. rjust(width[, fillchar]): Right-justifies the string in the given width.
#    Arguments:
#    - width (int): REQUIRED
#    - fillchar (str): OPTIONAL (default: space)
str3 = "right"

updatedStr3 = str3.rjust(10)
print(updatedStr3)  # Output: '     right'

updatedStr3b = str3.rjust(10, '.')
print(updatedStr3b)  # Output: '.....right'



# 4. zfill(width): Pads the string on the left with zeros to fill the specified width.
#    Arguments:
#    - width (int): REQUIRED
str4 = "42"

updatedStr4 = str4.zfill(5)
print(updatedStr4)  # Output: '00042'

str4b = "-42"
updatedStr4b = str4b.zfill(6)
print(updatedStr4b)  # Output: '-00042'



# 5. format(*args, **kwargs): Formats the string using positional or keyword arguments. 
#    Arguments:
#    - *args: OPTIONAL – positional arguments
#    - **kwargs: OPTIONAL – named arguments
str5 = "Name: {}, Age: {}"

updatedStr5 = str5.format("Hammad", 22)
print(updatedStr5)  # Output: 'Name: Hammad, Age: 22'

str5b = "Name: {name}, Age: {age}"

updatedStr5b = str5b.format(name="Bob", age=25)
print(updatedStr5b)  # Output: 'Name: Bob, Age: 25'

str5c = "|{:<10}|{:^10}|{:>10}|"
updatedStr5c = str5c.format('left', 'center', 'right')
print(updatedStr5c)  # Output: '|left      |  center  |     right|'
