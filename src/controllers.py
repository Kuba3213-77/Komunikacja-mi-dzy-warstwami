from .repositories import Book, BookRepository

class BookController:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_books(self, id: int) -> Book:
        return self.repository.get_book(id)
