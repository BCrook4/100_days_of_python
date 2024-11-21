from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]


    def create_snake(self):
        for i in range(3):
            position = (i * -MOVE_DISTANCE, 0)
            self.add_segment(position)


    def add_segment(self, position):
        # self.body.append(Turtle("square"))
        # self.body[len(self.body) -1].penup()
        # self.body[len(self.body) -1].teleport(position)
        # self.body[len(self.body) -1].color("white")
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.teleport(position)
        new_segment.color("white")
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            next_x = self.body[i - 1].xcor()
            next_y = self.body[i - 1].ycor()
            self.body[i].goto(next_x, next_y)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
