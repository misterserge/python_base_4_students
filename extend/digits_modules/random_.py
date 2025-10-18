import random as r

# print(random.random() * 100)
print(r.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(r.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=3))
print(r.shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(r.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=3))
print(r.randrange(1, 10))
print(r.randint(1, 10))