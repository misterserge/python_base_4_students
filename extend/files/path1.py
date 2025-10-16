from pathlib import Path

# file_path = Path('test.txt')

# print([m for m in dir(file_path) if not m.startswith('_')])

print(Path.cwd())

print(Path('usr').joinpath('local', 'bin', 'python3')/"test.txt")

print(Path('main.py').exists())
print(Path('./main.py').exists())
print(Path('../main.py').exists())

for f in Path('.').iterdir():
    print(f)
