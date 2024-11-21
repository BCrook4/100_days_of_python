from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def rotate_left():
    tim.left(10)

def rotate_right():
    tim.right(10)

def move_backwards():
    tim.backward(10)

def clear_screen():
    screen.resetscreen()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(rotate_left, "a")
screen.onkeypress(rotate_right, "d")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(clear_screen, "c")













screen.exitonclick()