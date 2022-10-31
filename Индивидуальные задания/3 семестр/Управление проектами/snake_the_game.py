import turtle
import time
from random import randrange
from colorsys import hsv_to_rgb

# Restarting game def
def restart_game():
    pen_lost.clear()
    close.clear()
    head.showturtle()
    food.goto(randrange(-280, 280, 20), randrange(-280, 280, 20))
    wind.bgcolor("#6d9057")
    wind.onkeypress(None, "q")
    wind.onkeypress(None, "Q")
    wind.onkeypress(None, "r")
    wind.onkeypress(None, "R")
    pen.write(f"Score : {score} High Score : {high_score} ", 
    align="center", font=("Tw Cen MT", 24, "normal", "italic"))

# Quiting game def
def quit_game():
    wind.bye()

# Choosing after death def
def choose(w):
    time.sleep(1)
    head.direction = "Stop"
    pen.clear()
    score = 0
    delay = 0.1
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    food.goto(1000,1000)
    head.goto(0, 0)
    head.hideturtle()
    w.bgcolor("red")
    pen_lost.write('You lost.', align="center", 
    font = ("Tw Cen MT", 20, "normal"))
    close.write('Press "Q" to exit, or "R" to restart.', 
    align="center", font = ("Tw Cen MT", 20, "normal"))
    head.direction = "Stop"
    w = turtle.Screen()
    w.listen()
    w.onkeypress(quit_game, "q")
    w.onkeypress(quit_game, "Q")
    w.onkeypress(restart_game, "r")
    w.onkeypress(restart_game, "R")

# Constants
score = 0
high_score = 0
delay = 0.1
pen_lost = turtle.Turtle()
pen_lost.hideturtle()
pen_lost.speed(0)
pen_lost.penup()
pen_lost.goto(0, 0)
close = turtle.Turtle()
close.hideturtle()
close.speed(0)
close.penup()
close.goto(0,-30)

# Creating a window screen
wind = turtle.Screen()
wind.title("Snake : The Best Game EVER!")
wind.bgcolor("#6d9057")

# Creating a start menu loading
loading_screen = turtle.Screen()
loading_screen.setup(650, 650)
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, -30)
pen.write("Loading, please wait...", align="center",
font=("Tw Cen MT", 40, "normal"))

# Let's show some hints
pen_hint = turtle.Turtle()
pen_hint.hideturtle()
pen_hint.color("white")
pen_hint.penup()
pen_hint.goto(0, -230)
rand = randrange(1, 4)
if rand == 1: 
    pen_hint.write("Hint: You can move, using 'wasd' or '↑↓←→'.", 
    align="center", font=("Tw Cen MT", 12, "normal"))
if rand == 2: 
    pen_hint.write("Hint: Beware of the borders!", 
    align="center", font=("Tw Cen MT", 12, "normal"))
if rand == 3: 
    pen_hint.write("Hint: Don't eat yorself!", 
    align="center", font=("Tw Cen MT", 12, "normal"))
if rand == 4: 
    pen_hint.write("Hint: .", 
    align="center", font=("Tw Cen MT", 12, "normal"))

# Draw loading form
loading_screen.tracer(0)
loading_form = turtle.Turtle()
loading_form.hideturtle()
loading_form.speed(0)
loading_form.width(9)
loading_form.penup()
loading_form.sety(-300)
loading_form.pendown()
for angle in range(360):
    loading_form.color("black")
    loading_form.circle(300, 1)

# Draw loading
loading_screen.tracer(2)
loading = turtle.Turtle()
loading.hideturtle()
loading.speed(0)
loading.width(5)
loading.penup()
loading.sety(-300)
loading.pendown()
for angle in range(360):
    loading.pencolor(hsv_to_rgb(angle / 360, 0.75, 0.75))
    loading.circle(300, 1)

# Clear everything that gets in the way
loading_form.clear()
loading.clear()
pen.clear()
pen_hint.clear()

# The wind width and height
wind.setup(650, 650)
wind.tracer(0)

# Draw a game field borders
borders = turtle.Turtle()
borders.hideturtle()
borders.penup() 
for k in range(291, 310):
    borders.goto(-k, k)
    borders.pendown()
    borders.goto(k, k)
    borders.goto(k, -k)
    borders.goto(-k, -k)
    borders.goto(-k, k)

# Game score
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center", 
font=("Tw Cen MT", 24, "normal", "italic"))

# Head of the snake
head = turtle.Turtle()
head.shape("circle")         # head shape
head.fillcolor("white")      # head color
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food in the game
food = turtle.Turtle()
food.speed(0)
food.shape('circle')         # food shape
food.fillcolor("red")        # food color
food.penup()
food.goto(randrange(-280, 280, 20), randrange(-280, 280, 20))

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
wind.onkeypress(go_up, "W")
wind.onkeypress(go_up, "Up")
wind.onkeypress(go_left, "a")
wind.onkeypress(go_left, "A")
wind.onkeypress(go_left, "Left")
wind.onkeypress(go_down, "s")
wind.onkeypress(go_down, "S")
wind.onkeypress(go_down, "Down")
wind.onkeypress(go_right, "d")
wind.onkeypress(go_right, "D")
wind.onkeypress(go_right, "Right")
segments = []

# Main Gameplay 
while True:
    wind.update()
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor(
    ) > 280 or head.ycor() < -280:
        choose(wind)
    if head.distance(food) < 20:
        food.goto(randrange(-280, 280, 20), randrange(-280, 280, 20))
 
        # Adding segment
        # Make it more patriotic
        if score == 0:
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")         # tail shape
            new_segment.fillcolor("blue")       # tail fillcolour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
        elif score == 10:
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")        # tail shape
            new_segment.fillcolor("red")       # tail fillcolour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10

        # Adding partially invisible segment 
        elif score >= 20:
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")            # tail shape
            new_segment.fillcolor("#6d9057")       # tail fillcolour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score : {score} High Score : {high_score} ", 
        align="center", font=("Tw Cen MT", 24, "normal", "italic"))
    
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
            choose(wind)
    time.sleep(delay)
 
wind.mainloop()