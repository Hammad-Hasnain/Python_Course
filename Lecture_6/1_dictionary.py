# `Dictionary` is a built-in data structure that stores data as key-value pairs
# Key characterstics:
#   → unordered (as of Python <3.7)
#   → insertion-ordered from Python 3.7+ 
#   → mutable
#   → unique keys,
#   → changeable values
#   → can contain any data type (Heterogeneous). 
"""
Rules:
  → Keys must be immutable types. That means:
  → Strings (str) 
  → Numbers (int, float) 
  → Tuples (only if the elements inside the tuple are immutable) 
  → Booleans (True, False) 
  → Frozensets (immutable version of a set)
"""


my_dict = {"name": "Hammad", "age": 22, "city": "karachi"}
print(my_dict)

# Accessing Values
name = my_dict["name"] # Output: "Hammad" 
print(name)
# accessing unknown key
# print(my_dict["hobby"])  # ❌err => KeyError: 'hobby'



# Updating Item:
my_dict["age"] = 25
print(my_dict)  # Output: {'name': 'Hammad', 'age': 25, 'city': 'karachi'}

# Updating Item:
my_dict["country"] = 'Pakistan'
print(my_dict)  # Output: {'name': 'Hammad', 'age': 25, 'city': 'karachi', 'country': 'Pakistan'}

# Lenght 
my_dict_length = len(my_dict)
print(my_dict_length)  # Output: 4



# ------------------ Dictionary with different types of keys ------------------
multi_type_keys = {
    "name": "Hammad",         # string key
    "": "empty string key",   # empty string key
    22: "age",                # integer key
    (1, 2): "tuple key",      # tuple key
    True: "boolean key"  ,    # boolean key
    None: "none key"          # none key
}

print(multi_type_keys) # Output: {'name': 'Hammad', '': 'empty string key', 22: 'age', (1, 2): 'tuple key', True: 'boolean key', None: 'none key'}
