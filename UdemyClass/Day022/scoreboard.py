# Scoreboard class - inherits from Turtle

from turtle import Turtle

PLAYER1 = 0
PLAYER2 = 1

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.scores = []
        self.scores.append(0)
        self.scores.append(0)
               
        
    def increment_score(self, playerno):
        self.scores[playerno] += 1
        
    def show_scores(self):
        self.clear()
        self.color("white")
        
        self.teleport(-200, 335)
        self.write(f"{self.scores[PLAYER1]}", move=False, align="center", font=('Arial', 40, 'bold'))
        
        self.teleport(200, 335)
        self.write(f"{self.scores[PLAYER2]}", move=False, align="center", font=('Arial', 40, 'bold'))
        
    def winner_check(self):
        if self.scores[0] == 10 or self.scores[1] == 10:
            return True
        else:
            return False
         
    def game_over(self):
        self.color("white")
        self.teleport(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=('Arial', 16, 'bold'))
        

        
        
        
        