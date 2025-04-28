from sys import getsizeof


def generator_func():
    for i in range(1000_000):
        yield i

print(getsizeof(generator_func()))

sqare_gen = (x * x for x in range(1000_000))

print(getsizeof(sqare_gen)) # generator is smaller than list

sqare_gen_list = [x * x for x in range(1000_000)]

print(getsizeof(sqare_gen_list))