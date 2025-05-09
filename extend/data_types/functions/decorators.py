from datetime import datetime

def validate_args(fn):
    def wrapper(*args, **kwargs):
        if len(args) == 0:
            raise ValueError("No arguments provided")
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"All arguments must be numbers, got {arg} of type {type(arg)}")
        return fn(*args, **kwargs)
    return wrapper

@validate_args
def sum_nums(a, b):
    return a + b

print(sum_nums(1, 2))
print(sum_nums(1, 22.5))
# print(sum_nums(1, '225'))

print('========================================')

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed this before {original_function.__name__}")
        start_time = datetime.now()
        res = original_function(*args, **kwargs)
        print(f"executing time: {datetime.now() - start_time}")
        print(f"function returned {res}")
        print(f"wrapper executed this after {original_function.__name__}")
        return res
    return wrapper_function

@decorator_function
def my_function(a, b):
    print(f"hello world! {a} {b}")
    return (a, b)
my_function(1, 2)

print('========================================')

def log_func(fn):
    def wrapper(*args, **kwargs):
        print(f"executing {fn.__name__} with arguments {args} and {kwargs}")
        res = fn(*args, **kwargs)
        print(f"function returned {res}")
        return res
    return wrapper

@log_func
def mult(a, b):
    return a * b
@log_func
def sum(a, b):
    return a + b

print(mult(2, b = 3))
print('========================================')
print(sum(2, 3))


print('========================================')

def cache_func(fn):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            return cache[key]
        cache[key] = fn(*args, **kwargs)
        return cache[key]
    return wrapper

@cache_func
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))

print('========================================')

def is_authenticated():
    return True

def check_auth(fn):
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise ValueError("User is not authenticated")
        return fn(*args, **kwargs)
    return wrapper
    
@check_auth
def get_user_data():
    return "User data"

print(get_user_data())

