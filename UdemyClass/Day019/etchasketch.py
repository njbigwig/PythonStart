from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)


def move_forwards():
    tim.forward(10)
    print(f"x = {tim.xcor()} y = {tim.ycor()}")
    
def move_back():
    tim.backward(10)
    print(f"x = {tim.xcor()} y = {tim.ycor()}")
    
def turn_countclockwise():
    # could use:
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    tim.left(10)
    print(f"x = {tim.xcor()} y = {tim.ycor()}")
    
def turn_clockwise():
    # could use:
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)
    tim.right(10)
    print(f"x = {tim.xcor()} y = {tim.ycor()}")
    
def clear():
    tim.clear()
    tim.teleport(0,0)


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)

screen.onkey(key="a", fun=turn_countclockwise)
screen.onkey(key="d", fun=turn_clockwise)

screen.onkey(key="c", fun=clear)

screen.listen()

screen.exitonclick()
