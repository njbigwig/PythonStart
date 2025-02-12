# Snake Game
from turtle import Screen, Turtle
from scoreboard import Scoreboard, PLAYER1, PLAYER2
from players import Player
from court import Court
from ball import Ball
import time
import random

ball = None

def whereami(x,y):
    print(x, y)    

screen = Screen()
screen.setup(width=800, height=800)
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

players = []
players.append(Player(PLAYER1))
players.append(Player(PLAYER2))


scoreboard = Scoreboard()
scoreboard.show_scores()

# create a ball
ball = Ball()

# build a Pong court
court = Court()


# key bindings for snake movement control
screen.listen()
screen.onkeypress(players[0].up, "q")
screen.onkeypress(players[0].down, "a")
screen.onkeypress(players[1].up, "p")
screen.onkeypress(players[1].down, "l")

screen.onscreenclick(whereami)
    
game_is_on = True

# get a random angle for the ball to start moving to

# define a starting screen quadrant so the starting angle will not be too steep
# 0: 0 to 90 degrees
# 1: 90 to 180 degrees
# 2: 180 to 270 degrees
# 3: 270 to 360 degrees
quadrant = random.randint(0, 3)

if quadrant == 0:
    angle = random.randint(0, 70)
elif quadrant == 1:
    angle = random.randint(120, 180)
elif quadrant == 2:
    angle = random.randint(180, 250)
else:
    angle = random.randint(290, 350)  
    
#print(f"Quad: {quadrant} {angle}")
ball.set_heading(angle)
ball.forward(10)

while game_is_on == True:
    screen.update()
    time.sleep(0.05)
    game_is_on = ball.move()
    
    ball.position()
    
    # check for paddle hitting the ball back
    if int(ball.distance(players[0])) < 50 and ball.xcor() < -335:  
        ball.paddle()         
    elif int(ball.distance(players[1])) < 50 and ball.xcor() > 335: 
        ball.paddle() 
      
    # check for a score  
    if ball.xcor() < -385:
        # player 1 scored
        scoreboard.increment_score(1)
        scoreboard.show_scores()
        ball.reset(1)
    elif ball.xcor() > 385:
        # player 0 scored
        scoreboard.increment_score(0)
        scoreboard.show_scores()
        ball.reset(0)
        
    # check if player reached a score of 10
    if scoreboard.winner_check() == True:
        game_is_on = False        

    
scoreboard.game_over()           
    

screen.exitonclick()

        
  
        
    



