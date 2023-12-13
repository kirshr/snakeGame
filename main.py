from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakeee")
screen.tracer(0)

screen.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()


game_is_on = True

# def play_again():
#     scoreboard.score = 0
#     scoreboard.update_scoreboard()
#     game_is_on = True

# def quit_game():
#     game_is_on = False

while game_is_on:
    screen.update()
    time.sleep(0.1)
    scoreboard
    snake.move()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')


    #Detect Collision
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    #detect collision with snake tail
    for segment in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False




   



    











screen.exitonclick()