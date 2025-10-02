from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('input_name')
    password = request.form.get('input_password')
    return f"<h1>Welcome, {username}! PWD={password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)