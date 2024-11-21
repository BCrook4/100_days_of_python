from flask import Flask
import random
import time


app = Flask(__name__)

@app.route("/")
def guess_number():
    screen = ("<h1>Guess a number between 0 and 9</h1>"
              "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='numbers'>")
    return screen


rand_num = random.randint(0, 9)

@app.route("/<int:user_guess>")
def check_guess(user_guess):
    if user_guess < rand_num:
        screen = ("<h1 style='color:blue'>Too low, try again!</h1>"
                  "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
    elif user_guess > rand_num:
        screen = ("<h1 style='color:red'>Too high, try again!</h1>"
                  "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    else:
        screen = ("<h1 style='color:green'>You found me!</h1>"
                  "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    return screen


if __name__ == "__main__":
    app.run(debug=True) # app.run() does the same as what we did in the terminal