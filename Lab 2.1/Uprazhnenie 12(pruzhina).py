import turtle as t
t.shape('circle')
t.color('yellow')
t.speed(100)
t.left(90)
t.penup()
t.goto(-350,0)
t.pendown()
def duga(a):                         #рисуем половину окружности
    for i in range(500):
        t.forward(a)
        t.right(0.36)
for j in range(5):
    duga(0.5)
    duga(0.1)