from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.reset()       
        
    def move(self):
        if self.ycor()+MOVE_DISTANCE <= 280: 
            self.forward(MOVE_DISTANCE)
        
    def reset(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
                
        

