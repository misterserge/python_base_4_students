my_num = -10
print(+my_num)

my_bool = True
print(not my_bool)

print(+my_bool+my_num)

my_str = "Hello"
print(my_str * 3)

my_list = [1, 2, 3]
print(my_list * 3)

a = 5
b = 1
print(a+b)
a+=5
print(a)
print(a==b)
print(a and b)

set_one = {10, 'abc', 50, True}
set_two = {10, 'abc', True, 50}
set_tree = {10, 'abc', 50, True}

print(set_one == set_two)
print(set_one.__eq__(set_two))
print(set_one is set_two)
print(set_one is set_tree)
print(10 in set_one)