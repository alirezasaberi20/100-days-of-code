
from turtle import Turtle,Screen
import random
every_thing_ok = False

timmy = Turtle()

screen = Screen()
screen.exitonclick()
timmy.shape("turtle")
#timmy.color("green")
colors = ["red","green","yellow","blue","brown","orange","purple","black","light blue"]
for num_sides in range(4,35):
    timmy.color(random.choice(colors))
    for _ in range(num_sides):
        angle = 360 / num_sides
        
        timmy.forward(10)
        timmy.right(angle)