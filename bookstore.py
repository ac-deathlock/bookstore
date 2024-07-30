from models.book import Book
from models.order import Order
from models.user import User


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Bookstore(metaclass=Singleton):
    """
    A class representing a bookstore.
    Implementing this as a singleton class as we would need only a single instance for this

    Attributes:
    books: A dictionary of books with book ID as key and Book object as value.
    users: A dictionary of users with user ID as key and User object as value.
    orders: A dictionary of orders with order ID as key and Order object as value.

    Methods:
    add_book: Add a book to the bookstore.
    list_books: List all available books in the bookstore.
    register_user: Register a user in the bookstore.
    list_users: List all registered users in the bookstore.
    create_order: Create an order in the bookstore.
    """

    def __init__(self):
        """
        Initialize the Bookstore with empty dictionaries for books, users, and orders.
        """
        self.books = {}
        self.users = {}
        self.orders = {}

    def add_book(self, book: Book):
        """
        Add a book to the bookstore.

        Args:
        book: Book object to be added to the bookstore.

        Returns:
        None
        """
        self.books.update({book.id: book})

    def list_books(self):
        """
        List all available books in the bookstore.

        Returns:
        None
        """
        if not self.books:
            print("No books available.")
        else:
            for _, book in self.books.items():
                print(book)

    def register_user(self, user: User):
        """
        Register a user in the bookstore.

        Args:
        user: User object to be registered in the bookstore.

        Returns:
        None
        """
        self.users.update({user.id: user})

    def list_users(self):
        """
        List all registered users in the bookstore.

        Returns:
        None
        """
        if not self.users:
            print("No users registered.")
        else:
            for _, user in self.users.items():
                print(user)

    def create_order(self, order: Order) -> Order:
        """
        Create an order in the bookstore.

        Args:
        order: Order object to be created in the bookstore.

        Returns:
        order: The created Order object.
        """
        self.orders.update({order.id: order})
        return order
