info_msg = """Strings with messages
with multiple lines"""

print(info_msg)
print(type(info_msg))
print(type(str))
print(id(info_msg))
print('len', len(info_msg))
print(info_msg[0])
print(info_msg[1:3])  # slicing
print('slicing with step === ', info_msg[1:10:2])  # slicing with step
print(info_msg[1:])  # slicing without end
print(info_msg[:10])  # slicing without start
print(info_msg[:])  # slicing without start and end
print(info_msg[-1])  # slicing from the end
print(info_msg[-10:-1])  # slicing from the end
print(info_msg[-10:])  # slicing from the end
print(info_msg[:-10])  # slicing from the end
print(info_msg[::2])  # slicing with step
print(info_msg[::-1])  # slicing with negative step
