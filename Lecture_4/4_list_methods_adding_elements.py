# Python methods for adding element to list
# 1. append(item) : Adds a single item to the very end of the list. 

# A Sample List
fruits = ["apple", "banana", "cherry"]


fruits.append("orange",)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']


# ------------------------------ What if we try to add two elements or keep it empty using append() ?? 🤔💭 ------------------------------
# fruits.append("orange","almond")  # ❌err => TypeError: list.append() takes exactly one argument (2 given)
# fruits.append()  # ❌err => TypeError: list.extend() takes exactly one argument (0 given)
  


# 2. extend(iterable) : Adds all the items from an iterable (like another list, a tuple, or a string) to the end of the list. 
cars = ['Toyota', 'Honda', 'BMW']
more_cars = ['Audi', 'Ford', 'Tesla']

cars.extend('Kia')  # 'Kia' is a string (iterable), so 'K', 'i', 'a' added separately
print(cars)  # Output: ['Toyota', 'Honda', 'BMW', 'K', 'i', 'a', 'Audi', 'Ford', 'Tesla']

cars.extend(more_cars)
print(cars)


# ------------------------------ What if we try to add two elements or keep it empty using extend() ?? 🤔💭 ------------------------------
# alphabets.extend('d','e')  # ❌err => TypeError: list.append() takes exactly one argument (2 given)
# fruits.extend()  # ❌err => TypeError: list.extend() takes exactly one argument (0 given)



# 3. insert(index, item) : Inserts an item at a specific index. All items from that index onward are shifted one position to the right.
countries = ["Pakistan", "China", "USA"]

countries.insert( 1,"India")
print(countries)  # Output: ['Pakistan', 'India', 'China', 'USA']


# ------------------------------ What if we try to add element at an index greater than the list length ?? 🤔💭 ------------------------------
countries.insert( 10,"Russia")
print(countries)  # Output: ['Pakistan', 'India', 'China', 'USA', 'Russia'] i.e. Index > length, so 'Russia' appended at end


# ------------------------------ What if we try to add element at an negative index ?? 🤔💭 ------------------------------
countries.insert( -1 ,"Indonesia")
print(countries)  # Output: ['Pakistan', 'India', 'China', 'USA', 'Indonesia', 'Russia'] i.e. # -1 inserts before last element, -2 before second last, etc.
