from library_functions.library_operations import (
    add_book,
    remove_book,
    mark_as_read,
    get_books_by_author,
)


def main():
    library = {}
    # Welcome message
    print("\nWelcome to My Library Manager!")
    print("Please enter information for three books.\n")

    # Variables for Book 1
    print("Book 1:")
    title1 = input("Enter title: ")
    author1 = input("Enter author: ")
    year1 = int(input("Enter publication year: "))
    add_book(library, title1, author1, year1, False)
    print(f"Added: {title1} by {author1} ({year1})\n")

    # Variables for Book 2
    print("Book 2:")
    title2 = input("Enter title: ").strip()
    author2 = input("Enter author: ").strip()
    year2 = int(input("Enter publication year: ").strip())
    add_book(library, title2, author2, year2, False)
    print(f"Added: {title2} by {author2} ({year2})\n")

    # Variables for Book 3
    print("Book 3:")
    title3 = input("Enter title: ").strip()
    author3 = input("Enter author: ").strip()
    year3 = int(input("Enter publication year: ").strip())
    add_book(library, title3, author3, year3, False)
    print(f"Added: {title3} by {author3} ({year3})\n")

    remove = input("Would you like to remove a book? (y/n) ").strip()
    if remove == "y":
        title = input("Enter title of book to remove: ").strip()
        remove_book(library, title)
        print(f"Removed: {title}\n")

    mark_read = input("Would you like to mark a book as read? (y/n) ").strip()
    if mark_read == "y":
        title = input("Enter title of book to mark as read: ").strip()
        mark_as_read(library, title)
        print(f"Marked as read: {title}\n")

    get_book = input("Would you like to get a book by author? (y/n) ").strip()
    if get_book == "y":
        author = input("Enter author of book to get: ").strip()
        books_by_author = get_books_by_author(library, author)
        print(f"Books: {books_by_author}\n")

    # Calculate statistics
    average_year = (year1 + year2 + year3) / 3
    total_title_length = len(title1) + len(title2) + len(title3)

    # Find the oldest book
    oldest_year = min(year1, year2, year3)
    if oldest_year == year1:
        oldest_book = title1
    elif oldest_year == year2:
        oldest_book = title2
    else:
        oldest_book = title3

    # Display summary
    print("\nLibrary Summary:")
    print("-" * 40)
    print(f"1. {title1} by {author1} ({year1})")
    print(f"2. {title2} by {author2} ({year2})")
    print(f"3. {title3} by {author3} ({year3})")

    # Display statistics
    print("\nStatistics:")
    print("-" * 40)
    print(f"Average publication year: {average_year:.0f}")
    print(f"Total characters in titles: {total_title_length}")
    print(f"Oldest book: {oldest_book} ({oldest_year})")


# Run the program
if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("\nError: Publication year must be a valid number.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
