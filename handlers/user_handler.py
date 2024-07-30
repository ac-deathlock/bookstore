from models.cart import Cart
from models.user import Admin, Customer


class UserFactory:
    """
    Factory class for creating user objects based on user type.

    This factory pattern is relevant as it encapsulates the object creation logic for different user types,
    providing a centralized place to create user objects based on the user type. It promotes loose coupling
    and separation of concerns by abstracting the object creation process from the client code.
    """

    @staticmethod
    def create_admin(user_id, name, email):
        return Admin(user_id, name, email)

    @staticmethod
    def create_customer(user_id, name, email):
        customer_obj = Customer(user_id, name, email)
        customer_obj.cart = Cart(customer_obj)
        return customer_obj

    @staticmethod
    def create_user(user_id, user_type, name, email):
        """
        Create a user based on the user type.

        Args:
        user_id: Unique identifier for the user.
        user_type: Type of the user (1 for Admin, 2 for Customer).
        name: Name of the user.
        email: Email of the user.

        Returns:
        Admin or Customer: An instance of the corresponding user type based on the user_type.

        Raises:
        Exception: If an invalid user type is selected.
        """
        if user_type == "1":
            return UserFactory.create_admin(user_id, name, email)
        elif user_type == "2":
            return UserFactory.create_customer(user_id, name, email)
        else:
            print("Invalid user type selected")
            raise Exception("Invalid user type selected")
