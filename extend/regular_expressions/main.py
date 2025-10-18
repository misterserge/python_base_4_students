import re

my_string = 'Hello, World! 123'

print(re.match(r'Hello', my_string))
print(re.search(r'Hello$', my_string))
pattern_ = re.compile(r'Hello\,')
print(pattern_.search(my_string))
print(pattern_.match(my_string))
print(re.search(r'^Hello', my_string))

# email validation
email = 'test@test.com'
email2 = 'test@testcom'
email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
# print(email_regex.search(email))
print(email_regex.fullmatch(email))
print(email_regex.fullmatch(email2))
# print(email_regex.findall(email))
# print(email_regex.split(email))