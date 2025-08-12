# Loop inside a loop is called nested loop either for or while loop. No fixed nesting limit.
# A `while` loop can contain a `for` loop inside it.
# A `for` loop can also contain a `while` loop inside it


# 1. nested for loop
outer_list = [1, 2]
inner_list = ['a', 'b']

for i in outer_list:  # Outer loop
    print("Outer loop =", i)
    for j in inner_list:  # Inner loop
        print("  Inner loop =", j)

# Output:  Outer loop = 1
#            Inner loop = a
#            Inner loop = b
#          Outer loop = 2
#            Inner loop = a
#            Inner loop = b



# 2. nested while loop
outer_list = [1, 2]
inner_list = ['a', 'b']

i = 0  # index for outer_list
while i < len(outer_list):  # Outer loop
    print("Outer loop =", outer_list[i])

    j = 0  # index for inner_list
    while j < len(inner_list):  # Inner loop
        print("  Inner loop =", inner_list[j])
        j += 1

    i += 1

# Output:  Outer loop = 1
#            Inner loop = a
#            Inner loop = b
#          Outer loop = 2
#            Inner loop = a
#            Inner loop = b



# 3. try for inside while



# 4. try while inside for 


