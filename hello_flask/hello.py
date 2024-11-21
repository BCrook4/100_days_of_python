from flask import Flask


# __name__ is name of current class, function, method, descriptor, or generator instance being run
app = Flask(__name__)

print(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_italic(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def underline_wrapper():
        return "<u>" + function() + "</u>"
    return underline_wrapper


# Python Decorator - gives additional functionality to a function
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def say_bye():
    return "<p>Bye</p>"

@app.route("/<name>")
def greet(name):
    return f"Hello there {name}!"

# to run server open terminal and switch to Command Prompt then type:
# set FLASK_APP=hello.py
#
# flask run

if __name__ == "__main__":
    app.run(debug=True) # app.run() does the same as what we did in the terminal