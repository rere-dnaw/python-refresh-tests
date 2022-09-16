import unittest

from unittest.mock import patch
import my_app.app as app
import my_app.statics.lang_eng as lang_str


class AppTest(unittest.TestCase):
    def test_list_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.list_blogs()
            mocked_print.assert_called_with("Blog list empty!\n")

    def test_menu(self):
        with patch('builtins.ord') as mocked_ord:
            mocked_ord.return_value = 52
            with patch('builtins.input') as mocker_input:
                app.menu()
                mocker_input.assert_called_with(lang_str.MAIN_MENU_OPT)

    # def test_menu_list_blog(self):
    #     with patch('builtins.ord') as mocked_ord:
    #         with patch('builtins.input') as mocked_input:
    #             with patch('app.list_blogs') as mocker_app_list:
    #                 mocked_ord.return_value = 49
    #                 mocked_input.return_value = '1'
    #                 app.menu()
    #                 mocker_app_list.assert_called()
