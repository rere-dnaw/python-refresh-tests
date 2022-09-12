import unittest
from blog import Blog


class BlogTest(unittest.TestCase):
    def test_create_blog(self):
        b = Blog("Cars", "Tom Don")

        self.assertEqual(3, b.blogID)
        self.assertEqual("Cars", b.title)
        self.assertEqual("Tom Don", b.author)
        self.assertListEqual([], b.posts)
    
    def test_repr(self):
        b = Blog("Cars", "Tom Don")

        expected = f"Blog<3, Cars, Tom Don, 0 Post>"

        self.assertEqual(expected, b.__repr__())

    def test_repr_multiple(self):
        b = Blog("Cars", "Tom Don")
        b.posts = ['post1', 'post2']

        expected = f"Blog<4, Cars, Tom Don, 2 Post>"

        self.assertEqual(expected, b.__repr__())

    def test_str(self):
        b = Blog("Cars", "Tom Don")

        expected = f"Title: Cars, Author: Tom Don, Posts: 0"


        self.assertEqual(expected, b.__str__())
    
    def test_str_multiple(self):
        b = Blog("Cars", "Tom Don")
        b.posts = ['post1', 'post2']

        expected = f"Title: Cars, Author: Tom Don, Posts: 2"

        self.assertEqual(expected, b.__str__())

    def test_json(self):
        b = Blog("Cars", "Tom Don")

        expected = {"ID": 2,
                    "title": "Cars",
                    "author": "Tom Don",
                    "posts": [],}

        self.assertDictEqual(expected, b.json())
    
    def test_create_blog_class(self):
        b = Blog.create_blog('Dogs', 'Sam Rond')

        self.assertEqual('Dogs',b.title)
        self.assertEqual('Sam Rond',b.author)
        self.assertListEqual([], b.posts)