from post import Post
from typing import List


class Blog:
    def __init__(self,title: str, author: str, posts: List[Post] = []) -> None:
        self.title = title
        self.author = author
        self.posts = posts
    
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Posts: {len(self.posts)}"

    def __repr__(self) -> str:
        return f"Blog<{self.title}, {self.author}, {len(self.posts)} Post>"

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }
    
    def create_post(self, title: str, content: str) -> None:
        self.posts.append(Post(title, content))

    @classmethod
    def create_blog(cls: 'Blog', title: 'str',
                    author: 'str', posts: List[Post] = []) -> 'Blog':
        return cls(title, author, posts)
