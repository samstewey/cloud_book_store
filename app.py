from flask import Flask, render_template, request, redirect
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.user_repository import UserRepository
from lib.user import User

# instantiate a Flask app object
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def get_all_books():
  connection = DatabaseConnection()
  connection.connect()
  book_repository = BookRepository(connection)
  books = book_repository.all()
  return render_template('books.html', books=books)

@app.route('/authors', methods=['GET'])
def authors():
  return render_template('authors.html')

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/books', methods=['POST'])
def create_book():
  connection = DatabaseConnection()
  connection.connect()
  book_repository = BookRepository(connection)
  book_details = request.form
  book = Book(id=None, title=book_details['title'], author=book_details['author'])
  book_repository.create(book)
  return redirect('/books')

@app.route('/users/new', methods=['GET'])
def new_user():
  return render_template('signup_form.html')

@app.route('/users/new', methods=['POST'])
def save_user():
  connection = DatabaseConnection()
  connection.connect()
  user_repository = UserRepository(connection)
  user_details = request.form
  user = User(id=None, username=user_details['username'], password=user_details['password'])
  user_repository.save(user)
  return redirect('/books')

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
