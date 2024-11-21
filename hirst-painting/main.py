# import colorgram
#
# colors = colorgram.extract('image.jpeg', 30)
# palette = []
# for i in range(1, len(colors)):
#     temp = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
#     palette.append(temp)
#
# print(palette)
import turtle
from turtle import Turtle, Screen
import random

color_list = [(219, 254, 237), (84, 254, 155), (173, 146, 118), (245, 39, 191), (158, 107, 56),
              (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246),
              (35, 34, 253), (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70),
              (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107),
              (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]


# create painting of 10x10 dots. each dot is of radius 20 and spaced by 50 paces
tim = Turtle()
screen = Screen()
turtle.colormode(255)
#screen.screensize(600,600)
screen.setup(1000,800)
screen.setworldcoordinates(0, 0, 600,600)
print(screen.screensize())
tim.speed(0)
tim.penup()
tim.hideturtle()
tim.teleport(75,65)

for row in range(10):
    for col in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        if col == 0 or col == 9:
            print(tim.position())
    tim.teleport(75, tim.ycor() + 50)

screen.exitonclick()