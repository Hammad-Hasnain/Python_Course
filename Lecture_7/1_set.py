# `Set` is a built-in data type in Python used to store collections of items.
# Key characterstics:
#   → unordered
#   → mutable
#   → unique elements,
#   → immutable elements (While a set is mutable, its elements must be of an immutable type (like numbers, strings, or tuples). We cannot have mutable items like lists or other sets inside a set.) 
#   → can contain any data type (Heterogeneous). 

# 1. *** Using Curly Braces {} *** 
# A set of integers
my_set = {1, 2, 3, 5, 5, 2}
print(my_set)  # Output: {1, 2, 3, 5} - duplicates are automatically removed

# A set with mixed data types
mixed_set = {"hello", 100, (20, 30)}
print(mixed_set)  # Output: {100, 'hello', (20, 30)} (order may vary)



# 2. *** Using the set() Constructor ***
# For empty set
empty_dict = {}  # Dictionary not a Set
empty_set = set()  # Dictionary not a Set
print(type(empty_dict))  # Output: <class 'dict'>
print(type(empty_set))  # Output: <class 'set'>


# From a list
my_list = [1, 2, 3, 1]
my_set_from_list = set(my_list)
print(my_set_from_list)  # Output: {1, 2, 3}

# From a string
my_set_from_string = set("hello")
print(my_set_from_string)  # Output: {'e', 'o', 'l', 'h'} (order may vary)

    