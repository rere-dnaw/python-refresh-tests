from dataclasses import dataclass
import unittest
from blog import Blog
from datetime import datetime


class BlogTest(unittest.TestCase):
    def test_create_post(self):
        b = Blog('Dogs', 'Tom Dans')
        b.create_post('Husky', 'Drama queen')
        date = datetime.now()

        self.assertEqual(0, b.posts[0].postID)
        self.assertEqual('Husky', b.posts[0].title)
        self.assertEqual('Drama queen', b.posts[0].content)
        