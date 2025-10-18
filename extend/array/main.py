from array import array

numbers_ = array('i', [1, 2, 3, 4, 5])
print(numbers_)
print(type(numbers_))
numbers_.append(6)
print(numbers_[0])
print(numbers_[5])