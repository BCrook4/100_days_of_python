from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
CAR_CHANCE = 6


class CarManager():
    def __init__(self):
        self.cars = []
        self.move_dist = STARTING_MOVE_DISTANCE
        self.generate_car()


    def move_car(self):
        for car in range(0, len(self.cars) -1):
            if self.cars[car].xcor() < -320:
                del self.cars[car]
                continue
            else:
                new_x = self.cars[car].xcor() - self.move_dist
                self.cars[car].goto(x= new_x, y= self.cars[car].ycor())


    def generate_car(self):
        if random.randint(1, CAR_CHANCE) == CAR_CHANCE:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=320, y=random.randint(-255, 255))
            self.cars.append(new_car)

    def speed_up(self):
        self.move_dist += MOVE_INCREMENT
