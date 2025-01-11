from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        co_ord_x = random.randint(-280, +280)
        co_ord_y = random.randint(-280, +280)
        self.goto(co_ord_x, co_ord_y)
