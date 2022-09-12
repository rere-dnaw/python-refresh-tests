import unittest
from post import Post
from datetime import datetime

unittest.defaultTestLoader.sortTestMethodsUsing = lambda *args: -1

class PostTest(unittest.TestCase):
    def test_create_add_post(self):
        date = datetime.now()
        p = Post('Test', 'Testing Content', date)

        self.assertEqual('Test', p.title)
        self.assertEqual('Testing Content', p.content)
        self.assertEqual(date, p.date)
        self.assertEqual(p.postID, 0)
    
    def test_json(self):
        date = datetime.now()
        p = Post('Test', 'Testing Content', date)

        expected = {'ID':1, 'Title':'Test',
                    'Date':date, 'Content':'Testing Content'}

        self.assertDictEqual(expected, p.json())

    def test_repr(self):
        date = datetime.now()
        p = Post('Test', 'Testing Content', date)

        expected = f'Post<2,Test,{date},Testing Content>'
        self.assertEqual(expected, p.__repr__())

    def test_str(self):
        date = datetime.now()
        p = Post('Test Post', 'This is my awsome text.', date)
        date_format = date.strftime("%d/%m/%Y %H:%M:%S")

        expected = f"ID: 3, Title: Test Post, Date: {date_format}\nPost content:\nThis is my awsome text.\n"
        self.assertEqual(expected, p.__str__())
