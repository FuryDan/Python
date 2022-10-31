import turtle
from colorsys import hsv_to_rgb

wind = turtle.Screen()
wind.setup(650, 650)

wind.tracer(0)
loading_form = turtle.Turtle()
loading_form.hideturtle()
loading_form.speed(0)
loading_form.width(7)
loading_form.penup()
loading_form.sety(-300)
loading_form.pendown()
for angle in range(360):
    loading_form.color("black")
    loading_form.circle(300, 1)

wind.tracer(1)
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

wind.exitonclick()