def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy
person_one = {
    'name': 'Alice',
    'age': 25
}
print(person_one)
print(increase_person_age(person_one))

def merge_list_to_dict(my_list, my_list2):
    return dict(zip(my_list, my_list2))

print(merge_list_to_dict(['name', 'age'], ['Alice', 25]))
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}
print(merge_dicts({'name': 'Alice'}, {'age': 25}))
