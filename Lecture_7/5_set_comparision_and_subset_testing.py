# 

#  Two ways for subset:
#   → Operator : <= (or < for proper subset)
#   → Method : .issubset()

# 1. .issubset(iterable) : A set a is a subset of b if all elements in a are also in b.
set_a = {1, 2}
set_b = {1, 2, 3}

# Using the <= operator (subset)
print(set_a <= set_b)  # Output: True

# Using the .issubset() method
print(set_a.issubset(set_b))  # Output: True
# Tuple as argument
print(set_a.issubset((1, 2, 3)))  # Output: True
# List as argument
print(set_a.issubset([1, 2, 3]))  # Output: True
# String as argument
print(set_a.issubset("123"))  # Output: False ('1' and '2' as characters; '1' != 1)


#  Two ways for supersetset:
#   → Operator : >= (or > for proper subset)
#   → Method : .issuperset()

# 2. .issuperset(iterable ) : A set b is a superset of a if it contains all elements of a.
set_a = {1, 2}
set_b = {1, 2, 3}

# Using the >= operator (superset)
print(set_b >= set_a)  # Output: True

# Using the .issuperset() method
print(set_b.issuperset(set_a))  # Output: True
# Tuple as argument
print(set_b.issuperset((1, 2)))  # Output: True
# List as argument
print(set_b.issuperset([1]))  # Output: True
# String as argument
print(set_b.issuperset("12"))  # Output: False (characters vs. integers mismatch)



# 3.  Proper Subset (<) and Proper Superset (>)
set_a = {1, 2}
set_b = {1, 2, 3}
set_c = {1, 2}

# Proper subset : A proper subset is strictly contained within another set (not equal).
print(set_a < set_b)  # Output: True
print(set_a < set_c)  # Output: False (equal sets)

# Proper superset : A proper superset strictly contains another set (not equal).
print(set_b > set_a)  # Output: True
print(set_c > set_a)  # Output: False (equal sets)



# 4. Equality (==) and Inequality (!=)
set_x = {1, 2, 3}
set_y = {3, 2, 1}
set_z = {1, 2}

# Equality
print(set_x == set_y)  # Output: True

# Inequality
print(set_x != set_z)  # Output: True
