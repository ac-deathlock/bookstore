class User:
    """
    A class representing a user in the bookstore.

    Attributes:
    id: Unique identifier for the user.
    name: Name of the user.
    email: Email address of the user.
    cart: Cart object associated with the user.

    Methods:
    user_type: Get the type of the user.
    __str__: String representation of the user.
    """

    def __init__(self, _id, name, email):
        """
        Initialize the User with a unique identifier, name, and email.

        Args:
        _id: Unique identifier for the user.
        name: Name of the user.
        email: Email address of the user.
        """
        self.id = _id
        self.name = name
        self.email = email
        self.cart = None

    def user_type(self):
        """
        Get the type of the user.

        Returns:
        str: Type of the user.
        """
        return self.__class__.__name__

    def __str__(self):
        """
        String representation of the user.

        Returns:
        str: String representation of the user.
        """
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}, Type: {self.user_type()}"


class Customer(User):
    """
    A class representing a customer, inheriting from User.
    This class inherits all attributes and methods from the User class.
    """

    pass


class Admin(User):
    """
    A class representing an admin, inheriting from User.
    This class inherits all attributes and methods from the User class.
    """

    pass
