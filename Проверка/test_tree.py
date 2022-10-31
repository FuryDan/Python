import queue
from threading import Thread, active_count
from turtle import Turtle, Screen

def forward(turtle, distance):
    graphics.put((turtle.forward, distance))

def right(turtle, angle):
    graphics.put((turtle.right, angle))

def left(turtle, angle):
    graphics.put((turtle.left, angle))

def fractalright(turtle, angle, length):
    forward(turtle, length)

    if length - 20 > 0:
        right(turtle, angle)
        fractalright(turtle, angle, length - 20)
        left(turtle, angle)
        fractalright(turtle, -angle, length - 20)

    forward(turtle, -length)

def fractalleft(turtle, angle, length):
    forward(turtle, length)

    if length - 20 > 0:
        left(turtle, angle)
        fractalleft(turtle, angle, length - 20)
        right(turtle, angle)
        fractalleft(turtle, -angle, length - 20)

    forward(turtle, -length)

def process_queue():
    while not graphics.empty():
        action, argument = graphics.get()
        action(argument)

    if active_count() > 1:
        screen.ontimer(process_queue, 100)

START_X, START_Y = 0, -200

screen = Screen()
screen.mode('logo')  # make starting direction 0 degrees towards top

tree1 = Turtle(visible=False)
tree1.color('green')
tree1.penup()
tree1.goto(START_X, START_Y)
tree1.pendown()

tree2 = Turtle(visible=False)
tree2.color('dark green')
tree2.penup()
tree2.goto(START_X, START_Y)
tree2.pendown()

graphics = queue.Queue(1)  # size = number of hardware threads you have - 1

def fractal1():
    fractalright(tree1, 30, 100)

def fractal2():
    fractalleft(tree2, 30, 100)

thread1 = Thread(target=fractal1)
thread1.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread1.start()

thread2 = Thread(target=fractal2)
thread2.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread2.start()

process_queue()

screen.exitonclick()