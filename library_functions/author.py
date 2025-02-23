from datetime import date
from typing import Optional, List

from library_functions.book import Book


class Author:
    def __init__(self, first_name: str, last_name: str, birth_date: date, death_date: Optional[date] = None):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
        self._death_date = death_date
        self._books = []

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if not value or not value.strip():
            raise ValueError("First name cannot be empty")
        self._first_name = value.strip()

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Last name cannot be empty")
        self._last_name = value.strip()

    @property
    def birth_date(self) -> date:
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: date):
        if not value:
            raise ValueError("Birth date cannot be empty")
        self._birth_date = value

    @property
    def death_date(self) -> Optional[date]:
        return self._death_date

    @death_date.setter
    def death_date(self, value: Optional[date]):
        self._death_date = value

    @property
    def books(self) -> List[Book]:
        return self._books

    def __str__(self) -> str:
        return f"{self._first_name} {self._last_name} ({self._birth_date})"

    def __eq__(self, other: 'Author') -> bool:
        if not isinstance(other, Author):
            return NotImplemented
        return (self._first_name == other._first_name and
                self._last_name == other._last_name and
                self._birth_date == other._birth_date)

    def __lt__(self, other: 'Author') -> bool:
        if not isinstance(other, Author):
            return NotImplemented
        return (self._last_name, self._first_name) < (other._last_name, other._first_name)
