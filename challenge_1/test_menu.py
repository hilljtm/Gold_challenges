
import unittest
import cafe_menu_repo as repo
from cafe_menu_repo import Menu


class TestMenu(unittest.TestCase):

    def menu(self, meal_number, meal_name, description, ingredients, price):
        
        self.add_menu(self.add_menu)
        self.get_menu = []
        self.update_menu

    def test_repo_add_menu_should_show_item_added(self):
        actual = 1
        self.add_menu = menu(5, 'Chicken', 'Hot chicken served fresh', 'legs', 10)
        expected = 1
        self.assertEqual(actual, expected)
   
    def test_repo_delete_menu_should_delete_item_menu(self):
        expected = 0
        self.cafe_menu_repo.delete_menu_item(1)
        actual = len(self.cafe_menu_repo.get_menu)
        self.assertEqual(expected, actual)

    def test_method_item_should_be_deleted(self):
        actual = len(menu.get_menus())
        expected = 1
        self.assertEqual(actual, expected)
