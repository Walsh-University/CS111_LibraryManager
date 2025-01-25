def add_book(books: dict, book: dict):
    """Add a new book to the library"""
    title = book["title"]
    books[title] = book


def remove_book(books: dict, title: str):
    """Remove a book from the library by title"""
    del books[title]


def mark_as_read(books, title):
    """Mark a book as read"""
    book = books[title]
    book["read_status"] = True


def get_books_by_author(books, author):
    """Return all books by a specific author"""
    books_by_author = []
    for title, book in books.items():
        if book["author"] == author:
            books_by_author.append(title)
    return books_by_author


def show_statistics(library):
    if not library:
        return "Library is empty"

    average_year = sum(book["year"] for book in library.values()) / len(library)
    total_title_length = sum(len(title) for title in library.keys())
    oldest_year = min(book["year"] for book in library.values())
    oldest_book = next(value["title"] for value in library.values() if value["year"] == oldest_year)

    summary = "\nLibrary Summary:\n" + "-" * 40
    summary += "\n".join([f"1. {book['title']} by {book['author']} ({book['year']})" for book in library.values()])
    summary += "\n\nStatistics:\n" + "-" * 40
    summary += f"\nAverage publication year: {average_year:.0f}"
    summary += f"\nTotal characters in titles: {total_title_length}"
    summary += f"\nOldest book: {oldest_book} ({oldest_year})"

    return summary
