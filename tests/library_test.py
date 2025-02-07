from assertpy import assert_that

from library_functions.book import Book
from library_functions.library_operations import Library


def test_book_str():
    book = Book()
    book.title = "Book 1"
    book.author = "Author 1"
    book.year = 2000
    print(book)


def make_book(book_count: int = 1):
    books = []
    for i in range(book_count):
        book = Book()
        book.title = "Book " + str(i)
        book.author = "Author " + str(i)
        book.year = 2000 + i
        book.pages = 100 + i
        book.read_status = False
        if book_count == 1:
            return book
        books.append(book)
    return books


def test_add_book():
    library = Library()
    book = make_book()
    library.add_book(book)
    b = library.get_book("Book 0")
    assert_that(b.title).is_equal_to(book.title)


def test_remove_book():
    library = Library()
    book = make_book()
    library.add_book(book)
    library.remove_book("Book 0")
    assert_that(library).does_not_contain("Book 0")


def test_mark_as_read():
    library = Library()
    book = make_book()
    library.add_book(book)
    library.mark_as_read("Book 0")
    b = library.get_book("Book 0")
    assert_that(b.read_status).is_true()


def test_get_books_by_author():
    library = Library()
    books = make_book(3)
    for i in range(len(books)):
        if i == 2:
            books[i].author = "Author 0"
        library.add_book(books[i])
    books_by_author_a = library.get_books_by_author("Author 0")
    assert_that(books_by_author_a).contains_only("Book 0", "Book 2")


def test_get_books_by_author_no_match():
    library = Library()
    book = make_book()
    library.add_book(book)
    books_by_author_c = library.get_books_by_author("Author 2")
    assert_that(books_by_author_c).is_empty()
