# Type Conversion (Implicit Conversion) automatically by translator
a = 10  # int
b = 5.5 # float (superiror than int)
"""
print(a+b)
print(type(a+b))
"""



# Type Casting (Explicit Conversion) manually by programmer
c = "10"
d = 10

# print(c + d) #TypeError: can only concatenate str (not "int") to str
# print(int(c) + d) # 20
