from bookstore import Bookstore
from views.book import add_book
from views.order import create_cart
from views.user import create_user


def main():
    """
    Main function to run the bookstore management system.
    Displays a menu for various operations and executes the selected operation.

    Args:
    None

    Returns:
    None
    """
    bookstore = Bookstore()

    while True:
        try:
            print("\nMenu:")
            print("1. Create User")
            print("2. Add Book to Store")
            print("3. Cart")
            print("4. List Books")
            print("5. List Users")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                create_user(bookstore)
            elif choice == "2":
                add_book(bookstore)
            elif choice == "3":
                create_cart(bookstore)
            elif choice == "4":
                print("\nAvailable Books:")
                bookstore.list_books()
            elif choice == "5":
                print("\nRegistered Users:")
                bookstore.list_users()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    main()
