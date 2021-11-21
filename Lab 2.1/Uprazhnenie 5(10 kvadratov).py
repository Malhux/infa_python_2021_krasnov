import turtle as t         #здесь и далее черепашку я буду вызывать через 't', а не через 'turtle'!
t.shape('turtle')
t.speed(5)
k=30
for i in range(10):
    for j in range(4):
        t.forward(k)
        t.right(90)
    t.penup()
    t.forward(k+45)
    t.left(90)
    t.forward(45)
    t.right(180)
    k+=90
    t.pendown()