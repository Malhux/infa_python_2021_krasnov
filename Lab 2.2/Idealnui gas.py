import turtle as t
from random import *
t.penup()
t.speed(0)
t.goto(-350, 350)
t.pendown()
t.color('red')
t.width(8)
t.goto(350, 350)
t.goto(350, -350)
t.goto(-350, -350)
t.goto(-350, 350)
t.penup()
t.goto(0, 0)
t.shape('circle')
t.color('black')
nums_turt = 25
times = 50
turtles = [t.Turtle(shape='circle') for i in range(nums_turt)]
for turtle in turtles:
    turtle.penup()
    turtle.speed(50)
    turtle.goto(randint(-200,200), randint(-200,200))
for j in range(times):
    for turtle in turtles:
        turtle.penup()
        turtle.speed(6)
        turtle.right(randint(0, 360))
        turtle.forward(randint(25,100))
    t.speed(6)
    t.right(randint(0, 360))
    t.forward(randint(0,50))