# Need to install Flask package:
#   pip install flask
# Web app, to execute CTRL=click on this link in the command window:
#  python webapp.py
#  Running on http://127.0.0.1:5000

from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World!"

app.run(debug=True)