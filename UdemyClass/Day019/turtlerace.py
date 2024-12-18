from turtle import Turtle, Screen
import random

tim = Turtle(shape="turtle")
screen = Screen()


screen.title("The Turtle Race")
screen.setup(width=500, height=400)

# 0,0 = center
# Y range 200 to -200
# X range -250 to 250

tim.speed("fastest") 

tim.hideturtle()

# starting line
tim.pencolor("green")
tim.pensize(3)
tim.teleport(-220,199)
tim.right(90)

for dashline in range(0, 388, 10):
    tim.pendown()
    tim.forward(5)
    tim.up()
    tim.forward(5)
    
tim.left(90)

# finish line
tim.pencolor("black")
tim.pensize(5)
tim.pendown()
tim.teleport(230,199)
tim.right(90)
tim.forward(199+189)

#tim.teleport(x=-235,y=0)
#tim.goto(x=-250, y=0)
#tim.left(90)
#tim.hideturtle()

race_ended = False

user_bet = screen.textinput(title="Make Your Bet!", prompt="Which turtle will win the race? Enter a color: ")
print(f"You bet on {user_bet} to win.\n")

if user_bet:
    race_ended = True

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(colors)
racing_turtles =[]

# create race turtles
tx = -235
ty = 125
for t in range(0, len(colors)):
    racer = Turtle(shape="turtle")
    racer.hideturtle()
    racer.color(colors[t])
    #print(f"color = {racer.color()} {type(racer.color())}")
    racer.teleport(tx, ty)
    racer.showturtle()
    racing_turtles.append(racer)
    ty -= 50
    
while race_ended == True:
    x = 0
    while x < len(colors) and race_ended == True:
        racer = racing_turtles[x]
        x += 1 
    #for racer in racing_turtles:
        turtle_step = random.randint(0, 10)
        racer.penup()
        racer.forward(turtle_step)
        
        if racer.xcor() >= 230:
            race_ended = False
            print(f"{racer.color()[0]} won the race!!!\n\n")
            if racer.color()[0] == user_bet:
                print("Your turtle won.")
            else:
                print(f"You lost.")



screen.exitonclick()