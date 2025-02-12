# Ball class - inherits from Turtle

# install packages to support playing MP3 or WAV files
# pip install wheel
# pip install playsound

#import threading
#from playsound import playsound
from turtle import Turtle
import random
import time

SLOWBALL = 10
FASTBALL = 15

class Ball(Turtle):
    def __init__(self):
        super().__init__()   
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.teleport(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.speed = SLOWBALL 
                
    
    def sound_wall(self):
        pass
        #playsound('pongwall.mp3', True)
        
    def sound_paddle(self):
        pass
        #playsound('pongpaddle.mp3', True)

    def fast_speed(self):
        self.speed = FASTBALL
        
    def slow_speed(self):
        self.speed = SLOWBALL
    
    def get_heading(self):
        return self.heading()
    
    def set_heading(self, setangle):
        self.setheading(setangle)
    
    def paddle(self):
        #print("paddle hit")
        ballheading = self.heading()
        ballheading += 180
        
        # give an angle a bit off to prevent easy back and forth
        if int(self.ycor()) > 0:
            ballheading += random.randint(10, 25)
        else:
            ballheading -= random.randint(10, 25)            
        
        self.setheading(ballheading)
        self.fast_speed()
        self.forward(self.speed)
        self.sound_paddle()    
     
    def position(self):
        x = int(self.xcor())
        y = int(self.ycor())
        #print(f"Heading={self.get_heading()} X={x} Y={y}") 
        
    def reset(self, playerscored):
        self.teleport(0, 0)
        
        # select top or bottom to reset ball position
        quadrant = random.randint(0, 1)
        
        angle = 0
        
        if quadrant == 0:
            if playerscored == 0:
                angle = random.randint(120, 180)            
            else:
                angle = random.randint(0, 70)
        else:
            if playerscored == 0:
                angle = random.randint(180, 250)
            else:
                angle = random.randint(290, 350)         
        
        self.set_heading(angle)
        self.slow_speed()
    
    def move(self):
        x = int(self.xcor())
        y = int(self.ycor())
        ballheading = self.heading()           
        
        # check for court side line collision - bounce at opposite angle
        if ballheading > 90 and ballheading <= 180:
            # quadrant #1
            #print(f"Q1 BEFORE heading={ballheading} X={x} Y={y}")
            if y < 385:
                self.forward(self.speed)
            elif y >= 385:                
                ballheading += 90                 
                self.setheading(ballheading)
                #print(f"Q1 Heading = {ballheading}")
                self.slow_speed()
                self.forward(self.speed)   
                self.sound_wall()
        elif ballheading > 180 and ballheading < 270:
            # quadrant #2
            #print(f"Q2 BEFORE heading={ballheading} X={x} Y={y}")
            if y > -380:
                self.forward(self.speed)  
            elif y <= -380:
                ballheading -= 90            
                #sound_thread = threading.Thread(target=self.sound_wall)
                #sound_thread.start()
                self.setheading(ballheading)
                #print(f"Q2 Heading = {ballheading}")
                self.slow_speed()
                self.forward(self.speed)     
                self.sound_wall()  
        elif ballheading > 270 and ballheading < 359:
            # quadrant #3
            #print(f"Q3 BEFORE heading={ballheading} X={x} Y={y}")
            if y > -380:
                self.forward(self.speed) 
            elif y <= -380:
                ballheading += 90                 
                self.setheading(ballheading)
                #print(f"Q3 Heading = {ballheading}")
                self.slow_speed()
                self.forward(self.speed)    
                self.sound_wall()                
        elif ballheading >= 0 and ballheading < 90:
            # quadrant #0
            #print(f"Q0 BEFORE heading={ballheading} X={x} Y={y}")
            if y < 385:
                self.forward(self.speed)  
            elif y >= 385:
                ballheading += 270                 
                self.setheading(ballheading)
                #print(f"Q0 Heading = {ballheading}")
                self.slow_speed()
                self.forward(self.speed)      
                self.sound_wall()              
     

        return True


        
        
              
        

        

        
        
        
        