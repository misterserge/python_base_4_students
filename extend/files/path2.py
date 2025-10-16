from os import path
from pathlib import Path

print(path.curdir)
print(path.abspath('.'))
print('cwd', Path('.').cwd())
cwd = Path('.')
print(cwd.__str__())
print(isinstance(cwd, Path))
print(type(cwd))

print(Path.__subclasses__())

print(dir(cwd))
print(cwd.absolute())
print(cwd.parent)
print(cwd.parent.is_dir())
# print(Path('.').mkdir('test_dir'))
print(Path('usr').joinpath('local', 'bin', 'python3')/"test.txt")
