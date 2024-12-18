# Snake Game
from turtle import Screen, Turtle
import snake
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

# key bindings for snake movement control
screen.listen()
screen.onkey(mysnake.up, "Up")
screen.onkey(mysnake.down, "Down")
screen.onkey(mysnake.left, "Left")
screen.onkey(mysnake.right, "Right")

    
game_is_on = True

while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    mysnake.move()
    
    
    
    # for seg_num in range(len(snake_list)-1, 0, -1):
    #     new_x = snake_list[seg_num - 1].xcor()
    #     new_y = snake_list[seg_num - 1].ycor()
    #     snake_list[seg_num].goto(new_x, new_y)
    
    # snake_list[0].forward(20)
    
    # snake chasing its tail
    # snake_list[0].forward(20)
    # snake_list[0].left(90)
        
        
    #for move in range(len(snake_list)):
    #    #snake_list[move].forward(20)
    #   snake_list[move].teleport(snake_list[move].xcor()+20, snake_list[move].ycor())
        
        
        
    



screen.exitonclick()