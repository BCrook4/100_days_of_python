from turtle import Turtle, Screen
import random

def text_display(msg):
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.teleport(-50,0)
    text.write(msg)

screen = Screen()
screen.setup(width=500,height=400)

bet = screen.textinput("Make Your Bet", "Who will win the turtle race? Enter a colour:").lower()

colors = ["red", "blue", "orange", "purple", "green", "sienna"]
contestants = []

for i in range(0, len(colors)):
    contestants.append(Turtle(shape="turtle"))
    contestants[i].color(colors[i])
    contestants[i].penup()
    contestants[i].goto(x=-230, y=-80 + 30 * i)
    # contestant = Turtle(shape= "turtle")
    # contestant.color(colors[i])
    # contestant.penup()
    # contestant.goto(x=-230, y= -80 + 30 * i)

if bet:
    is_race_on = True

while is_race_on:
    # random_distance = random.randint(0,10)
    # random.choice(contestants).forward(random_distance)
    for i in contestants:
        random_distance = random.randint(0, 10)
        i.forward(random_distance)
        if i.xcor() > 230:
            winner = i.pencolor()
            if bet == winner:
                print(f"You've won! The {winner} turtle is the winner!")
                text_display(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
                text_display(f"You've lost! The {winner} turtle is the winner!")
            is_race_on = False








screen.exitonclick()