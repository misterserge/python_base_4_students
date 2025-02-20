def person_info(name, age):
    print(name)
    print(age)


# person_info('John', age=30)
# person_info('Jane', 25)

def sum(*args):
    total = 0
    for arg in args:
        print(total, ' + ', arg)
        total += arg
    return total
    # print(args)
    # print(type(args))
    # return a + b

print(sum(5, 2, 5, 4, 8, 9, 0))