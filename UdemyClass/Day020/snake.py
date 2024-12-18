from turtle import Turtle

MOVE_DISTANCE = 20
UP_DIRECTION = 90
DOWN_DIRECTION = 270
RIGHT_DIRECTION = 0
LEFT_DIRECTION = 180

# Snake class
# Snake() constructor
# snake.move()

class Snake:
    def __init__(self, segments):
        self.snake_list = []
        self.length = segments
        self.segmentsize = 20
        self.head = None
        
        tx = 0
        ty = 0
        
        for segs in range(self.length):
            snake = Turtle(shape="square")
            snake.teleport(tx, ty)
            snake.color("white")
            snake.speed("normal") 
            snake.penup()
            self.snake_list.append(snake)
            tx -= self.segmentsize
        self.head = self.snake_list[0]
    def move(self): # Method
        for seg_num in range(self.length-1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)
    
        self.head.forward(MOVE_DISTANCE)
    # snake cannot go over itself - hence we check for the opposite direction
    def up(self):        
        if self.head.heading() != DOWN_DIRECTION:
            self.head.setheading(UP_DIRECTION)
    def down(self):
        if self.head.heading() != UP_DIRECTION:
            self.head.setheading(DOWN_DIRECTION)
    def right(self):
        if self.head.heading() != LEFT_DIRECTION:
            self.head.setheading(RIGHT_DIRECTION)
    def left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.setheading(LEFT_DIRECTION)
        