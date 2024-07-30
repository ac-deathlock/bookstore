from models.book import Book
from models.user import User


class Cart:
    """
    A class representing a cart for a user in the bookstore.

    Attributes:
    user: User object representing the user associated with the cart.
    items: List of tuples containing book and quantity added to the cart.

    Methods:
    add_book: Add a book with a specified quantity to the cart.
    clear: Clear all items from the cart.
    total_cost: Calculate the total cost of all items in the cart.
    list_cart_items: List all items in the cart along with their quantities.
    __str__: String representation of the cart including user, items, and total cost.
    """

    def __init__(self, user: User):
        """
        Initialize the Cart with a user and an empty list of items.

        Args:
        user: User object representing the user associated with the cart.
        """
        self.user = user
        self.items = {}

    def add_book(self, book: Book, quantity: int):
        """
        Add a book with a specified quantity to the cart.

        Args:
        book: Book object to be added to the cart.
        quantity: Integer representing the quantity of the book to be added.

        Returns:
        None
        """
        if self.items.get(book):
            self.items[book] += quantity
        else:
            self.items.update({book: quantity})

    def clear(self):
        """
        Clear all items from the cart.

        Returns:
        None
        """
        self.items = {}

    def total_cost(self) -> float:
        """
        Calculate the total cost of all items in the cart.

        Returns:
        float: Total cost of all items in the cart.
        """
        return sum(
            book_instance.price * quantity
            for book_instance, quantity in self.items.items()
        )

    def list_cart_items(self):
        """
        List all items in the cart along with their quantities.

        Returns:
        None
        """
        for item, quantity in self.items.items():
            print("Book titles ---- Ordered Quantity")
            print(item.title, "----", quantity)
        print("Total cost of items is :Rs", self.total_cost())

    def __str__(self):
        """
        String representation of the cart including user, items, and total cost.

        Returns:
        str: String representation of the cart.
        """
        items_str = "\n".join(
            [
                f"{book_instance.book.title} x{quantity} - Rs{book_instance.book.price * quantity:.2f}"
                for book_instance, quantity in self.items
            ]
        )
        return f"User: {self.user.name}\nItems:\n{items_str}\nTotal Cost: Rs{self.total_cost():.2f}"
