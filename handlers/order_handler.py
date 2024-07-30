from bookstore import Bookstore
from models.order import Order
from models.user import User


def place_order(store: Bookstore, user: User):
    """
    Place an order for the user and update book quantities.

    Args:
    store: Bookstore object representing the bookstore.
    user: User object representing the user placing the order.

    Returns:
    None
    """
    order_id = len(store.orders) + 1
    order = Order(order_id, user)
    order.add_cart_items(user.cart.items)
    store.create_order(order)
    update_book_quantity(user.cart.items)
    print("\nOrder Placed:")
    print(order)
    user.cart.clear()


def update_book_quantity(cart_items: dict):
    """
    Update the quantity of books in the store based on the items in the cart.

    Args:
    cart_items: List of tuples containing book and quantity in the cart.

    Returns:
    None
    """
    for book, quantity in cart_items.items():
        updated_quantity = book.quantity - quantity
        book.update_book(quantity=updated_quantity)
        print(f"Book stock updated for book id {book.id}")
