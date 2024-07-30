from bookstore import Bookstore
from handlers.order_handler import place_order
from handlers.validators import ValidateOrder, ValidateBookOrder, ValidateCustomerId
from models.user import User


def create_cart(store: Bookstore):
    """
    View to create a cart for a user in the bookstore.

    Args:
    store: Bookstore object representing the bookstore.

    Returns:
    None

    Raises:
    Exception: If the user is not found, If user is not a Customer
                if book is not found or quantity is less.
    """
    print("\nCreate Cart:")
    ValidateOrder().validate(store)
    user_id = int(input("Enter user ID to create a cart for: ").strip())
    user = ValidateCustomerId().validate(store=store, user_id=user_id)
    print(f"Creating cart for {user.name}")

    while True:
        print("Cart")
        action = int(
            input(
                "Enter 1 to add more books to cart or 2 to place order or "
                "3 to view Cart or any other key to exit cart: "
            ).strip()
        )
        if action == 1:
            add_books_in_cart(store, user)
        elif action == 2:
            try:
                place_order(store, user)
            except ValueError as e:
                print(f"Error: {e}")
            break
        elif action == 3:
            print(user.cart.list_cart_items())
        else:
            print("Exiting cart")
            break


def add_books_in_cart(store: Bookstore, user: User):
    """
    Sub view to add books in cart
    :param store:
    :param user:
    :return: None
    """
    book_id = int(input("Enter book ID to add to cart: ").strip())
    quantity = int(input("Enter quantity: ").strip())

    book = ValidateBookOrder().validate(store, book_id=book_id, quantity=quantity)
    user.cart.add_book(book, quantity)
    print(f"Added {quantity} instances of book ID {book_id} to cart.")
