
def move_ball(self, delta_y):
    delta_y *= 10
    new_x = self.xcor() + 5* 1.3333
    new_y = self.ycor() + delta_y
    self.goto(x=new_x, y=new_y)
    # self.setheading(36.87)
    # self.forward(20)