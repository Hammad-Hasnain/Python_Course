

#  Two ways for union:
#   → Operator : | 
#   → Method : .union()

# 1. union() : combines  all unique elements and returns a new set but order may vary 
set_a = {"A", "B", "C", "D"}
set_b = { "D", "E"}

# Using the | operator
op_union = set_a | set_b
print(op_union)  # Output: {'A', 'C', 'D', 'E', 'B'} 

# Using the .union(iterables) method
method_union = set_a.union(set_b)
print(method_union)  # Output: {'A', 'C', 'D', 'E', 'B'} 
#  tuple as an argument
print(set_a.union((1,2,3))) # Output: {1, 2, 3, 'A', 'D', 'B', 'C'}
#  list as an argument
print(set_a.union([1,2,3])) # Output: {1, 2, 3, 'A', 'D', 'B', 'C'}
#  string as an argument
print(set_a.union("Hello")) # Output: {'H', 'e', 'l', 'o', 'A', 'D', 'B', 'C'}



#  Two ways for intersection:
#   → Operator : & 
#   → Method : .intersection()

# 2. intersection() : returns a new set containing common elements in both sets but order may vary
set_a = {"A", "B", "C", "D", "E"}
set_b = { "D", "E"}

# Using the & operator
op_intersecition = set_a & set_b
print(op_intersecition)  # Output: {'D', 'E'} 

# Using the .intersection(iterables) method
method_itnersection = set_a.intersection(set_b)
print(method_itnersection)  # Output: {'D', 'E'}
#  tuple as an argument
print(set_a.intersection((1,2,3))) # Output: set() (nothing common)
#  list as an argument
print(set_a.intersection([1,2,'A'])) # Output: {'A'}
#  string as an argument
print(set_a.intersection("Hello Doctor")) # Output: {'D'}



#  Two ways for difference:
#   → Operator : - 
#   → Method : .difference()

# 3. difference() : returns a new set containing elements in the first set but not in the second set, order may vary
set_a = {"A", "B", "C", "D", "E"}
set_b = {"D", "E"}

# Using the - operator
op_difference = set_a - set_b
print(op_difference)  # Output: {'A', 'B', 'C'}

# Using the .difference(iterables) method
method_difference = set_a.difference(set_b)  
print(method_difference)  # Output: {'A', 'B', 'C'}
# tuple as an argument
print(set_a.difference((1, 2, 3)))  # Output: {'A', 'B', 'C', 'D', 'E'} (no common elements removed)
# list as an argument
print(set_a.difference([1, 2, 'A']))  # Output: {'B', 'C', 'D', 'E'} ('A' removed)
# string as an argument
print(set_a.difference("Hello Doctor"))  # Output: {'B', 'E', 'A', 'C'} ('D' removed)



#  Two ways for symmetric_difference:
#   → Operator : ^
#   → Method : .symmetric_difference()

# 4. symmetric_difference() : returns a new set containing elements in either set but not in both, order may vary
set_a = {"A", "B", "C", "D", "E"}
set_b = {"D", "E", "F", "G"}

# Using the ^ operator
op_symmetric_diff = set_a ^ set_b
print(op_symmetric_diff)  # Output: {'A', 'B', 'C', 'F', 'G'}

# Using the .symmetric_difference(iterables) method
method_symmetric_diff = set_a.symmetric_difference(set_b)
print(method_symmetric_diff)  # Output: {'A', 'B', 'C', 'F', 'G'}
# tuple as an argument
print(set_a.symmetric_difference((1, 2, 3)))  # Output: {'A', 'B', 'C', 'D', 'E', 1, 2, 3}
# list as an argument
print(set_a.symmetric_difference([1, 2, 'A']))  # Output: {'B', 'C', 'D', 'E', 1, 2}
# string as an argument
print(set_a.symmetric_difference("Hello Doctor"))  # Output: {'A', 'B', 'C', 'E', 'H', 'l', 'o', ' ', 't', 'r'}



# 5. isdisjoint(other) : returns True if the set has no elements in common with other, otherwise False
set_a = {"A", "B", "C"}
set_b = {"D", "E", "F"}
set_c = {"B", "E"}

# Check if set_a and set_b are disjoint (no common elements)
print(set_a.isdisjoint(set_b))  # Output: True
# Check if set_a and set_c are disjoint
print(set_a.isdisjoint(set_c))  # Output: False
# tuple as an argument
print(set_a.isdisjoint((1, 2, 3)))  # Output: True (no common elements)
# list as an argument
print(set_a.isdisjoint(['X', 'Y', 'B']))  # Output: False ('B' is common)
# string as an argument
print(set_a.isdisjoint("XYZ"))  # Output: True (no common characters)
print(set_a.isdisjoint("ABC"))  # Output: False ('A', 'B', 'C' are common)
