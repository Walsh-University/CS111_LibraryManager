from assertpy import assert_that

from library_functions.library_operations import add_book, remove_book, mark_as_read, get_books_by_author


def test_add_book():
    library = {}
    book = {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False}
    add_book(library, book)
    assert_that(library).contains("Book One")
    assert_that(library["Book One"]).is_equal_to(
        {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False})


def test_remove_book():
    library = {"Book One": {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False}}
    remove_book(library, "Book One")
    assert_that(library).does_not_contain("Book One")


def test_mark_as_read():
    library = {"Book One": {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False}}
    mark_as_read(library, "Book One")
    assert_that(library["Book One"]["read_status"]).is_true()


def test_get_books_by_author():
    library = {
        "Book One": {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False},
        "Book Two": {"title": "Book Two", "author": "Author B", "year": 2001, "read_status": True},
        "Book Three": {"title": "Book Three", "author": "Author A", "year": 2002, "read_status": False},
    }
    books_by_author_a = get_books_by_author(library, "Author A")
    assert_that(books_by_author_a).contains_only("Book One", "Book Three")


def test_get_books_by_author_no_match():
    library = {
        "Book One": {"title": "Book One", "author": "Author A", "year": 2000, "read_status": False},
    }
    books_by_author_c = get_books_by_author(library, "Author C")
    assert_that(books_by_author_c).is_empty()
