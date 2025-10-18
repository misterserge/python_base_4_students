from pathlib import Path
from zipfile import ZipFile

# Path('./files').mkdir(exist_ok=True)
# with open("files/test.txt", "w") as test_file:
#     test_file.write("Hello, World!\n")
#     test_file.write("Hello, World!\n")

# with open("files/test2.txt", "w") as test_file:
#     test_file.write("Hello, World!\n")
#     test_file.write("Hello, World!\n")

# with ZipFile('files.zip', mode='w') as my_zip_file:
#     print(my_zip_file)
#     # my_zip_file.write('files/test.txt')
#     # my_zip_file.write('files/test2.txt')
#     for file in Path('files').iterdir():
#         print(file)
#         my_zip_file.write(file)

with ZipFile('files.zip', mode='r') as my_zip_file:
    print(my_zip_file)
    for file in my_zip_file.namelist():
        print(file)
        with open(file, 'r') as test_file:
            print(test_file.read())
    my_zip_file.extractall('files_extracted')
    print(my_zip_file.infolist())

