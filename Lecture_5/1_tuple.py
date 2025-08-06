# `Tuple` is a built-in data structure used to store an ordered collection of items in a single variable
# Key characterstics: Ordered, immutable, allows duplicate values, can contain any data type (Heterogeneous). 


my_tuple = ("apple", "banana", "cherry", "apple")
print(my_tuple)

# A tuple with mixed data types
mixed_tuple = (1, "hello", 3.14)
print(mixed_tuple)

# A tuple with a single element needs a trailing comma
single_item_tuple = ("apple",)
print(type(single_item_tuple)) # Output: tuple
#  Single element without a trailing comma
single_item_tuple = ("apple")
print(type(single_item_tuple)) # Output: str



# Same as `List`: 
# 1. Accessing tuple element 
# 2. Slicing  
# 3. Methods: 
#   → count()  
#   → index()  