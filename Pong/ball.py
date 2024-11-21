from turtle import Turtle
import random

SPEED_XDELTA = 1.2
SPEED_YDELTA = 1.05

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.speed_state = 0

    def serve(self):
        self.y_move = random.randint(1, 20)
        self.x_move *=-1
        self.move_speed = 0.1
        # if self.speed_state > 0:
        #     self.x_move /= SPEED_XDELTA**self.speed_state
        #     self.speed_state = 0
        self.home()

    def speed_up(self):
       self.move_speed *= 0.9
        # self.speed_state += 1
        # self.x_move *= SPEED_XDELTA
        #self.y_move *= SPEED_DELTA

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)


    def bounce_y(self):
        self.y_move *= -1
        self.move_ball()

    def bounce_x(self):
        self.x_move *= -1
        self.move_ball()