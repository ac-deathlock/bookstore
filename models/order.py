from models.user import User


class Order:
    """
    A class representing an order in the bookstore.

    Attributes:
    id: Unique identifier for the order.
    user: User object representing the user associated with the order.
    items: List of items in the order.

    Methods:
    add_cart_items: Add items from the user's cart to the order.
    total_cost: Calculate the total cost of the order.
    __str__: String representation of the order.
    """

    def __init__(self, order_id: int, user: User):
        """
        Initialize the Order with a unique identifier and a user.

        Args:
        order_id: Unique identifier for the order.
        user: User object representing the user associated with the order.
        """
        self.id = order_id
        self.user = user
        self.items = []
        self.cost = None

    def add_cart_items(self, items: dict):
        """
        Add items from the user's cart to the order.

        Args:
        items: List of items Tuples(Book instance and quantity) to be added to the order.

        Returns:
        None
        """
        self.items = [(k, v) for k, v in items.items()]
        self.update_total_cost()

    def update_total_cost(self) -> float:
        """
        Calculate the total cost of the order and set it in Order Object.

        Returns:
        float: Total cost of the order.
        """
        self.cost = self.user.cart.total_cost()
        return self.cost

    def total_cost(self) -> float:
        """
        Returns:
        float: Total cost of the order.
        """
        return self.cost

    def __str__(self):
        """
        String representation of the order.

        Returns:
        str: String representation of the order.
        """
        items_str = [(item[0].title, item[1]) for item in self.items]
        return f"Order ID: {self.id}\nUser: {self.user.name}\nItems:\n{items_str}\nTotal Cost: Rs{self.total_cost():.2f}"
