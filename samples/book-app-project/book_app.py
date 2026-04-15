import sys
from datetime import date
from typing import Callable, Iterable

from books import Book, BookCollection


def show_books(books: Iterable[Book]) -> None:
    """Display books in a user-friendly format."""
    if not books:
        print("No books found.")
        return

    print("\nYour Book Collection:\n")

    for index, book in enumerate(books, start=1):
        status = "✓" if book.read else " "
        print(f"{index}. [{status}] {book.title} by {book.author} ({book.year})")

    print()


def handle_list(collection: BookCollection) -> None:
    books = collection.list_books()
    show_books(books)


def handle_add(collection: BookCollection) -> None:
    print("\nAdd a New Book\n")

    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year_str = input("Year: ").strip()

    try:
        if not title:
            raise ValueError("Title cannot be empty.")
        if not author:
            raise ValueError("Author cannot be empty.")
        if not year_str:
            raise ValueError("Year is required.")

        year = int(year_str)
        current_year = date.today().year
        if year < 1450 or year > current_year:
            raise ValueError(f"Year must be between 1450 and {current_year}.")

        collection.add_book(title, author, year)
        print("\nBook added successfully.\n")
    except ValueError as e:
        print(f"\nError: {e}\n")


def handle_remove(collection: BookCollection) -> None:
    print("\nRemove a Book\n")

    title = input("Enter the title of the book to remove: ").strip()
    if not title:
        print("\nError: Title cannot be empty.\n")
        return

    collection.remove_book(title)

    print("\nBook removed if it existed.\n")


def handle_find(collection: BookCollection) -> None:
    print("\nFind Books by Author\n")

    author = input("Author name: ").strip()
    if not author:
        print("\nError: Author cannot be empty.\n")
        return

    books = collection.find_by_author(author)

    show_books(books)


def show_help() -> None:
    print("""
Book Collection Helper

Commands:
  list     - Show all books
  add      - Add a new book
  remove   - Remove a book by title
  find     - Find books by author
  help     - Show this help message
""")


def main() -> None:
    collection = BookCollection()

    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    handlers: dict[str, Callable[[BookCollection], None]] = {
        "list": handle_list,
        "add": handle_add,
        "remove": handle_remove,
        "find": handle_find,
    }

    if command == "help":
        show_help()
        return

    handler = handlers.get(command)
    if not handler:
        print("Unknown command.\n")
        show_help()
        return

    handler(collection)


if __name__ == "__main__":
    main()
