from turtle import Turtle, Screen
import random
import math
import colorgram

# using aliasing
# import turtle as t

colors = ["AliceBlue", 
          "purple", 
          "BlueViolet", 
          "DarkSeaGreen3", 
          "pink", 
          "DarkOrchid2", 
          "burlywood4", 
          "green", 
          "blue", 
          "red",
          "DarkGray",
          "gold1",
          "MistyRose",
          "goldenrod3",
          "SlateGray2",
          "wheat",
          "RoyalBlue"]

def random_color_tuple():
    # return random color tuple
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
    
jamie_the_turtle = Turtle()
jamie_the_turtle.shape("turtle")
jamie_the_turtle.color("chocolate4")

#jamie_the_turtle.forward(100)
#jamie_the_turtle.right(90)

# draw a square
# jamie_the_turtle.forward(100)
# jamie_the_turtle.right(90)
# jamie_the_turtle.forward(100)
# jamie_the_turtle.right(90)
# jamie_the_turtle.forward(100)
# jamie_the_turtle.right(90)
# jamie_the_turtle.forward(100)

# # draw a square - more efficiently
# for jman in range(4):
#      jamie_the_turtle.forward(100)
#      jamie_the_turtle.right(90)

# # draw a dashed line
# for jman in range(15):
#     jamie_the_turtle.pendown()
#     jamie_the_turtle.forward(10)
#     jamie_the_turtle.penup()
#     jamie_the_turtle.forward(10)

# randomize colors
random.shuffle(colors)  

# # draw a series of shapes
# for shape in range(3,11):
#     jamie_the_turtle.color(colors[shape])
#     print(f"Shape = {shape} sides/color = {colors[shape]}")
#     for side in range(1,shape+1):
#         jamie_the_turtle.forward(100)
#         angle = 360/shape
#         jamie_the_turtle.right(angle)  

# random walk
# screen = Screen()
# screen.colormode(255)

# walks = random.randint(1,500)

# walker_color = ["red", "green", "blue", "black"]
# walker_direction = [0, 90, 180, 270]

# jamie_the_turtle.speed("fastest")
# for walker in range(1,walks):
#     print(f"Path {walker} of {walks}")
#     #jamie_the_turtle.color(walker_color[random.randint(0,3)])
    
#     my_tuple = random_color_tuple()
#     print(f"Color Tuple = {my_tuple}")
    
#     jamie_the_turtle.pencolor(my_tuple)
#     jamie_the_turtle.pensize(random.randint(1,10))
#     walk_length = random.randint(10,100)
    
#     jamie_the_turtle.forward(walk_length)
#     jamie_the_turtle.setheading(walker_direction[random.randint(0,3)])     
    
# spirograph
screen = Screen()
screen.colormode(255)

my_tuple = random_color_tuple()
jamie_the_turtle.pencolor(my_tuple)

jamie_the_turtle.home()
print(f"x = {jamie_the_turtle.xcor()} y = {jamie_the_turtle.ycor()}")

# center of first circle will be (x = 0 , y = 100)
# we want to draw the next circle on a point on the origonal circle, 10 degrees away, so we will have 36 circles
# x = 100 * cos(n) + 0
# y = 100 * sin(n) + 100

# jamie_the_turtle.circle(100)

# print(f"x = {jamie_the_turtle.xcor()} y = {jamie_the_turtle.ycor()}")

# jamie_the_turtle.left(90)
# jamie_the_turtle.forward(100)
# print(f"Center x = {jamie_the_turtle.xcor()} y = {jamie_the_turtle.ycor()}")

# jamie_the_turtle.speed("fastest")

# for n in range(0, 360, 10):
#     # convert degrees to radians
#     myradians = n * (math.pi/180)
#     x = 100 * math.cos(myradians) + 0 
#     y = 100 * math.sin(myradians) + 100
#     jamie_the_turtle.teleport(x,y)
#     #jamie_the_turtle.dot(5)
    
#     my_tuple = random_color_tuple()
#     jamie_the_turtle.pencolor(my_tuple)
#     jamie_the_turtle.circle(100)
    
# # could also use heading() & setheading()
# jamie_the_turtle.teleport(0,0)    

# for n in range(0, 360, 10):
#     my_tuple = random_color_tuple()
#     jamie_the_turtle.pencolor(my_tuple)
#     jamie_the_turtle.circle(100)
#     jamie_the_turtle.setheading(jamie_the_turtle.heading() + 10)
    
# create a Hirst style image 10 x 10 = 100 dots
rgb_colors = []
colors = colorgram.extract('myimage.jpg', 50)
for color in colors:
    #print(color.rgb.r, color.rgb.g, color.rgb.b)
    mytuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(mytuple)

#print(rgb_colors)  

jamie_the_turtle.speed("fastest")  
jamie_the_turtle.teleport(0,0) 

print(rgb_colors[0][0], rgb_colors[0][1], rgb_colors[0][2])

for x in range (0,10):
    for y in range (0,10):
        # print a row of dots
        jamie_the_turtle.teleport(50*x-200, 50*y-100)
        #jamie_the_turtle.pencolor(random.choice(rgb_colors))
        jamie_the_turtle.dot(20, random.choice(rgb_colors))
 
# move turtle off the painting       
jamie_the_turtle.teleport(-300, -300)
        
# jamie_the_turtle.teleport(0,0)
# jamie_the_turtle.pencolor(random.choice(rgb_colors))
# jamie_the_turtle.dot(5)

# jamie_the_turtle.teleport(10,0)
# jamie_the_turtle.pencolor(random.choice(rgb_colors))
# jamie_the_turtle.dot(5)






screen.exitonclick()

# # installed via pip
# import heroes
# print(heroes.gen())
