from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_dist = STARTING_MOVE_DISTANCE
        #self.generate_car()


    def move_car(self):
        for car in range(0, len(self.cars) -1):
            new_x = self.cars[car].xcor() - self.move_dist
            self.cars[car].goto(x= new_x, y= self.cars[car].ycor())


    def generate_car(self):

        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(x=320, y=random.randint(-260, 260))
        self.cars.append(new_car)

