from copy import deepcopy


list = [1, 2, 3]
print(id(list))
other_list = [1, 2, 3]
print(id(other_list))
print(id([1, 2, 3]))
other_list.append(4)
print(id(other_list))


info_obj = {
    'name': 'John',
    'age': 25
}
print(id(info_obj))
info_obj2 = {
    'name': 'John',
    'age': 25,
    'reviews': []
}
print(id(info_obj2))
print(info_obj2)
new_obj4 = deepcopy(info_obj2)
new_obj4['reviews'].append('pupupu')
new_obj3 = info_obj2.copy()
new_obj3['reviews'].append('Great product!')
print(info_obj2)
print(new_obj3)
print(new_obj4)

new_obj = info_obj
new_obj['name'] = 'Jane'
print(info_obj)

new_obj = info_obj.copy()
new_obj['name'] = 'Alice'
print(info_obj)  # {'name': 'Jane', 'age': 25}
print(new_obj)  # {'name': 'Alice', 'age': 25}
copied_obj = {**info_obj}
copied_obj['name'] = 'Alice2'
print(copied_obj)  # {'name': 'Alice2', 'age': 25}
