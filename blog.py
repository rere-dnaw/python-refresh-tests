from datetime import datetime
import typing
from post import Post
from typing import List


class Blog:
    def __init__(self,title: str, author: str, posts: List[Post] = []) -> None:
        self.title = title
        self.author = author
        self.posts = posts
    
    def __str__(self) -> str:
        return f""