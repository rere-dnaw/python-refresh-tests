from unittest import TestCase
from unittest.mock import patch
from blog import Blog
import app


class BlogTest(TestCase):
    def test_list_blogs(self):
        b = Blog("Cars", "Tom Don")

        with patch('builtins.print') as mocked_print:
            app.list_blogs(b)
            mocked_print.assert_called_with('\nWhat do you want to do?\n1)List Posts.\n2)Add Post\n3)Back.')
