# Player class - inherits from Turtle

from turtle import Turtle
from scoreboard import PLAYER1, PLAYER2


class Player(Turtle):
    def __init__(self, player_no):
        super().__init__()
 
        self.playerid = player_no        
        
        if self.playerid == PLAYER1:
            self.shape("square")
            self.penup()
            self.speed("fastest")
            self.teleport(-360, 0)
            self.color("white")
            self.shapesize(stretch_wid=5, stretch_len=1)
        else:
            self.shape("square")
            self.penup()
            self.speed("fastest")
            self.teleport(360, 0)
            self.color("white")
            self.shapesize(stretch_wid=5, stretch_len=1)               
        
    def up(self):
        if self.ycor()+30 <= 345:
            self.teleport(self.xcor(), self.ycor()+30)
            #self.position()
                
    def down(self):
        if self.ycor()-30 > -360:
            self.teleport(self.xcor(), self.ycor()-30)
            #self.position()
           
            
    def position(self):
        print(f"#{self.playerid} X={self.xcor()} Y={self.ycor()}")
       


        

        

        
        
        
        