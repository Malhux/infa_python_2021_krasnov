import turtle as t
t.shape('classic')
t.color('blue')
t.width(2)
t.speed(100)
def okrL(a):                                 #окружность против часовой стрелки
    for i in range(1000):                     
        t.forward(a)
        t.left(180-180*998/1000)
def okrR(a):                                 #окружность по часовой стрелки
    for i in range(1000):
        t.forward(a)
        t.right(180-180*998/1000)
b=0.3
t.left(90)
for j in range(10):
    okrL(b)
    okrR(b)
    b+=0.05