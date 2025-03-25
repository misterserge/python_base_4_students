my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

my_dict2 = {
    'name': 'John',
    'city': 'New York',
    'age': 25,
}

print(id(my_dict) == id(my_dict2))
print(my_dict == my_dict2)
print(my_dict2)
my_dict2['name']='Bob'
my_dict2['surname']='Smith'
del my_dict2['age']
print(my_dict2)