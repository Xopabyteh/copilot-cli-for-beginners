def print_menu():
    print("\n📚 Book Collection App")
    print("1. Add a book")
    print("2. List books")
    print("3. Mark book as read")
    print("4. Remove a book")
    print("5. Exit")


def get_user_choice() -> str:
    while True:
        choice = input("Choose an option (1-5): ").strip()
        if not choice:
            print("Please enter a choice.")
            continue
        if not choice.isdigit():
            print("Please enter a number.")
            continue
        return choice


def get_book_details():
    """Prompt the user for book details and return the values.

    Parameters:
        None. This function gathers input interactively from the user.

    Returns:
        tuple[str, str, int]: A tuple of (title, author, year). The title is
        guaranteed to be non-empty. The year is an integer; invalid input
        defaults to 0.
    """
    while True:
        title = input("Enter book title: ").strip()
        if title:
            break
        print("Title cannot be empty.")

    author = input("Enter author: ").strip()

    year_input = input("Enter publication year: ").strip()
    try:
        year = int(year_input)
    except ValueError:
        print("Invalid year. Defaulting to 0.")
        year = 0

    return title, author, year


def print_books(books):
    if not books:
        print("No books in your collection.")
        return

    print("\nYour Books:")
    for index, book in enumerate(books, start=1):
        status = "✅ Read" if book.read else "📖 Unread"
        print(f"{index}. {book.title} by {book.author} ({book.year}) - {status}")
