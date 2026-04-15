import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from books import Book
import utils


class TestPrintMenu:
    """Tests for print_menu."""

    def test_print_menu_outputs_options(self, capsys):
        utils.print_menu()
        output = capsys.readouterr().out

        assert "Book Collection App" in output
        assert "1. Add a book" in output
        assert "2. List books" in output
        assert "3. Mark book as read" in output
        assert "4. Remove a book" in output
        assert "5. Exit" in output


class TestGetUserChoice:
    """Tests for get_user_choice."""

    @pytest.mark.parametrize("inputs,expected,expected_messages", [
        (["3"], "3", []),
        (["", "2"], "2", ["Please enter a choice."]),
        (["abc", "5"], "5", ["Please enter a number."]),
        (["", "not-a-number", "1"], "1", ["Please enter a choice.", "Please enter a number."]),
    ])
    def test_get_user_choice_validates_input(self, monkeypatch, capsys, inputs, expected, expected_messages):
        input_iter = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(input_iter))

        result = utils.get_user_choice()

        output = capsys.readouterr().out
        for message in expected_messages:
            assert message in output
        assert result == expected


class TestGetBookDetails:
    """Tests for get_book_details."""

    def test_get_book_details_happy_path(self, monkeypatch):
        inputs = iter(["Dune", "Frank Herbert", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        title, author, year = utils.get_book_details()

        assert title == "Dune"
        assert author == "Frank Herbert"
        assert year == 1965

    def test_get_book_details_requires_title(self, monkeypatch, capsys):
        inputs = iter(["", "   ", "Foundation", "Isaac Asimov", "1951"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        title, author, year = utils.get_book_details()

        output = capsys.readouterr().out
        assert "Title cannot be empty." in output
        assert title == "Foundation"
        assert author == "Isaac Asimov"
        assert year == 1951

    def test_get_book_details_invalid_year_defaults_to_zero(self, monkeypatch, capsys):
        inputs = iter(["Neuromancer", "William Gibson", "not-a-year"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        title, author, year = utils.get_book_details()

        output = capsys.readouterr().out
        assert "Invalid year. Defaulting to 0." in output
        assert title == "Neuromancer"
        assert author == "William Gibson"
        assert year == 0


class TestPrintBooks:
    """Tests for print_books."""

    def test_print_books_empty(self, capsys):
        utils.print_books([])
        output = capsys.readouterr().out
        assert "No books in your collection." in output

    def test_print_books_outputs_read_status(self, capsys):
        books = [
            Book(title="1984", author="George Orwell", year=1949, read=True),
            Book(title="The Hobbit", author="J.R.R. Tolkien", year=1937, read=False),
        ]

        utils.print_books(books)
        output = capsys.readouterr().out

        assert "Your Books:" in output
        assert "1984 by George Orwell (1949) - ✅ Read" in output
        assert "The Hobbit by J.R.R. Tolkien (1937) - 📖 Unread" in output
