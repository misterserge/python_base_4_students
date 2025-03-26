users = [
    {"name": "John", "age": 25, "city": "New York"},
    {"name": "Jane", "age": 30, "city": "Los Angeles"},
    {"name": "Jim", "age": 35, "city": "Chicago"},
]

print(users)
users[2]["name"] = "John"

print(users)
print(users+users)
print(users[len(users)-1])



