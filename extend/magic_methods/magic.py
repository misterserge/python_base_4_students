int = 5
float = 5.1

sum = int + float
print(sum)  # 10.1
print(int.__add__(float))  # NotImplemented
print(float.__add__(int))  # 10.1
print(float.__radd__(int))  # 10.1

print(30*'asdadas')
print(float.__rmul__('asdadas'))
print(int.__mul__('asdadas'))
