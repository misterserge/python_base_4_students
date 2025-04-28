person_info = {
    'name': "John Doe",
    'age': 30,
    'gender': "Male",
    'email': "john.doe@example.com",
    'phone': "+1234567890",
    'address': "123 Main St, Anytown, USA",
    'city': "Anytown",
}

if not person_info.get('name'):
    print("Name is required")
else:
    print(person_info['name'])

number = 10.1
if isinstance(number, int):
    print("Number is an integer")
elif type(number) is float:
    print(f"{number} is a float")
else:
    print(f"{number} is not an integer or float")


