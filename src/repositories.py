class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

class BookRepository:
    def __init__(self):
        self.books = {
            1: Book(1, 'Ksiazka 1', 'Autor 1'),
            2: Book(2, 'Ksiazka 2', 'Autor 2'),
            3: Book(3, 'Ksiazka 3', 'Autor 3'),
        }

    def get_book(self, id: int) -> Book:
        return self.books.get(id)
