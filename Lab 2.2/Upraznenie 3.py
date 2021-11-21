import turtle as t
t.shape('turtle')
t.speed(3)
t.color('blue')
t.width(2)

#0
def nol():
    for i in range(2):
        t.forward(30)
        t.right(90)
        t.forward(60)
        t.right(90)
    t.penup()
    t.forward(45)
    t.pendown()

#1
def odin():
    t.right(90)
    t.penup()
    t.forward(30)
    t.left(135)
    t.pendown()
    t.forward(30*(2**0.5))
    t.right(135)
    t.forward(60)
    t.left(90)
    t.penup()
    t.forward(15)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()

#2
def dva():
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(45)
    t.forward(30*(2**0.5))
    t.left(135)
    t.forward(30)
    t.penup()
    t.forward(15)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()

#3
def tri():
    for i in range(2):
        t.forward(30)
        t.right(135)
        t.forward(30*(2**0.5))
        t.left(135)
    t.penup()
    t.forward(45)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()

#4
def cheture():
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.left(180)
    t.forward(60)
    t.penup()
    t.right(90)
    t.forward(15)
    t.pendown()

#5
def pyat():
    t.forward(30)
    t.left(180)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.left(180)
    t.penup()
    t.forward(45)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()

#6
def schect():
    t.penup()
    t.forward(30)
    t.right(135)
    t.pendown()
    t.forward(30*(2**0.5))
    t.left(135)
    for i in range(4):
        t.forward(30)
        t.right(90)
    t.penup()
    t.forward(45)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.pendown()

#7
def sem():
    t.forward(30)
    t.right(135)
    t.forward(30*(2**0.5))
    t.left(45)
    t.forward(30)
    t.penup()
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()

#8
def vosem():
    for i in range(2):
        t.forward(30)
        t.right(90)
        t.forward(60)
        t.right(90)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.penup()
    t.forward(15)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.pendown()

#9
def devyat():
    for i in range(6):
        t.forward(30)
        t.right(90)
    t.left(45)
    t.forward(30*(2**0.5))
    t.left(135)
    t.penup()
    t.forward(45)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()

t.penup()
t.goto(-200,30)
t.pendown()
input = open('Desktop/Labs Python/Lab 2.2/Upr 3.txt', 'r')      #вернуть ссылку на файл, с которого нужно будет считать содержимое, в переменную input
s = input.read()                                                #перейти по возвращенной ссылке и считать содержимое из файла в переменную s
input.close()
for j in range(len(s)):
    if s[j] == '0':
        nol()
    elif s[j] == '1':
        odin()
    elif s[j] == '2':
        dva()
    elif s[j] == '3':
        tri()
    elif s[j] == '4':
        cheture()
    elif s[j] == '5':
        pyat()
    elif s[j] == '6':
        schect()
    elif s[j] == '7':
        sem()
    elif s[j] == '8':
        vosem()
    elif s[j] == '9':
        devyat()
    else:                                       #для пробела = переход на новую строку
        t.penup()
        t.left(180)
        t.forward(270)
        t.left(90)
        t.forward(80)
        t.left(90)
        t.pendown()