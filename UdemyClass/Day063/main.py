from flask import Flask, render_template, request, redirect, url_for
#import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, select

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)

# Create database
class Base(DeclarativeBase):
  pass

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)

# Create table
# (id INTEGER PRIMARY KEY, 
# title varchar(250) NOT NULL UNIQUE, 
# author varchar(250) NOT NULL, 
# rating FLOAT NOT NULL)")

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context
with app.app_context():
    db.create_all()
    
# Create test record, Copilot provided this block due to consistent errors
with app.app_context():
    db.session.execute(db.insert(Book).prefix_with("OR IGNORE").values(title="Harry Potter", author="J. K. Rowling", rating=9.3))
    db.session.commit()
  
# # All records  
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()
#     print(all_books)
    
# # A single record
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     print(book)
    
# Update a record
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit() 
#     # print(book_to_update)
    
# Retrieve a record with a primary key
# book_id = 2
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()  
#     print(book_to_update)


all_books = []

#db = sqlite3.connect("books-collection.db")

#cursor = db.cursor()

#cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# test data - getting various errors, Copilot recommended OR REPLACE and script now works, removed key = 1, auto assigned by SQL
# cursor.execute("INSERT OR REPLACE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

@app.route('/')
def home():
    # Fetch records - query via select
    result = db.session.execute(db.select(Book).order_by(Book.title))
    
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = result.scalars().all()
    
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    
        if request.method == "POST":
            new_book = Book(title = request.form["title"], author = request.form["author"], rating = request.form["rating"])
            print(request.form["title"])
            
            #all_books.append(new_book)
            
            db.session.add(new_book)
            db.session.commit()
            
            return redirect(url_for('home'))
            
        return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)

