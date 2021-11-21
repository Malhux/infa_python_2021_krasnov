import turtle as t
import numpy as np
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
a = input('Введите цифры через пробел:').split()
for j in range(len(a)):
    a[j]=int(a[j])
for k in range(len(a)):
    if a[k] == 0:
        nol()
    elif a[k] == 1:
        odin()
    elif a[k] == 2:
        dva()
    elif a[k] == 3:
        tri()
    elif a[k] == 4:
        cheture()
    elif a[k] == 5:
        pyat()
    elif a[k] == 6:
        schect()
    elif a[k] == 7:
        sem()
    elif a[k] == 8:
        vosem()
    else:
        devyat()