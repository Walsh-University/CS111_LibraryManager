from library_functions.library_operations import Library


def prompt_for_book_info(library):
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    read_status = input("Have you read this book? (y/n) ")
    if read_status == "y":
        read_status = True
    else:
        read_status = False
    book = {'title': title, 'author': author, 'year': year, 'read_status': read_status}
    library.add_book(book)
    print(f"Added: {book['title']} by {book['author']} ({book['year']})\n")


def prompt_for_remove(library):
    title = input("Enter title of book to remove: ").strip()
    library.remove_book(title)
    print(f"Removed: {title}\n")


def prompt_for_read_status(library):
    title = input("Enter title of book to mark as read: ").strip()
    library.mark_as_read(title)
    print(f"Marked as read: {title}\n")


def prompt_for_author(library):
    author = input("Enter author of book to get: ").strip()
    books_by_author = library.get_books_by_author(author)
    print(f"Books: {books_by_author}\n")


def print_menu():
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Mark a book as read")
    print("4. Get books by author")
    print("5. Show statistics")
    print("6. Exit")


def main():
    # Welcome message
    print("\nWelcome to My Library Manager!")
    print("Please enter information for three books.\n")

    library_manager = Library()

    while True:
        print_menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            prompt_for_book_info(library_manager)
        elif choice == 2:
            prompt_for_remove(library_manager)
        elif choice == 3:
            prompt_for_read_status(library_manager)
        elif choice == 4:
            prompt_for_author(library_manager)
        elif choice == 5:
            library_manager.show_statistics()
        elif choice == 6:
            print("Goodbye!")
            exit()


# Run the program
if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("\nError: Publication year must be a valid number.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
