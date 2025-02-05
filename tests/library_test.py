from assertpy import assert_that

from library_functions.library_operations import Library


def test_add_book():
    library = Library()
    book = {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False}
    library.add_book(book)
    assert_that(library).contains("Book One")
    assert_that(library["Book One"]).is_equal_to(
        {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False})


def test_remove_book():
    library = Library()
    book = {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False}
    library.add_book(book)
    library.remove_book("Book One")
    assert_that(library).does_not_contain("Book One")


def test_mark_as_read():
    library = Library()
    library.add_book({"Book One": {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False}})
    library.mark_as_read("Book One")
    assert_that(library["Book One"]["read_status"]).is_true()


def test_get_books_by_author():
    library = Library()
    books = {
        "Book One": {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False},
        "Book Two": {"title": "Book Two", "author": "Author B", "year": 2001, "read_status": True},
        "Book Three": {"title": "Book Three", "author": "Author A", "year": 2002, "read_status": False},
    }
    for books in books.values():
        library.add_book(books)
    books_by_author_a = library.get_books_by_author("Author A")
    assert_that(books_by_author_a).contains_only("Book One", "Book Three")


def test_get_books_by_author_no_match():
    library = Library()
    book = {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False}
    library.add_book(book)
    books_by_author_c = library.get_books_by_author("Author C")
    assert_that(books_by_author_c).is_empty()
