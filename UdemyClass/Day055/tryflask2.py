# to run:
# need an Environmental Variable:
#   set FLASK_APP=tryflask2.py
#   set FLASK_DEBUG=1 (optional) OR  app.run(debug=True)
# flask run [ENTER]  or
# py tryflask2.py [ENTER] to get app.run() to execute 

from flask import Flask

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
 
def is_authenicated_decorator(function):
    def wrapper(*args, **kwargs):
        #print(f"{function} {args[1]}")
        fn_name = f"{function}".split()[1]
        print(fn_name)
        print(function.__name__)
        if args[0].is_logged_in == True:
           function(args[0], args[1])
    return wrapper
   
@is_authenicated_decorator        
def create_blog_post(user,num):
        print(f"{num} This is {user.name}'s new blog post.")
        
new_user = User("Bubba")
new_user.is_logged_in = True
create_blog_post(new_user,1)

app = Flask(__name__)
print(__name__)

def make_bold(function):
  def wrapper_function():
      return "<b>" + function() + "</b>"
  return wrapper_function

def make_italic(function):
  def wrapper_function():
      return "<em>" + function() + "</em>"
  return wrapper_function

def make_underlined(function):
  def wrapper_function():
      return "<u>" + function() + "</u>"
  return wrapper_function

# Python decorator - user goes to home page
# also can use <p> <p> - added CSS code
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmFudzBxZmFzdnl3OHF5cHBwemczaTlqMWl0eDB1dWUyZjN1dG9yYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/tj7q6n5L4qW7m/giphy.gif" width=200>'

@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def bye_world():
    return "<p>Bye Bye, World!<p>"

# http://127.0.0.1:5000/username/dave/1
#@app.route("/username/<path:name>")
# http://127.0.0.1:5000/username/dave
@app.route("/username/<name>")
def greet(name):
    return f"Hello there - {name}!"

# http://127.0.0.1:5000/username/george/89
@app.route("/username/<name>/<int:age>")
def greet2(name, age):
    return f"Hello {name} - you are {age} years old"

if __name__ == "__main__":
    app.run()
    
# # TODO: Create the logging_decorator() function 👇
# def logging_decorator(function):
#     def wrapper(*args, **kwargs):
#         fn_name = f"{function}".split()[1] OR function.__name__
#         print(f"You called {fn_name}({args[0]}, {args[1]}, {args[2]})")
#         result = function(*args)
#         print(f"It returned: {result}")
#         return result
        
#     return wrapper


# # TODO: Use the decorator 👇
# @logging_decorator
# def a_function(*args):
#     return sum(args)
    
# a_function(1,2,3)   
