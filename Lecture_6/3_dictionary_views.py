
product = {
    "id": 101,
    "name": "Laptop",
    "price": 90000
}

# keys(): returns all keys
print(product.keys())  # Output: dict_keys(['id', 'name', 'price'])

# values(): returns all values
print(product.values())  # Output: dict_values([101, 'Laptop', 90000])

# items(): returns key-value pairs
print(product.items())  # Output: dict_items([('id', 101), ('name', 'Laptop'), ('price', 90000)])
