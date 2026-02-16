from flask import Flask, jsonify, abort
from .controllers import BookController
from .repositories import BookRepository

app = Flask(__name__)

repository = BookRepository()
controller = BookController(repository)

@app.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    book = controller.get_books(id)
    return str(book)

if __name__ == '__main__':
    app.run(debug=True)
