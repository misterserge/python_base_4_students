import pack.module as m

from pack.module import test_str as ts
# from module import *

print(m)
print(type(m))
print(dir(m))
print(m.sum(1, 2))
print(m.mult(1, 2))
print(m.test_str)

print(ts)

print('__main__' == __name__)