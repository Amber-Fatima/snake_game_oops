from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,240)
        self.score = 0
        self.write(f"Score: {self.score}",False,align="center",font=("courier",20,"bold"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",False,align="center",font=("courier",20,"bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",False,align="center",font=("courier",20,"bold"))

