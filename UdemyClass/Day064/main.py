from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, SubmitField, DecimalField, validators
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class UpdateForm(FlaskForm):
    title = StringField('Title', [validators.Length(max=60)])
    year = IntegerField('Year', [validators.Optional(), validators.NumberRange(min=2025)])
    description = StringField('Description', [validators.Length(max=250)])
    rating = DecimalField('Rating', places=1, validators=[validators.DataRequired(),validators.NumberRange(min=0.0, max=10.0)])
    ranking = IntegerField('Ranking', [validators.Optional(), validators.NumberRange(min=1, max=10)])
    review = StringField('Review', [validators.DataRequired(), validators.Length(max=250)])
    imgurl = StringField('URL', [validators.Length(max=500)])
    submit = SubmitField("Done")
    
class AddForm(FlaskForm):
    title = StringField('Title', [validators.Length(max=60)])
    submit = SubmitField("Add Movie")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Create database
class Base(DeclarativeBase):
  pass

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myfavoritemovies.db"

# Create the extension
db = SQLAlchemy(model_class=Base)

# Initialize the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    description: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(Float, unique=False, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    review: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), unique=False, nullable=False)

# Create table schema in the database. Requires application context
with app.app_context():
    db.create_all() 
    
# Create test record #1, Copilot provided this block due to consistent errors
with app.app_context():
    db.session.execute(db.insert(Movie).prefix_with("OR IGNORE").values(title="Phone Booth", year=2002, description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.", rating=7.3, ranking=9, review="My favourite character was the caller.",  img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"))
    db.session.commit()  
    
    
# Create test record #2, Copilot provided this block due to consistent errors
with app.app_context():
    db.session.execute(db.insert(Movie).prefix_with("OR IGNORE").values(title="Avatar The Way of Water", year=2022, description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.", rating=7.3, ranking=10, review="I liked the water.",  img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"))
    db.session.commit()  
    
all_movies = []
    
@app.route("/")
def home():
    # Fetch records - query via select
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    
    # Use .scalars() to get the elements rather than entire rows from the database
    all_movies = result.scalars().all()     
        
    return render_template("index.html", movies=all_movies)

@app.route("/edit",methods=["GET", "POST"])
def update_review():
    editmovieform = UpdateForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if editmovieform.validate_on_submit():
        movie.rating = float(editmovieform.rating.data)
        movie.review = editmovieform.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=editmovieform)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddForm()
    print(form.title.data)
    return render_template("add.html", form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
