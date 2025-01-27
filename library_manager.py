from library_functions.library_operations import (
    add_book,
    remove_book,
    mark_as_read,
    get_books_by_author, show_statistics,
)


def prompt_for_book_info():
    # Variables for Book 1
    print("Book 1:")
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    read_status = input("Have you read this book? (y/n) ")
    if read_status == "y":
        read_status = True
    else:
        read_status = False
    return {'title': title, 'author': author, 'year': year, 'read_status': read_status}


def prompt_for_remove(library):
    remove = input("Would you like to remove a book? (y/n) ").strip()
    if remove == "y":
        title = input("Enter title of book to remove: ").strip()
        remove_book(library, title)
        print(f"Removed: {title}\n")


def prompt_for_read_status(library):
    mark_read = input("Would you like to mark a book as read? (y/n) ").strip()
    if mark_read == "y":
        title = input("Enter title of book to mark as read: ").strip()
        mark_as_read(library, title)
        print(f"Marked as read: {title}\n")


def prompt_for_author(library):
    get_book = input("Would you like to get a book by author? (y/n) ").strip()
    if get_book == "y":
        author = input("Enter author of book to get: ").strip()
        books_by_author = get_books_by_author(library, author)
        print(f"Books: {books_by_author}\n")


def main():
    library = {}
    # Welcome message
    print("\nWelcome to My Library Manager!")
    print("Please enter information for three books.\n")

    book = prompt_for_book_info()
    add_book(library, book)
    print(f"Added: {book['title']} by {book['author']} ({book['year']})\n")

    prompt_for_remove(library)

    prompt_for_read_status(library)

    prompt_for_author(library)

    show_statistics(library)


# Run the program
if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("\nError: Publication year must be a valid number.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
