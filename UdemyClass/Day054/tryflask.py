# to run:
# need an Environmental Variable:
#   set FLASK_APP=tryflask.py
# flask run [ENTER]  or
# py tryflaskpy [ENTER] to get app.run() to execute

from flask import Flask

app = Flask(__name__)
print(__name__)

# Python decorator - user goes to home page
@app.route('/')
def hello_world():
    return "<p>Hello, World!<p>"

@app.route('/bye')
def bye_world():
    return "<p>Bye Bye, World!<p>"

if __name__ == "__main__":
    app.run()
