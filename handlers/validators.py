from abc import ABC, abstractmethod
from bookstore import Bookstore
from models.user import Customer


class Validator(ABC):
    """
    Abstract base class for validators.
    """

    @abstractmethod
    def validate(self, *args, **kwargs):
        """
        Abstract method to be implemented by concrete validators.
        """
        pass


class ValidateUser(Validator):
    """
    Validator for user validation.
    """

    def validate(self, store: Bookstore):
        """
        Validate the presence of users in the store.

        Args:
        store: Bookstore object representing the bookstore.

        Raises:
        Exception: If no users are available in the store.
        """
        if not store.users:
            print("No users available. Please create a user first.")
            raise Exception("No users in store")


class ValidateCustomerId(Validator):
    """
    Validator for customer ID validation.
    """

    def validate(self, store: Bookstore, **kwargs):
        """
        Validate the user ID and its type.

        Args:
        store: Bookstore object representing the bookstore.
        **kwargs: Additional keyword arguments.

        Returns:
        User: The validated user object.

        Raises:
        Exception: If the user is not found or is not a customer.
        """
        user_id = kwargs.get("user_id")
        user = store.users.get(user_id)
        if not user:
            print(f"User not found: {user_id}")
            raise Exception("User not found")
        if not isinstance(user, Customer):
            print("Only Customer Users have cart")
            raise Exception("Only Customer Users have cart")
        return user


class ValidateBookOrder(Validator):
    """
    Validator for book order validation.
    """

    def validate(self, store: Bookstore, **kwargs):
        """
        Validate the book ID and quantity for placing a book order.

        Args:
        store: Bookstore object representing the bookstore.
        **kwargs: Additional keyword arguments.

        Returns:
        Book: The validated book object.

        Raises:
        Exception: If the book is not found or the quantity exceeds stock.
        """
        try:
            book_id = kwargs["book_id"]
            quantity = kwargs["quantity"]
        except KeyError:
            raise Exception("book_id and quantity are mandatory to place book order")
        book = store.books.get(book_id)
        if not book:
            print(f"book not found: {book_id}")
            raise Exception("Book not found")
        if book.quantity < quantity:
            print(
                f"Only {book.quantity} books with id {book.id} are left please change the order quantity"
            )
            raise Exception("Book quantity exceeds stock")
        return book


class ValidateBook(Validator):
    """
    Validator for book validation.
    """

    def validate(self, store: Bookstore):
        """
        Validate the presence of books in the store.

        Args:
        store: Bookstore object representing the bookstore.

        Raises:
        Exception: If no books are available in the store.
        """
        if not store.books:
            print("No books available. Please create a book first.")
            raise Exception("no books in store")


class ValidateOrder(Validator):
    """
    Validator for order validation.
    """

    validators = [ValidateUser(), ValidateBook()]

    def validate(self, store: Bookstore):
        """
        Validate the order using multiple validators.

        Args:
        store: Bookstore object representing the bookstore.

        Raises:
        Exception: If any of the validators fail.
        """
        for validator in self.validators:
            validator.validate(store)
