from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("courier", 60, "normal")
WIN_FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.teleport(0, 200)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", align= ALIGNMENT, font=SCORE_FONT )


    def l_scored(self):
        self.l_score += 1
        self.update_score()

    def r_scored(self):
        self.r_score += 1
        self.update_score()


    def game_won(self):
        self.goto(0,0)
        if self.l_score > self.r_score:
            self.write("Left Player Wins!", align= ALIGNMENT, font=WIN_FONT)
        else:
            self.write("Right Player Wins!", align= ALIGNMENT, font=WIN_FONT)

