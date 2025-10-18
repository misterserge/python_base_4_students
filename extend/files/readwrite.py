from pathlib import Path

# if Path('test.txt').exists():
#     Path('test.txt').unlink()

# with open('test.txt', 'w') as file:
#     file.write('Hello, World!\n')

# with open('test.txt', encoding='utf-8') as file:
#     print(file.read())

# with open('test.txt', 'a') as file:
#     file.write('Hello, World!\n')

# with open('test.txt', 'r') as file:
#     print(file.readlines())


# ==============================================
# test_file = open('test.txt', 'w')
# print('test_file', test_file)
# test_file.write('Hello, World!\n')
# test_file.close()

# test_file = open('test.txt', 'r')
# print(test_file.read())
# test_file.close()

# test_file = open('test.txt', 'a')
# test_file.write('Hello, World!\n')
# test_file.close()

# with open('test.txt', 'w') as test_file:
with open('test.txt', 'a') as test_file:
    test_file.write('Hello, World!\n')
    test_file.write('Hello, World!\n')


test_file = open('test.txt', 'r')
print(test_file.read())
test_file.close()

# with open('test.txt', 'a') as test_file:
    # print(test_file.read())
    # lines = test_file.readlines()
    # for line in lines:
    #     print(line)
    # for line in test_file:
    #     print(line)
    # while True:
    #     lines = test_file.readline()
    #     if not lines:
    #         break
    #     print(lines)

Path('test.txt').unlink()
