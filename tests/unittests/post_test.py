import unittest
from datetime import datetime
from my_app.post import Post


class PostTest(unittest.TestCase):
    def setUp(self) -> None:
        self.date = datetime.now()
        self.p = Post('Test', 'Testing Content', self.date)
        self.p2 = Post.create_post('Test', 'Testing Content', self.date)

    def tearDown(self) -> None:
        pass

    def test_create_post(self):
        self.assertEqual('Test', self.p.title)
        self.assertEqual('Testing Content', self.p.content)
        self.assertEqual(self.date, self.p.date)
        self.assertEqual(self.p.postID, 0)

    def test_create_post_class(self):
        self.assertEqual('Test', self.p2.title)
        self.assertEqual('Testing Content', self.p2.content)
        self.assertEqual(self.date, self.p2.date)
        self.assertEqual(self.p2.postID, 3)

    def test_json(self):
        expected = {'ID': 4, 'Title': 'Test',
                    'Date': self.date, 'Content': 'Testing Content'}

        self.assertDictEqual(expected, self.p.json())

    def test_repr(self):
        expected = f'Post<6,Test,{self.date},Testing Content>'
        self.assertEqual(expected, self.p.__repr__())

    def test_str(self):
        date_format = self.date.strftime("%d/%m/%Y %H:%M:%S")

        expected = f"ID: 8, Title: Test, Date: {date_format}\n"\
            "Post content:\nTesting Content\n"

        self.assertEqual(expected, self.p.__str__())


# will run all the tests
if __name__ == "main":
    unittest.main()
