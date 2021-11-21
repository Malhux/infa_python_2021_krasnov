import turtle as t
t.shape('circle')
t.speed(0)
t.goto(750,0)
t.goto(-750,0)
Vx = 15
Vy = 60
g = 10
dt = 0.07
x = -750
y = 0
for i in range(1430):
    if y >= 0:
        x = x + Vx*dt
        y = y + Vy*dt - g*dt**2/2
        Vy = Vy - g*dt
        t.goto(x, y)
    else:
        Vy = -0.9*Vy
        x = x + Vx*dt
        y = y + Vy*dt - g*dt**2/2
        Vy = Vy - g*dt
        t.goto(x, y)