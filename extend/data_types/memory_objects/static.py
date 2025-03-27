number = 10
print(id(number))
other_number = 10
print(id(other_number))
print(id(10))

second_number = number
second_number += 5
print(id(second_number))
print(id(number))