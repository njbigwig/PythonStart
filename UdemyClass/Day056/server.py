# to run:
# need an Environmental Variable:
#   set FLASK_APP=server.py
#   set FLASK_DEBUG=1 (optional) OR  app.run(debug=True)
# flask run [ENTER]  or
# py server.py [ENTER] to get app.run() to execute 

from flask import Flask, render_template



app = Flask(__name__)
print(__name__)

# using templates
@app.route("/")
def home():
    return render_template("index.html")
    #return render_template("davessite.html")

if __name__ == "__main__":
    app.run()
    