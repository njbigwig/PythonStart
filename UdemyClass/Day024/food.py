# Food class - inherits from Turtle

from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        #self.score = -1
        self.refresh()
                
        
    def refresh(self):
        self.color("SandyBrown")
        ran_xcor = random.randint(-260, 260)
        ran_ycor = random.randint(-260, 260)
        self.goto(ran_xcor, ran_ycor)
        
        
    
        
        
        
        