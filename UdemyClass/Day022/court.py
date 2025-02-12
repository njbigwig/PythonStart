# Court class - inherits from Turtle

from turtle import Turtle


class Court(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.speed("fastest")
        
        # draw a dotted center court line
        self.pencolor("white")
        self.pensize(3)
        self.setheading(270)      
      
        self.teleport(0, 395)
        
        for dashline in range(0, 790, 10):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(5)
            
        # draw red end lines
        self.pencolor("red")
        self.pensize(2)
        self.teleport(-396, 397)
        self.setheading(270) 
        self.pendown()
        self.forward(800)
        
        self.pencolor("red")
        self.pensize(2)
        self.teleport(390, 397)
        self.setheading(270) 
        self.pendown()
        self.forward(800)
        
        self.leftwall = -396
        self.rightwall = 390
        
        # draw side lines
        self.pencolor("LightSkyBlue")
        self.pensize(2)
        self.teleport(-390, -390)
        self.setheading(0) 
        self.pendown()
        self.forward(775)
        
        self.pencolor("LightSkyBlue")
        self.pensize(2)
        self.teleport(-390, 395)
        self.setheading(0) 
        self.pendown()
        self.forward(775)
        
        
              
        

        

        
        
        
        