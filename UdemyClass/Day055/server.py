# to run:
# need an Environmental Variable:
#   set FLASK_APP=server.py
#   set FLASK_DEBUG=1 (optional) OR  app.run(debug=True)
# flask run [ENTER]  or
# py server.py [ENTER] to get app.run() to execute 

from flask import Flask
import random

number_to_guess = 0


app = Flask(__name__)
print(__name__)

@app.route('/')
def welcome():
    global number_to_guess
    number_to_guess = random.randint(0, 9)
    print(f"rando = {number_to_guess}")
    return '<h1 style="text-align: center">Welcome to my guess the number game</h1>' \
           '<h2>Guess a number between 0 and 9</h2>'
        

@app.route("/<int:mynumber>")
def myguess(mynumber):
    global number_to_guess
    print(f"guess: {mynumber} number {number_to_guess}")
    if mynumber == number_to_guess:
        return "<p style='color: green;'>You are correct!</p>" \
               "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExc24zbHlwcmR4andsbzY0NWZoMDJlemRvd3gxYnpudGE5bTl0cjI1NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/9kPNJ7j4mUdDkRjbzd/giphy.gif'>"
    elif mynumber > number_to_guess:
        return "<p style='color: red;'>Too high...</p>" \
               "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGZpejkzMHQ1d2F0a3FkM3VrazJtbGJyajZwMnB3MTBzMGE2OTh1MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/kF444ath8YSuOHUQhy/giphy.gif'>"
    else:
        return "<p style='color: blue;'>Too low...</p>" \
               "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ21hZGp4ZWVycmNrdmRrMWpsbmV2ZnZuMjFianl2dHFhcDV3cWF3diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/lb4alJWN4HKnNt6Ky7/giphy.gif'>"
        

if __name__ == "__main__":
    app.run()