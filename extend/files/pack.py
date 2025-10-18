from pathlib import Path

files_dir = Path('pack')
# if not files_dir.exists():
files_dir.mkdir(exist_ok=True)

with open('pack/test.txt', 'w') as test_file:
    test_file.write('Hello, World!\n')
    test_file.write('Hello, World!\n')

with open('pack/test.txt', 'r') as test_file:
    print(test_file.read())

# Path('files/test.txt').unlink()