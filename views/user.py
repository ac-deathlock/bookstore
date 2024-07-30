from bookstore import Bookstore
from handlers.user_handler import UserFactory


def create_user(store: Bookstore):
    """
    Create a new user and register them in the store.

    Args:
    store: The store object where the user will be registered.

    Returns:
    None
    """
    print("\nCreate User:")
    user_type = input("Enter '1' to create Admin or '2' to create Customer: ").strip()
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    user_id = len(store.users) + 1
    user = UserFactory.create_user(user_id, user_type, name, email)
    store.register_user(user)
    print(f"User {name} created successfully as {user.user_type()}")
