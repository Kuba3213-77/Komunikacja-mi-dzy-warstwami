import unittest
import json
from unittest.mock import patch, MagicMock
from src.app import app
from src.repositories import Book

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('src.app.controller')
    def test_get_book(self, mock_controller):
        # Prepare mock data
        expected_book = Book(1, 'Test Book', 'Test Author')
        mock_controller.get_books.return_value = expected_book

        # Make request
        response = self.app.get('/book/1')
        
        # Assertions
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['title'], 'Test Book')
        self.assertEqual(data['author'], 'Test Author')
        
        # Verify controller usage
        mock_controller.get_books.assert_called_once_with(1)

    @patch('src.app.controller')
    def test_get_book_not_found(self, mock_controller):
        mock_controller.get_books.return_value = None
        
        response = self.app.get('/book/999')
        
        self.assertEqual(response.status_code, 404)
