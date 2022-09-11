from datetime import date, datetime
import statics

class Post:
    POST_ID = 0

    def __init__(self, title: str,
                 content: str,
                 date: datetime = datetime.now()) -> None:
        self.postID = Post.POST_ID
        self.title = title
        self.date = date
        self.content = content

        Post.POST_ID += 1

    def __str__(self) -> str:
        return f'ID: {self.postID}, '\
               f'Title: {self.title}, '\
               f'Date: {self.date.strftime(statics.DATETIME_FORMAT)}\n'\
               f'Post content:\n{self.content}\n'

    def __repr__(self) -> str:
        return f'Post<{self.postID},' \
               f'{self.title},' \
               f'{self.date},' \
               f'{self.content}>'

    def json(self):
        return {'ID':self.postID,
                'Title':self.title,
                'Date':self.date,
                'Content':self.content,
                }        

    @classmethod
    def add_post(cls, title, content):
        return cls(title, content, datetime.now())

