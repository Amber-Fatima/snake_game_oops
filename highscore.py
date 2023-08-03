from turtle import Turtle

class Highscore(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(230, 240)
        self.score=self.high()
        self.write(f"HighScore: {self.score}",False,align="center",font=("courier",15,"bold"))
    def high(self):
        f = open('highscore.txt', 'r')
        f.seek(0)
        high_score = int(f.readline())
        f.close()
        return high_score

    def update_score(self):
        f = open('highscore.txt', 'r')
        prev = int(f.readline())
        f.close()

        f = open('highscore.txt', 'w+')
        f.write(f"{prev +1}")
        f.seek(0)
        f.close()
        self.score += 1
        self.clear()

        self.write(f"Highscore: {self.score}",False,align="center",font=("courier",16,"bold"))
