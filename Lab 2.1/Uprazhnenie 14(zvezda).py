import turtle as t
t.shape('square')
t.speed(3)
t.color('purple')
t.left(180)
t.width(1)
t.penup()
t.goto(150,65)
t.pendown()
def zvezda(n):                          #рисует звезду с n вершинами для нечетного n
    for i in range(n):
        t.forward(300)
        t.left((n-1)/2*360/n)
n=int(input('Введите n:'))
zvezda(n)