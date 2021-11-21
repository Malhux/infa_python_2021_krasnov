import turtle as t
t.shape('turtle')
t.speed(1)
def okrR(a):                                 #окружность по часовой стрелки
    for i in range(100):
        t.forward(a)
        t.right(180-180*98/100)
def duga(b):                         #рисуем половину окружности
    for i in range(50):
        t.forward(b)
        t.right(3.6)

#Лицо
t.penup()
t.goto(0,159)
t.pendown()
t.begin_fill()
okrR(10)
t.color('yellow')
t.end_fill()

#Левый глаз
t.penup()
t.goto(-70,90)
t.color('black')
t.pendown()
t.begin_fill()
okrR(1)
t.color('green')
t.end_fill()

#Правый глаз
t.penup()
t.goto(70,90)
t.color('black')
t.pendown()
t.begin_fill()
okrR(1)
t.color('green')
t.end_fill()

#Нос
t.penup()
t.goto(0,30)
t.color('black')
t.pendown()
t.right(90)
t.width(8)
t.forward(45)

#Рот
t.penup()
t.goto(75,-60)
t.color('red')
t.pendown()
t.width(10)
duga(4.5)