import turtle as t

t.speed(4)
t.color('blue')
t.penup()
t.goto(-150,30)
t.pendown()

with open('Desktop/Labs Python/Lab 2.2/Upr 3.2.txt', 'r+') as opened_file:
    s = opened_file.read()
print(s)