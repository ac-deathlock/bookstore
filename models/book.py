class Book:
    """
    A class representing a book in the bookstore.

    Attributes:
    id: Unique identifier for the book.
    title: Title of the book.
    author: Author of the book.
    price: Price of the book.
    quantity: Quantity of the book available in the store.

    Methods:
    __str__: String representation of the book.
    update_book: Update the attributes of the book.

    """

    def __init__(self, _id, title, author, price, quantity):
        """
        Initialize the Book with a unique identifier, title, author, price, and quantity.

        Args:
        _id: Unique identifier for the book.
        title: Title of the book.
        author: Author of the book.
        price: Price of the book.
        quantity: Quantity of the book available in the store.
        """
        self.id = _id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        String representation of the book.

        Returns:
        str: String representation of the book.
        """
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Price: Rs{self.price:.2f}, Quantity: {self.quantity}"

    def update_book(self, **kwargs):
        """
        Update the attributes of the book with the provided keyword arguments.

        Args:
        **kwargs: Keyword arguments representing the attributes to update.

        Returns:
        None
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
