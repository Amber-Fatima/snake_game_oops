from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from highscore import Highscore
import winsound
from threading import Thread

import time

def play_sound(a):
   winsound.PlaySound(a, winsound.SND_FILENAME|winsound.SND_ASYNC)

# screen display
s=Screen()
s.title("Snake game")
s.bgcolor("black")

# difficulty popup
d=s.textinput("Game level","Difficulty level(easy//medium//hard):")
if d=="easy":
    timer=1
elif d=="medium":
    timer=0.5
else:
    timer=0.1


# snakes body
snake=Snake()
food=Food()
scoreboard=Scoreboard()
highscore=Highscore()

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
thread = Thread(target=play_sound("mixkit-arcade-game-opener-222.wav"))
thread.start()
while game:
    s.update()
    time.sleep(timer)
    snake.move()
    # if turtle reaches boundary
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>265 or snake.head.ycor()<-265:
        scoreboard.game_over()
        l = Thread(target=play_sound("mixkit-losing-bleeps-2026.wav"))
        l.start()
        game=False



    # new food in new location if snake hits the food
    if snake.head.distance(food)<15:
        snake.add_body()
        food.refresh()
        scoreboard.update_score()
        r = Thread(target=play_sound("mixkit-small-hit-in-a-game-2072.wav"))
        r.start()
        if scoreboard.score > highscore.score:
            highscore.update_score()



    for b in snake.snake_body[1:]:

        if snake.head.distance(b)<10 :
            scoreboard.game_over()
            l = Thread(target=play_sound("mixkit-losing-bleeps-2026.wav"))
            l.start()
            game=False



s.exitonclick()
