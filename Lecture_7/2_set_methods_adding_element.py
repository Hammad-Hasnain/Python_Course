# Adding elements in set

# 1. add(element): Adds a single element to the set. If the element is already present, the set remains unchanged.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
 
   
  
# 2. update(iterables:optional): Adds all elements from an iterable (like a list or another set) to the set.
my_set.update({ 4, 5, 6 })
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

#  can accept one or more iterable
my_set.update([7,8],(9,),"Hello")
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, H, e, l, o}

