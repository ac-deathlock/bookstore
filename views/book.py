from bookstore import Bookstore
from models.book import Book


def add_book(store: Bookstore):
    """
    Add a book to the bookstore.

    Args:
    store: Bookstore object representing the bookstore.

    Returns:
    None
    """
    print("\nAdd Book:")
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    try:
        price = float(input("Enter book price: ").strip())
    except ValueError:
        print("Invalid price. Book addition failed.")
        return
    try:
        quantity = int(input("Enter number of books: ").strip())
    except ValueError:
        print("Invalid Quantity. Book addition failed.")
        return

    book_id = len(store.books) + 1
    book = Book(book_id, title, author, price, quantity)
    store.add_book(book)
    print(f"Book '{book.title}' added successfully.")
