#  Two ways for Union-like:
#   → Operator : |=
#   → Method : .update()

# 1. update (Union-like) : Adds all elements from one or more iterables to the original set. Duplicates are ignored.

# Using the |= operator (requires set on the right-hand side)
set_a = {'a', 'b'}
other_iterables = ['b', 'c', 'd']
set_a |= set(other_iterables)
print(set_a)  # Output: {'a', 'b', 'c', 'd'}

# Using the update(iterables) method
set_b = {1, 2, 3}
set_c = {3, 4, 5}

set_b.update(set_a, set_c,[15,6], ('A','B'))
print(set_b)  # Output: {'d', 1, 2, 3, 4, 5, 6, 'b', 'a', 15, 'B', 'A', 'c'}



#  Two ways for Intersection Update:
#   → Operator : &=
#   → Method : .intersection_update()

# 2. intersection_update() : Keeps only elements found in both the original set and all specified iterables.
# Using the &= operator
set_a = {'x', 'y', 'z'}
set_b = {'w', 'x', 'y'}
set_a &= set_b
print(set_a)  # Output: {'x', 'y'}

# Using the intersection_update() method
set_c = {1, 2, 3, 4}
set_d = {3, 4, 5, 6}
set_c.intersection_update(set_d)
print(set_a)  # Output: {3, 4}


#  Two ways for Differnce Update:
#   → Operator : -=
#   → Method : .difference_update()

# 3. difference_update() : Removes all elements from the original set that are also in the provided iterable(s).
# Using the -= operator
set_c = {'a', 'b', 'c', 'd'}
set_d = {'c', 'd', 'e'}
set_c -= set_d
print(set_c)  # Output: {'a', 'b'}

# Using the difference_update(iterables) method
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.difference_update(set_b)
print(set_a)  # Output: {1, 2}



#  Two ways for Symmetric Differnce Update:
#   → Operator : ^=
#   → Method : .symmetric_difference_update()

# 4. symmetric_difference_update() : Updates the original set with elements that are in either set, but not both.

# Using the ^= operator
set_a = {'apple', 'banana', 'cherry'}
set_b = {'cherry', 'date', 'elderberry'}
set_a ^= set_b
print(set_a)  # Output: {'apple', 'banana', 'date', 'elderberry'}

# Using the symmetric_difference_update() method
set_c = {1, 2, 3, 4}
set_d = {3, 4, 5, 6}
set_c.symmetric_difference_update(set_d)
print(set_c)  # Output: {1, 2, 5, 6}
