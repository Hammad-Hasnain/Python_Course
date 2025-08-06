# Python methods for removing element from list

# 1. remove(element:reqd) : removes the first occurrence of a specified element.
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'banana']

# if value isn't found
# fruits.remove("guava")  # ❌err => ValueError: list.remove(x): x not in list



# 2. pop(index=-1) :  removes an element at a specific index and returns the removed element.
numbers = [10, 20, 30, 40, 50]

removed_element = numbers.pop(2)
print(numbers)  # Output: [10, 20, 40, 50]
print(removed_element)  # Output: 30

# remove last element if index isn't provided
numbers.pop() 
print(numbers)  # Output: [10, 20, 40]

# remove last element if index isn't provided
# numbers.pop(10) # ❌er=> IndexError: pop index out of range



# 3. clear() :  removes all elements/items from a list.
mixed_list = ['a', 1, 90.67, None, True,]
mixed_list.clear()
print(mixed_list)  # Output: []