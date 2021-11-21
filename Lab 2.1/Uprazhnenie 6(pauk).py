import turtle as t
n=int(input('Введите количество лапок паука:'))
t.speed(5)
t.shape('turtle')
for i in range (n):
    t.forward(200)
    t.stamp()
    t.right(180)
    t.forward(200)
    t.right(180+360/n)