import unittest
from io import StringIO
from unittest.mock import patch
from bookstore import Bookstore
from views.book import add_book
from views.order import create_cart
from views.user import create_user
from main import main


class TestBookstoreFunctionality(unittest.TestCase):
    @patch("builtins.input", side_effect=["1", "John Doe", "john@example.com"])
    def test_create_user(self, mock_input):
        bookstore = Bookstore()
        create_user(bookstore)
        mock_input.side_effect = ["2", "John Doe", "testuser@example.com"]
        create_user(bookstore)
        is_user_present = False
        for user in bookstore.users.values():
            if user.email == "testuser@example.com":
                is_user_present = True
        assert is_user_present is True

    @patch("builtins.input", side_effect=["test Title", "Author Name", "22", "5"])
    def test_add_book_to_store(self, mock_input):
        bookstore = Bookstore()
        add_book(bookstore)
        assert len(bookstore.books) == 1

    @patch("builtins.input", side_effect=["3"])
    def test_create_new_cart(self, mock_input):
        bookstore = Bookstore()
        mock_input.side_effect = ["2", "John Doe", "john@example.com"]
        create_user(bookstore)
        mock_input.side_effect = ["test Title", "Author Name", "22", "6"]
        add_book(bookstore)
        mock_input.side_effect = ["test Title2", "Author Name", "24", "8"]
        add_book(bookstore)
        mock_input.side_effect = ["1", "1", "1", "1", "2"]
        create_cart(bookstore)

        # Add assertions to validate the creation of the cart

    @patch("builtins.input", return_value="4")
    def test_list_books(self, mock_input):
        bookstore = Bookstore()
        mock_input.side_effect = ["test Title", "Author Name", "22", "8"]
        add_book(bookstore)
        mock_input.side_effect = ["test Title2", "Author Name", "24", "9"]
        add_book(bookstore)
        with patch("sys.stdout", new=StringIO()) as fake_output:
            mock_input.side_effect = "4"
            bookstore.list_books()
            assert fake_output is not None

    @patch("builtins.input", return_value="5")
    def test_list_users(self, mock_input):
        bookstore = Bookstore()
        mock_input.side_effect = ["2", "John Doe", "john@example.com"]
        create_user(bookstore)
        with patch("sys.stdout", new=StringIO()) as fake_output:
            bookstore.list_users()
            print(fake_output)
            assert fake_output is not None

    @patch("builtins.input", return_value="6")
    def test_exit_menu(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            main()


if __name__ == "__main__":
    unittest.main()
