from enum import Enum


class BookCategory(Enum):
    Unknown = 0
    Reference = 1
    NonFiction = 2
    Fiction = 3
    Biography = 4
    Children = 5
    YoungAdult = 6


class Book:
    def __init__(self, title: str = "",
                 author: str = "",
                 year: int = 0,
                 pages: int = 0,
                 read_status: bool = False,
                 category: BookCategory = BookCategory.Unknown):
        self._title = title
        self._author = author
        self._year = year
        self.read_status = read_status
        self._pages = pages
        self._category = category

    @property
    def title(self):
        return self._title

    # 
    # @title.setter
    # def title(self, t):
    #     self._title = t

    @property
    def author(self):
        return self._author

    # @author.setter
    # def author(self, a):
    #     self._author = a

    @property
    def year(self):
        return self._year

    # @year.setter
    # def year(self, y):
    #     if y < -600:
    #         raise ValueError("Year cannot be before 600 B.C.")
    #     self._year = y

    @property
    def pages(self):
        return self._pages

    # @pages.setter
    # def pages(self, p):
    #     if p < 0:
    #         raise ValueError("Pages cannot be negative")
    #     self._pages = p

    @property
    def category(self):
        return self._category

    def __str__(self):
        return f"{self._title} by {self.author} ({self.year})"
