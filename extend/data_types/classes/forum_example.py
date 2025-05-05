class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def __str__(self) -> str:
        return f"User(username={self.username}, email={self.email})"
    
class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author
        
class Forum:
    def __init__(self):
        self.users = []
        self.posts = []
        
    def register_user(self, username: str, email: str) -> User:
        user = User(username, email)
        self.users.append(user)
        return user   
    
    def create_post(self, title: str, content: str, author: User) -> Post:
        post = Post(title, content, author)
        self.posts.append(post)
        return post
    
    def get_posts(self) -> list[Post]:
        return self.posts
    
    def get_users(self) -> list[User]:
        return self.users
    
    def get_user_by_username(self, username: str) -> User | None:
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def get_user_by_email(self, email: str) -> User | None:
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def get_post_by_user(self, username: str) -> list[Post]:
        user = self.get_user_by_username(username)
        # return [post for post in self.posts if post.author == user]
        found_posts = []
        for post in self.posts:
            if post.author == user:
                found_posts.append(post)
        return found_posts
    
forum = Forum()

user1 = forum.register_user("user1", "user1@example.com")
user2 = forum.register_user("user2", "user2@example.com")

forum.create_post("Post 1", "Content 1", user1)
forum.create_post("Post 2", "Content 2", user2)

print(forum.get_posts())
print(forum.posts[0].title)

print(forum.get_user_by_username("user1"))
print('============')
print(forum.get_users())

print(forum.get_post_by_user('user111'))
print(forum.get_user_by_username('user1'))
found_posts = forum.get_post_by_user('user1')
print([post.title for post in found_posts])
found_user = forum.get_user_by_email('user1@example.com')
print(forum.get_post_by_user(found_user.username))