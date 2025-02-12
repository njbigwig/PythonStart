import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Road Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

myturtle = Player()

car_manager = CarManager()

scoreboard = Scoreboard()



# key bindings for snake movement control
screen.listen()
screen.onkey(myturtle.move, "Up")

game_is_on = True
while game_is_on == True:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(myturtle) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    # detect if turtle made it to the finish line
    if myturtle.is_at_finish_line() == True:
        myturtle.reset()
        car_manager.speed_up()
        scoreboard.increase_level()

            

screen.exitonclick()
            
    

