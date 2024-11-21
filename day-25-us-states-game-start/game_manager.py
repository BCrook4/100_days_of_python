from turtle import Turtle, Screen

ALIGN = "left"
FONT = ('Arial', 8, 'normal')

class Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.correct_guesses = 0

    def get_answer(self):
        return self.screen.textinput(title=f"{self.correct_guesses}/50 States Correct", prompt="Enter a state: ").title()

    def write_state(self, state, x, y):
        self.goto(x, y)
        self.write(f"{state}", align=ALIGN, font=FONT)
        self.correct_guesses += 1
