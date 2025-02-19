def person_info(**person):
    print(person.get('city', 'No city specified'))
    print(person)
    print(type(person))


# person_info(name='Bill', age=30, city='Paris')
person_info(name='Bill', age=30)