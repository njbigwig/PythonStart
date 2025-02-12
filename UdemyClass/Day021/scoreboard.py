# Scoreboard class - inherits from Turtle

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
               
        
    def add(self):
        self.score += 1
        
    def show_score(self):
        self.color("white")
        self.teleport(0, 280)
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 14, 'bold'))
        
    def get_score(self):
        return self.score
    
    def game_over(self):
        self.color("white")
        self.teleport(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=('Arial', 14, 'bold'))
        

        
        
        
        