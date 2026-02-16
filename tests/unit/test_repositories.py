import unittest
from src.repositories import BookRepository, Book

class TestBookRepository(unittest.TestCase):
    def test_get_book(self):
        repo = BookRepository()
        book = repo.get_book(1)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, 'Ksiazka 1')
        self.assertEqual(book.author, 'Autor 1')

    def test_get_book_not_found(self):
        repo = BookRepository()
        book = repo.get_book(999)
        self.assertIsNone(book)
