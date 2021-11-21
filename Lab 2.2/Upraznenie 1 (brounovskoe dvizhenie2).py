import turtle as t
from random import *
t.shape('circle')
t.color('red')
t.speed(5)
t.width(2)
for i in range(200):
    t.goto(randint(-300,300), randint(-300,300))