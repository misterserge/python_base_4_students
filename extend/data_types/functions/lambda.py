def multiply(a, b):
    return a * b

print(multiply(2, 3))


print((lambda a, b: a * b)(1, 2))

def greeting(greet):
    def info(name):
        return f"{greet}, {name}"
    return info
def greeting(greet):
    return lambda name: f"{greet}, {name}"

print(greeting("Hello")("John"))

greet = greeting("Hello")

print(greet("John"))