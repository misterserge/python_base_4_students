my_range = range(10)

print(my_range)
print(type(my_range))
print(id(my_range))
print(dir(my_range))

print(list(my_range))

my_range2 = range(10, 20)

print(list(my_range2))

my_range3 = range(10, 20, 2)
print(my_range3.start)
print(my_range3.stop)
print(my_range3.step)
print(my_range3.count(10))
print(my_range3.index(10))
print('========')

print(list(my_range3))

my_range4 = range(20, 10, -2)

print(list(my_range4))
print(my_range4[0])
print(my_range4[1])

print('test for')
print('========')
for n in my_range4:
    print(n)
# print(my_range4[6])

