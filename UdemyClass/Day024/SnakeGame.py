# Snake Game
from turtle import Screen
import snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

# snake_list = []

# tx = 0
# ty = 0
# squaresize = 20

# for box in range(3):
#     snake = Turtle(shape="square")
#     snake.teleport(tx, ty)
#     snake.color("white")
#     snake.speed("normal") 
#     snake.penup()
#     snake_list.append(snake)
#     tx -= squaresize
mysnake = snake.Snake(3)  
food = Food()

scoreboard = Scoreboard()
scoreboard.show_score()


# key bindings for snake movement control
screen.listen()
screen.onkey(mysnake.up, "Up")
screen.onkey(mysnake.down, "Down")
screen.onkey(mysnake.left, "Left")
screen.onkey(mysnake.right, "Right")

    
game_is_on = True

while game_is_on == True:
    screen.update()
    time.sleep(0.2)
    mysnake.move()
    
    # detect collision with food - use Turtle distance method
    if mysnake.head.distance(food) < 20:
        print("\aYummy food morsel...")
        food.refresh()   
        scoreboard.add()
        scoreboard.show_score()   
        mysnake.extend()
        
    # detect collision with a wall 560x560 active game box
    if mysnake.head.xcor() > 280 or mysnake.head.xcor() < -280 or mysnake.head.ycor() > 280 or mysnake.head.ycor() < -280:
        game_is_on = False 
        scoreboard.game_over()
        
    # detect head collision with any other segment - slice off the list head [1:]
    for segment in mysnake.snake_list[1:]:
        if mysnake.head.distance(segment) < 10:
            game_is_on = False 
            scoreboard.game_over()
            
    

screen.exitonclick()


        
  
        
    



