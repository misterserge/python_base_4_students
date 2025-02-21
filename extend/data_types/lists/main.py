list_items = ['true', True, 0]
print(list_items)
del list_items[-1]
print(list_items)

users = [
    {
        'id': 1,
        'name': 'John Doe',
    },
    {
        'id': 2,
        'name': 'Bob',
    }
]
print(users)
users.append({
    'id': 3,
    'name': 'Alice',
})
print(users)
print(len(users))
print(id(users))
print(type(users))
print(dir(users))
print(users[0].get('id'))

copy_users = users
print(copy_users)
copy_users = users.copy()
print(copy_users)
copy_users.pop()
print(copy_users)
copy_users.pop(0)
print(copy_users)


new_list_items = [1, 5, 6, 3, 2, 4, 7, 8, 9]
new_list_items.append(11)
new_list_items.insert(1, 1)
print(max(new_list_items))
new_list_items.sort()
print(new_list_items)
new_list_items.sort(reverse=True)
print(new_list_items)
new_list_items.reverse()
new_list_items.clear()

# convert
string_ = "hey, hi from here"
list_ = list(string_)
print(list_)
list_ = list({
    'id': 1,
    'name': 'John Doe',
})
print(list_)
print(list_+new_list_items[:2])
list_cop = list_
print(id(list_), id(list_cop))
print(list_, list_cop)
list_cop = list_.copy()
print(id(list_), id(list_cop))
print(list_, list_cop)
list_cop = list_[:]
print(id(list_), id(list_cop))
print(list_, list_cop)
list_cop = [*list_]
print(id(list_), id(list_cop))
print(list_, list_cop)
list_cop = list(list_)
print(id(list_), id(list_cop))
print(list_, list_cop)

# task
first_list = [1,2,3,4,5]
print(first_list)
first_list.pop(2)
print(first_list)
first_list.__len__()
print(first_list)
first_list.reverse()
print(first_list)
second_list = [14,15]
thirth_list = first_list + second_list
print(thirth_list)
