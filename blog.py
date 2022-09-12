from post import Post
from typing import List
from datetime import datetime


class Blog:
    BLOG_ID = 0
    def __init__(self,title: str, author: str, posts: List[Post] = None) -> None:
        self.blogID = Blog.BLOG_ID
        self.title = title
        self.author = author
        self.posts = posts
        if posts is None:
            self.posts = []
        
        Blog.BLOG_ID += 1

    
    def __str__(self) -> str:
        return f"ID: {self.blogID}, Title: {self.title}, Author: {self.author}, Posts: {len(self.posts)}"

    def __repr__(self) -> str:
        return f"Blog<{self.blogID}, {self.title}, {self.author}, {len(self.posts)} Post>"

    def json(self):
        return {
            "ID": self.blogID,
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }
    
    def create_post(self, title: str, content: str,
                    date: datetime = datetime.now()) -> None:
        self.posts.append(Post(title, content, date))

    @classmethod
    def create_blog(cls: 'Blog', title: 'str',
                    author: 'str', posts: List[Post] = None) -> 'Blog':
        return cls(title, author, posts)
