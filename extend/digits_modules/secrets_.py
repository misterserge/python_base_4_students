import secrets
import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)

password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10))
print('password', password)

# print(secrets.randbelow(10))
# print(secrets.token_bytes(10))
# print(secrets.token_hex(10))
# print(secrets.token_urlsafe(10))