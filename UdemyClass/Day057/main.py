# Jinja templates are already included with Flask
import random
from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    today = datetime.datetime.now()
    yyyy = today.year
    return render_template("index.html", num=random_number, current_year=yyyy)

@app.route('/guess/<name>')
def entername(name):
    today = datetime.datetime.now()
    yyyy = today.year
    
    myagify_request = requests.get(f"https://api.agify.io?name={name}")
    #print(myagify_request.json())
    ageguess = myagify_request.json()['age']
    
    mygenderize_request = requests.get(f"https://api.genderize.io/?name={name}")
    #print(mygenderize_request.json())
    xory = mygenderize_request.json()['gender']     
    
    return render_template("index2.html", fname=f"{name.title()}", gender=xory, age=ageguess, current_year=yyyy)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    
    today = datetime.datetime.now()
    yyyy = today.year
    
    print(f"Num = {num}")
    
    blog_request = requests.get(blog_url)
    print(blog_request.json())
    all_posts = blog_request.json()
    
    return render_template("blog.html", posts=all_posts, current_year=yyyy)


if __name__ == "__main__":
    app.run(debug=True)


