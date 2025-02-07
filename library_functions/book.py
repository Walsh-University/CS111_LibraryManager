class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.year = 0
        self.read_status = False
        self.pages = 0

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
