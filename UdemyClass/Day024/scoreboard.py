# Scoreboard class - inherits from Turtle

from turtle import Turtle
import os

HIGHSCOREFILE = "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.high_score = 0
        
        if os.path.exists(HIGHSCOREFILE):
            with open(HIGHSCOREFILE, "r") as scorefile:
                self.high_score = int(scorefile.read())
        else:
            with open(HIGHSCOREFILE, "w") as scorefile:
                scorefile.write(str(self.high_score))
        
    def add(self):
        self.score += 1
        
    def show_score(self):
        self.color("white")
        self.teleport(0, 280)
        self.clear()
        
        if self.score > self.high_score:
            self.high_score = self.score
            
        self.write(f"Score: {self.score}     High Score: {self.high_score}", move=False, align="center", font=('Arial', 14, 'bold'))
  
    def get_score(self):
        return self.score
    
    def game_over(self):
        self.color("white")
        self.teleport(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=('Arial', 14, 'bold'))
        
        # save high score
        with open(HIGHSCOREFILE, "w") as scorefile:
            scorefile.write(str(self.high_score))
        

        
        
        
        