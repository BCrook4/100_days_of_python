import turtle
from random import randint
from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")

screen = Screen()
screen.setup(1000,750)
screen.screensize(1000,750)
#screen.setworldcoordinates(0,-250, 1250, 250)
turtle.colormode(255)
tim.pensize(1)
tim.speed(0)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap):

    for i in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

draw_spirograph(5)





screen.exitonclick()




