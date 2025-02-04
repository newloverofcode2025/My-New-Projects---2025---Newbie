import json
import os

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

class Library:
    def __init__(self, file_path):
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_books(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book.to_dict())
        self.save_books()

    def remove_book(self, isbn):
        for book in self.books:
            if book["isbn"] == isbn:
                self.books.remove(book)
                self.save_books()
                return True
        return False

    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book["title"].lower() or \
               query.lower() in book["author"].lower() or \
               query.lower() in book["isbn"].lower():
                results.append(book)
        return results

    def get_all_books(self):
        return self.books