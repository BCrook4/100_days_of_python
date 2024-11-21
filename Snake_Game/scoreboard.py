from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.teleport(0, 280)
        self.score = 0

        with open("data.txt", mode= "r") as data:
            self.highscore = int(data.read())

        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()


# def game_over(self):
#     self.teleport(0,0)
#     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)