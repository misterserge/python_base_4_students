name = 'user'
# name = None
surname = 'user_surname'

if surname and name:
    print(surname, name)
elif name:
    print(name)
    print(name)
elif surname: #if name is False or None or empty string
    print(surname)
else:
    print('no name and surname specified')
