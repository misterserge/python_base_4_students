my_fruits1 = ['apple', 'banana', 'cherry']
apple, banana, cherry = my_fruits1
print(apple)
print(banana)
print(cherry)

my_fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
apple, banana, *tale = my_fruits
print(tale)

user_profile = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}
def user_info(name, age, city=''):
    if not city:
        print(f"Name: {name}, Age: {age}")
    else:
        print(f"Name: {name}, Age: {age}, City: {city}")

user_info(**user_profile)
user_info(*user_profile)
