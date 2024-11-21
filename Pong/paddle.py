from turtle import Turtle

PENSIZE = 20
HEIGHT_STRETCH = 5
UP = 90
DOWN = 270
MOVE_DIST = 20

class Paddle(Turtle):
    def __init__(self, coord):
        super().__init__()
        self.create_paddle(coord)


    def create_paddle(self, position):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)
        self.speed("fast")

    def move_up(self):
        # self.paddle.setheading(UP)
        # self.paddle.forward(MOVE_DIST)
        self.goto(self.xcor(), self.ycor() + MOVE_DIST)

    def move_down(self):
        # self.paddle.setheading(DOWN)
        # self.paddle.forward(MOVE_DIST)
        self.goto(self.xcor(), self.ycor() - MOVE_DIST)