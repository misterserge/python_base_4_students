try:
    print(10/0)
except ZeroDivisionError as e:
    print(isinstance(e, ZeroDivisionError))
    print(isinstance(e, Exception))
    print(isinstance(e, object))
    print(type(e))
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(isinstance(e, Exception))
    print(e)
except:
    print('unknown error')
else:
    print("no errors here")
finally:
    print("end")


def divide_nums(a, b):
    if (a == 0 or b == 0):
        raise ValueError("a and b cannot be 0")
    return a / b


def divide_nums_cover(a, b):
    try:
        return divide_nums(a, b)
    except TypeError as e:
        print(e)
        return None


print(divide_nums_cover(10,0))
