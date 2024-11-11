from collections import defaultdict
from typing import List, Dict


class Book:
    def __init__(self, title: str, author: str, category: str):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f"'{self.title}' by {self.author} [{self.category}]"


class Shelf:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def sort_books(self):
        # Sorts the books by title in ascending order
        self.books.sort(key=lambda book: book.title)

    def __str__(self):
        return ", ".join(str(book) for book in self.books)


class Room:
    def __init__(self):
        self.shelves = []

    def add_shelf(self, shelf: Shelf):
        self.shelves.append(shelf)

    def organize_books_by_category(self, books: List[Book]):
        category_shelves: Dict[str, Shelf] = defaultdict(Shelf)

        for book in books:
            category_shelves[book.category].add_book(book)

        self.shelves.extend(category_shelves.values())

    def sort_books_on_all_shelves(self):
        for shelf in self.shelves:
            shelf.sort_books()

    def __str__(self):
        return "\n".join(f"Shelf {i + 1}: {shelf}" for i, shelf in enumerate(self.shelves))


def demonstrate_organizing_books():
    books = [
        Book("The Catcher in the Rye", "J.D. Salinger", "Classics"),
        Book("To Kill a Mockingbird", "Harper Lee", "Classics"),
        Book("A Brief History of Time", "Stephen Hawking", "Science"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "Classics"),
        Book("The Selfish Gene", "Richard Dawkins", "Science"),
    ]

    room = Room()
    room.organize_books_by_category(books)

    room.sort_books_on_all_shelves()

    print(room)


demonstrate_organizing_books()
