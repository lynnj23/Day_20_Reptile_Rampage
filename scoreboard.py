#Generates Scoreboard and keeps a Tally
from turtle import Turtle
from food import Food
ALIGNMENT = "center"
FONT = ("Courier New", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.high_score = 0
        self.player_initials = ""
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Score = {self.player_score}, High Score = {self.high_score}",  False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.player_score > self.high_score:
            self.high_score = self.player_score
        self.player_score = 0


    # def wall_crash_gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.player_score += 1
        self.write_score()

