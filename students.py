# library_manager.py
# Basic Library Manager
# Demonstrates variables, input/output, and basic calculations

def add_book(books, title, author, year, genre, read_status):
    """Add a new book to the library"""
    new_book = {'title': '1984', 'author': 'George Orwell', 'year': 1949, 'genre': 'Science fiction',
                'read_status': False}
    books.append(new_book)
    # create a dictionary    


def remove_book(books, title):
    """Remove a book from the library by title"""
    for index, book in enumerate(books):
        if book['title'] == title:
            del books[index]
            return True  # Book found and removed
    return False  # Book not found


def mark_as_read(books, title):
    """Mark a book as read"""
    # Mark book as read

    marked = mark_as_read(library, "1984")

    # Check if book was marked and print the updated library
    if marked:
        print("Book marked as read successfully.")
    else:
        print("Book not found.")


def get_books_by_author(books, author):
    """Return all books by a specific author"""
    pass


def main():
    # Welcome message
    print("\nWelcome to My Library Manager!")
    print("Please enter information for three books.\n")

    # Variables for Book 1
    print("Book 1:")
    title1 = input("Enter title: ").strip()
    author1 = input("Enter author: ").strip()
    year1 = int(input("Enter publication year: ").strip())
    print(f"Added: {title1} by {author1} ({year1})\n")

    # Variables for Book 2
    print("Book 2:")
    title2 = input("Enter title: ").strip()
    author2 = input("Enter author: ").strip()
    year2 = int(input("Enter publication year: ").strip())
    print(f"Added: {title2} by {author2} ({year2})\n")

    # Variables for Book 3
    print("Book 3:")
    title3 = input("Enter title: ").strip()
    author3 = input("Enter author: ").strip()
    year3 = int(input("Enter publication year: ").strip())
    print(f"Added: {title3} by {author3} ({year3})\n")

    # Calculate statistics
    average_year = (year1 + year2 + year3) / 3
    total_title_length = len(title1) + len(title2) + len(title3)

    # Find oldest book
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
