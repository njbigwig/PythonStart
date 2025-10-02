from flask import Flask, request, render_template
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-entry", methods=['POST'])
def receive_data():
    username = request.form.get('name')
    emailaddress = request.form.get('email')
    phoneno = request.form.get('phone')
    messageinfo = request.form.get('message')
    #print(f"{username} {messageinfo}")
    return f"<h1>Successfully sent your message!</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
