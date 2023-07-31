import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))