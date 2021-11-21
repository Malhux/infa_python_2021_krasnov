import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
color = (255, 255, 255)

pygame.draw.rect               #рисует прямоугольник
pygame.draw.polygon            #рисует многоугольник
pygame.draw.circle             #рисует круг
pygame.draw.ellipse            #рисует эллипс
pygame.draw.arc                #рисует эллиптическую дугу
pygame.draw.line               #рисует прямую линию
pygame.draw.lines              #рисует несколько смежных отрезков прямых линий
pygame.draw.aaline             #рисует прямую сглаженную линию
pygame.draw.aalines            #рисует несколько смежных сглаженных отрезков прямых

#Все функции модуля pygame.draw в качестве первого аргумента принимают экран, 
# на котором нужно рисовать (приложение может открывать и несколько окон, нужно точно знать, на каком рисовать). 
# Второй аргумент - цвет, заданный кортежем из трех чисел от 0 до 255 в формате RGB. 
# Также возможно наличие четвертого числа - прозрачности. 
# После этого следуют координаты фигуры (для каждой фигуры свой формат задания координат), далее - параметр width. 
# Если передать в этот параметр положительное значение, оно будет означать толщину линии. 
# Если параметр равен 0 (значение по умолчанию), фигура будет полностью закрашеной.

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:            #цикл для рисования
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()