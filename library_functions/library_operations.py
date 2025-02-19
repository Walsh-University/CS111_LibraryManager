from .book import Book


class Library:

    def __init__(self, books=None):
        self.books = books if books is not None else {}

    def add_book(self, book: Book):
        """Add a new book to the library"""
        if not isinstance(book, Book):
            raise ValueError("Invalid book")
        if book is None or book.title is None:
            return
        title = book.title
        self.books[title] = book

    def remove_book(self, title: str):
        """Remove a book from the library by title"""
        del self.books[title]

    def mark_as_read(self, title):
        """Mark a book as read"""
        book = self.books[title]
        book.read_status = True

    def get_books_by_author(self, author):
        """Return all books by a specific author"""
        books_by_author = []
        for title, book in self.books.items():
            if book.author == author:
                books_by_author.append(title)
        return books_by_author

    def get_book(self, title):
        """Return a book by title"""
        return self.books.get(title)

    def show_statistics(self):
        if not self.books:
            return "Library is empty"

        average_year = sum(book.year for book in self.books.values()) / len(self.books)
        total_title_length = sum(len(title) for title in self.books.keys())
        oldest_year = min(book.year for book in self.books.values())
        oldest_book = next(value.title for value in self.books.values() if value.year == oldest_year)

        summary = "\nLibrary Summary:\n" + "-" * 40
        summary += "\n".join(
            [f"1. {book.title} by {book.author} ({book.year})" for book in self.books.values()])
        summary += "\n\nStatistics:\n" + "-" * 40
        summary += f"\nAverage publication year: {average_year:.0f}"
        summary += f"\nTotal characters in titles: {total_title_length}"
        summary += f"\nOldest book: {oldest_book} ({oldest_year})"

        return summary

    def __iter__(self):
        return iter(self.books.values())

    def load_books(self, book_loader):
        """Load books from a file"""
        self.books = book_loader.load()
        return self.books
