post_ids = {10, 40, 40, 30, 40, 25}
post_ids2 = {(10, 40), 40, 30, 40, 25}
# post_ids = {[10, 40], 40, 30, 40, 25} # error here
new_set = set()
print(type(new_set))
print(post_ids2.intersection(post_ids))
one_more_set = set([1,2,3,4,5]).union(post_ids)

print(one_more_set)

print(post_ids)
print(id(post_ids))
print(dir(post_ids))
print(type(post_ids))

post_ids.add(50)

print(post_ids)
print(id(post_ids))

post_ids.remove(40)

print(post_ids)

post_ids.discard(30)

print(post_ids)