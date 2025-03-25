my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

my_dict2 = {
    'name': 'John',
    'city': 'New York',
    'age': 25,
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'state': 'NY',
        'zip': '10001',
    }
}
print(id(my_dict))
print(type(my_dict))
print(my_dict.items())
print(my_dict.keys())
print(type(my_dict.items()))
print(id(my_dict) == id(my_dict2))
print(my_dict == my_dict2)
print(my_dict2)
print(len(my_dict2))
my_dict2['name']='Bob'
my_dict2['surname']='Smith'
age = 'age'
print(my_dict2['age'])
del my_dict2[age]
print(my_dict2.get('age', 000))
print(my_dict2)
print(my_dict2['address']['city'])
print(my_dict2.get('address').get('city'))
# print(my_dict2['address'].get(['city'])) #error here
print(my_dict2.get('address', {}).get('city2', 'Not found'))

my_dict2.pop('address')
print(my_dict2)
my_dict2.popitem()
print(my_dict2)
new_dict = my_dict2.copy()
print(new_dict)
new_dict['middle_name'] = 'Alice'
print(new_dict)
print(my_dict2)

my_list = [('name', 'Bob'), ['bool', True], ['list', [1,2,3]]]
my_dict3 = dict(my_list)
print(my_dict3)
