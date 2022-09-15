from unittest import TestCase

from unittest.mock import patch
import my_app.app as app


class AppTest(TestCase):
    def test_list_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.list_blogs()
            mocked_print.assert_called_with("Blog list empty!\n")

    def test_menu(self):
        with patch('builtins.ord') as mocked_input:
            with patch('builtins.input'):
                app.menu()
                mocked_input.assert_called_with()

    # def test_list_blogs_one(self):
    #     b = Blog("Cars", "Tom Don",)

    #     with patch('builtins.print') as mocked_print:
    #         app.list_blogs([b])
    #         mocked_print.assert_called_with("Type blog number to select (Press 'b' to go back.): ")

# will run all the tests
# if __name__ == "main":
#     unittest.main()
