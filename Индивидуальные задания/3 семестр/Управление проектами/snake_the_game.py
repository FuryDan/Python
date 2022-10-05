import turtle
import time
from random import randrange

# Constants
score = 0
high_score = 0
delay = 0.1

# Creating a window screen
wind = turtle.Screen()
wind.title("Snake : The Best Game EVER!")
wind.bgcolor("#6d9057")

# Draw a start menu loading
loading_screen = turtle.Screen()
loading_screen.setup(650, 650)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 30)
pen.write("Loading, please wait...", align="center",
font=("Agency FB", 40, "bold"))
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write("You can move, using 'wasd'.", align="center",
font=("Agency FB", 10, "bold"))
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, -15)
pen.write("Beware of the borders!", align="center",
font=("Agency FB", 10, "bold"))

# Draw a game field border
border = turtle.Turtle()
border.hideturtle()
border.penup() 
for k in range(309, 311):
    border.goto(-k, k)
    border.pendown()
    border.goto(k, k)
    border.goto(k, -k)
    border.goto(-k, -k)
    border.goto(-k, k)
pen.clear()

# The wind width and height
wind.setup(650, 650)
wind.tracer(0)

# Head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("black", "white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food in the game
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color("black", "red")
food.penup()
food.goto(randrange(-280, 280, 20), randrange(-280, 280, 20))
 
# Game score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
font=("Times New Roman", 24, "bold", "italic"))

# Assigning key directions
def go_up():
    if head.direction != "dowind":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "dowind"

def go_left():
    if head.direction != "right":
        head.direction = "left"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "dowind":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
wind.listen()
wind.onkeypress(go_up, "w")
wind.onkeypress(go_down, "s")
wind.onkeypress(go_left, "a")
wind.onkeypress(go_right, "d")
segments = []

# Main Gameplay 
while True:
    wind.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Times New Roman", 24, "bold", "italic"))
    if head.distance(food) < 20:
        food.goto(randrange(-280, 280, 20), randrange(-280, 280, 20))
 
        # Adding segment
        # Make it more patriotic
        if score == 0:
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")         # tail shape
            new_segment.color("black", "blue")  # tail colour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
        elif score == 10:
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")        # tail shape
            new_segment.color("black", "red")  # tail colour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10

        # Adding partially invisible segment 
        elif score >= 20:
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")            # tail shape
            new_segment.color("black", "#6d9057")  # tail colour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Times New Roman", 24, "bold", "italic"))
    
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("Times New Roman", 24, "bold", "italic"))
    time.sleep(delay)
 
wind.mainloop()