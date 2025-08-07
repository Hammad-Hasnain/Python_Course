# Python basic dictionary methods
"""
Rules
update()
  → If a key already exists: The update() method will overwrite the existing value with the new one.
  → If a key is new: The new key-value pair will be added to the dictionary.
"""

person = {
    "name": "Sara",
    "age": 28
}

# 1. get(key, default_value:Optional): returns value if key exists, else None or default
# Key exists
print(person.get("name"))  # Output: Sara
# Key does not exist, no default value provided
print(person.get("gender"))  # Output: None
# Key does not exist, with a default value
print(person.get("gender", "N/A"))  # Output: N/A



# 2. pop(key, default_value:Optional): removes a key and returns its value.
#                                      Raises a KeyError if the key is not found (unless a default is provided).

age = person.pop("age")
print(age)       # Output: 28
print(person)    # Output: {'name': 'Sara'}
# Key does not exist, default value provided
print(person.pop("city","N/A"))  # Output: => KeyError: 'city'
# Key does not exist, no default value provided
# print(person.pop("city"))  # ❌err => KeyError: 'city'




# update(): adds or updates keys from another dictionary
# Updating with another dictionary
person.update({"gender": "Female", "city": "Karachi"})
print(person)  # Output: {'name': 'Sara', 'gender': 'Female', 'city': 'Karachi'}
#  Updating with an iterable of key-value pairs
settings = {'theme': 'light', 'font_size': 12}
new_settings = [('font_size', 14), ('language', 'English')] 
settings.update(new_settings)
print(settings)  # Output: {'theme': 'light', 'font_size': 14, 'language': 'English'}
# Updating with keyword arguments
car = {'make': 'Toyota', 'model': 'Camry'} 
car.update(year=2023, color='blue')
print(car)  # Output: {'make': 'Toyota', 'model': 'Camry', 'year': 2023, 'color': 'blue'} 



# clear(): removes all items
person.clear()
print(person)  # {}



# copy(): returns a shallow copy as we done for `List`
