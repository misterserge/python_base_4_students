from array import array

numbers_ = array('i', [1, 2, 3, 4, 5])
print(numbers_)
print(type(numbers_))
numbers_.append(6)
print(numbers_[0])
print(numbers_[5])

with open('numbers.bin', 'wb') as f:
    numbers_.tofile(f)

with open('numbers.bin', 'rb') as f:
    numbers_from_file = array('i')
    numbers_from_file.fromfile(f, len(numbers_))
    print(numbers_from_file)