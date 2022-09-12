import unittest
from blog import Blog
from datetime import datetime

class BlogTest(unittest.TestCase):
    def test_create_post(self):
        b = Blog('Dogs', 'Tom Dans')
        b.create_post('Husky', 'Drama queen')

        self.assertEqual(0, b.posts[0].postID)
        self.assertEqual('Husky', b.posts[0].title)
        self.assertEqual('Drama queen', b.posts[0].content)

    def test_json(self):
        b2 = Blog("Cars", "Tom Don")
        date = datetime.now()

        b2.create_post('Fiat', "It's a average car", date)

        expected = {"ID": 1,
                    "title": "Cars",
                    "author": "Tom Don",
                    "posts": [{'ID': 1, 
                               'Title': 'Fiat',
                               'Date':date,
                               'Content':"It's a average car"}],}
  

        self.assertDictEqual(expected, b2.json())        