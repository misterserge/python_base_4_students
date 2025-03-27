from datetime import date


def sum_nums(a, b=3):
    return a + b
print(sum_nums(1, 2))  # Output: 3
print(sum_nums(1))  # Output: 4
def sum_nums(*args):
    print(args)
    print(type(args))
    return sum(args)
print(sum_nums(1, 2, 3, 4))  # Output: 10


def get_post_info(name='Username', post_id=11):
    return f'Post {post_id} by {name}'
print(get_post_info())  # Output: Post 11 by Username
print(get_post_info('John'))  # Output: Post 11 by John

def get_post_info(post_id=11, name = 'Username'):
    return f'Post {post_id} by {name}'
print(get_post_info())  # Output: Post 11 by Username
print(get_post_info(12, name = 'John'))  # Output: Post 11 by John

def get_person_info_by_dict(id, surname='', **person):
    return f"Post {person['post_id']} by {person['name']} and id {id} and surname {surname}"
print(get_person_info_by_dict(33, 'surname', name='John', post_id=12))  # Output: Post 12 by John


def merge_lists_to_dict(list1, list2):
    return {k: v for k, v in zip(list1, list2)}
print(merge_lists_to_dict(['a', 'b', 'c'], [1, 2, 3]))  # Output: {'a': 1, 'b': 2, 'c': 3}
def merge_lists_to_dict(list1, list2):
    return dict(zip(list1, list2))
print(merge_lists_to_dict(['a', 'b', 'c'], [1, 2, 3]))  # Output: {'a': 1, 'b': 2, 'c': 3}

def update_dict_info(**dict_data):
    dict_data['year_old'] = 12
    return dict_data
print(update_dict_info(name='John', surname='Doe'))  # Output: {'name': 'John', 'surname': 'Doe', 'post_id': 12}


def update_dict_info(*dict_data):
    dict_data = dict(dict_data)
    dict_data['year_old'] = 12
    return dict_data
print(update_dict_info({'John', 'Doe'}))



#############################################
def get_week_date():
    return date.today().strftime("%A")

def create_new_post(post, weekday=get_week_date()):
    post_copy = post.copy()
    post_copy['created at weekday'] = weekday
    return post_copy

initial_post = {
    'post_id': 1,
    'name': 'John',
    'surname': 'Doe'
}

post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)
# Output: {'post_id': 1, 'name': 'John', 'surname': 'Doe', 'created at weekday': 'Monday'}