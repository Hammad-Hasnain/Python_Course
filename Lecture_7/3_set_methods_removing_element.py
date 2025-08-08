# 1. remove(element)	Removes an element, but raises an error if it's not there, returns None.
active_users = {101, 105, 110, 115}

# Successfully remove user 105
active_users.remove(105)
print(active_users)  # Output: {115, 101, 110}
# element not exist
# active_users.remove(1050)  # ❌err =>  KeyError: 1050  



# 2. discard(element)	Removes an element, but does nothing if it's not there, returns None.
active_users = {101, 105, 110, 115}

# Successfully remove user 105
active_users.discard(105)
print(active_users)  # Output: {115, 101, 110}
# element not exist
active_users.discard(1050)  # No Error



# 3. pop()	Removes and returns an arbitrary element but raises a KeyError if set is empty.
numbers = {1, 2, 3, 4}

# Successfully remove arbitrary number
returned_number = numbers.pop()
print(numbers)  # Output: {2, 3, 4} may vary
print(returned_number)  # Output: 1 may vary
# if set is empty
numbers = {}
# numbers.pop()  # ❌err => TypeError: pop expected at least 1 argument, got 0



# 4. clear()	Removes all elements from the set and returns None.
shopping_cart = {"apple", "bread", "milk", "cheese"}
shopping_cart.clear()
print(shopping_cart)  # Output: set()