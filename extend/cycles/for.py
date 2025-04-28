my_tuple = (1, True, "Hello", {})
for item in my_tuple:
    print(item)

my_obj = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key, value in my_obj.items():
    print(key, value)

for item in 'Hello':
    print(item)

for item in range(10):
    print(item)

for item in range(10, 20):
    print(item)

for item in range(10, 20, 2):
    print(item)


def filter_list(l, type):
    def check_el(x):
        return isinstance(x, type)
    # return [item for item in l if isinstance(item, type)]
    # return list(filter(lambda x: isinstance(x, type), l))
    return list(filter(check_el, l))

res = filter_list([1, 2, "string", True], int)
print(res)
print(isinstance(True, int))
print(int.__subclasses__())

all_numbers = [-3,1,4,1,0,-9,2,6,5,3,-5]
absolute_numbers = [abs(number) for number in all_numbers]
print(absolute_numbers)
abs_number = [];
for number in all_numbers:
    abs_number.append(abs(number))
print(abs_number)

positive_numbers = [number for number in all_numbers if number > 0]
print(positive_numbers)


my_set = {15, 2, 3}

new_set = set()
for item in my_set:
    new_set.add(item*item)

print(new_set)

print({item*item for item in my_set})


my_dict = {
    "name": 10,
    "age": 30,
    "city": 2
}
print({key: value*10 for key, value in my_dict.items()})

for key, value in my_dict.items():
    print(type(my_dict.items()))
    print(key, value)


my_car = {
    "brand": "Toyota",
    "model": "Corolla",
    "is_new": 'old'
}

print({key: value.upper() for key, value in my_car.items()})

print({key: value for key, value in my_car.items() if value.__len__() > 3})
print({key: filter(lambda x: x.__len__() > 3, value) for key, value in my_car.items()})