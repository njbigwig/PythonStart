from flask import Flask, render_template
import post


app = Flask(__name__)

posts = post.Post()

@app.route('/')
def home():
    return render_template("index.html", post1_title=posts.get_blog_title(0), post1_subtitle=posts.get_blog_subtitle(0), post2_title=posts.get_blog_title(1), post2_subtitle=posts.get_blog_subtitle(1))

@app.route('/<num>')
def show_blog(num):
    print(f"Blogno = {num}")
    blogno = int(num)
    return render_template("post.html", post_title=posts.get_blog_title(blogno), post_subtitle=posts.get_blog_subtitle(blogno), post_body=posts.get_blog_body(blogno))

if __name__ == "__main__":
    app.run(debug=True)
