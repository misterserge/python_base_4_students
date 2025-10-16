from os import path
from pathlib import Path

print(path.abspath('.'))
print(type(path))

print(Path('.').absolute())
print(type(Path))

