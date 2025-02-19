from .book import Book, BookCategory


class BookFileReader:

    def __init__(self, file_path: str = 'books.csv'):
        self.books = {}
        self.file_path = file_path

    def load(self) -> dict[str, Book]:
        try:
            with open(self.file_path, 'r') as file:
                file.readline()  # Skip the header line
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 6:
                        book = Book()
                        book.title = parts[0]
                        book.author = parts[1]
                        book.year = int(parts[2])
                        book.read_status = parts[3].lower() == 'true'
                        book.pages = int(parts[4])
                        book.category = BookCategory[parts[5]]
                        self.books[book.title] = book
        except Exception as e:
            print(f"Error loading books: {e}")
        return self.books
