

with open('test.txt', 'w') as file:
    file.write('Hello, World!\n')

with open('test.txt', encoding='utf-8') as file:
    print(file.read())

with open('test.txt', 'a') as file:
    file.write('Hello, World!\n')

with open('test.txt', 'r') as file:
    print(file.readlines())