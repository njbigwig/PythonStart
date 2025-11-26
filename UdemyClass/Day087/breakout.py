# testing Copilot generation
"""
Breakout Game - Python Turtle Edition

🎮 How to Play:
- Use the LEFT and RIGHT arrow keys to move the paddle.
- Bounce the ball off the paddle to break all the bricks.
- Each brick gives you 10 points.
- If the ball falls below the paddle, the game is over.
- Destroy all bricks to win!

💡 Tips:
- Stay focused! The ball speeds up as you play.
- Try to aim the ball to hit multiple bricks in a row.
- You can restart the game by rerunning the script.

🔊 Sound:
- Sound effects play when the ball bounces or hits bricks.
- Make sure 'bounce.wav' is in the same folder (Windows only).

Enjoy the retro arcade fun!
"""

import turtle
import winsound  # For sound effects (Windows only)
import random

# Screen setup
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -200)
ball.dx = 3
ball.dy = 3

# Bricks
bricks = []

def create_bricks(rows=5, cols=10):
    colors = ["blue", "green", "yellow", "orange", "red"]
    for row in range(rows):
        for col in range(cols):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color(colors[row % len(colors)])
            brick.shapesize(stretch_wid=1, stretch_len=3)
            brick.penup()
            x = -350 + col * 75
            y = 250 - row * 30
            brick.goto(x, y)
            bricks.append(brick)

create_bricks()

# Paddle movement
def move_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 40)

def move_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 40)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Sound wrapper
def play_sound():
    try:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    except:
        pass  # Ignore if sound file is missing or unsupported

# Score setup
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-380, 260)
score_display.write(f"Score: {score}", align="left", font=("Courier", 16, "normal"))

# Game loop
def game_loop():
    global score
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall collision
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
        play_sound()

    if ball.ycor() > 290:
        ball.dy *= -1
        play_sound()

    # Paddle collision
    if (ball.ycor() < -240 and ball.ycor() > -250) and \
       (abs(ball.xcor() - paddle.xcor()) < 50):
        ball.dy *= -1
        play_sound()

    # Brick collision
    for brick in bricks:
        if brick.distance(ball) < 35:
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move off-screen
            bricks.remove(brick)
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="left", font=("Courier", 16, "normal"))
            play_sound()
            break

    # Game over
    if ball.ycor() < -290:
        ball.goto(0, -200)
        ball.dx = 0
        ball.dy = 0
        score_display.goto(0, 0)
        score_display.write("Game Over", align="center", font=("Courier", 24, "bold"))

    # Win condition
    if not bricks:
        score_display.goto(0, 0)
        score_display.write("You Win!", align="center", font=("Courier", 24, "bold"))
        ball.dx = 0
        ball.dy = 0

    screen.update()
    screen.ontimer(game_loop, 20)

game_loop()
screen.mainloop()

