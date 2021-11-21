import turtle as t
from random import *
t.shape('circle')
t.speed(8)
t.color('blue')
for i in range(150):
    t.forward(randint(1,100))
    t.left(randint(0,360))