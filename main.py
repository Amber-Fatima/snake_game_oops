from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen display
s=Screen()
s.title("Snake game")
s.bgcolor("black")


# snakes body
snake=Snake()
food=Food()
scoreboard=Scoreboard()
s.tracer(0)  # to make the body of the snake to move as a whole game

'''                         |
                    |       |
___  ->  __|  ->   _|  ->   |
 to make the snake turn like this we need to 
 ->first make 3rd last part (left part) overlap to middle 
 ->then middle to forward 
 ->right part move forward in a loop
'''
s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")
game = True
while game:
    s.update()
    time.sleep(0.5)
    snake.move()
    # if turtle reaches boundary
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>265 or snake.head.ycor()<-265:
        scoreboard.game_over()
        game=False


    # new food in new location if snake hits the food
    if snake.head.distance(food)<15:
        snake.add_body()
        food.refresh()
        scoreboard.update_score()

    for b in snake.snake_body:
        if b == snake.head:
            pass
        elif snake.head.distance(b)<10 :
            scoreboard.game_over()
            game=False



s.exitonclick()
