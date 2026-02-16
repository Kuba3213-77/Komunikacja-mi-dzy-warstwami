import unittest
from unittest.mock import MagicMock
from src.controllers import BookController
from src.repositories import Book

class TestBookController(unittest.TestCase):
    def test_get_books(self):
        mock_repo = MagicMock()
        expected_book = Book(1, 'Test Book', 'Test Author')
        mock_repo.get_book.return_value = expected_book
        
        controller = BookController(mock_repo)
        book = controller.get_books(1)
        
        self.assertEqual(book, expected_book)
        mock_repo.get_book.assert_called_once_with(1)

    def test_get_books_not_found(self):
        mock_repo = MagicMock()
        mock_repo.get_book.return_value = None
        
        controller = BookController(mock_repo)
        book = controller.get_books(999)
        
        self.assertIsNone(book)
