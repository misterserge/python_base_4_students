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