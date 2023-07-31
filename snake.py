from turtle import Turtle

P=[(0,0),(-20,0),(-40,0)]
class Snake:

    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]

    def create_snake(self):

        for i in P:
            a = Turtle()
            a.shape("square")
            a.color("white")
            a.penup()
            a.goto(i)
            self.snake_body.append(a)

# extending body when snake eats food
    def add_body(self):
        a = Turtle()
        a.shape("square")
        a.color("white")
        a.penup()

        a.goto(self.snake_body[-1].position())
        self.snake_body.append(a)




    def move(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[snake].goto(self.snake_body[snake - 1].xcor(), self.snake_body[snake - 1].ycor())

        self.head.forward(20)

    def up(self):
        self.head.setheading(90)

    def right(self):
        self.head.setheading(0)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)



