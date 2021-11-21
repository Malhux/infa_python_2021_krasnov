import pygame
from pygame import transform
from pygame.draw import *
from pygame.transform import *
import numpy as np
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
blue = (0, 184, 217)
grey = (133, 150, 150)
white = (255, 255, 255)
green = (153, 255, 153)
dark_green = (80, 200, 120)
yellow = (255, 255, 0)
purple = (128, 0, 255)
black = (0, 0, 0)

#небо
rect(screen, blue, (0, 0, 600, 400), 0)           

#трава
rect(screen, green, (0 ,400, 600, 400), 0)     

#горы
polygon(screen, grey, [(0, 250), (60, 100), (120, 200), (200, 125), (380, 280), (430, 110), (470, 140), (600, 50), (600, 450), (350, 450), (330, 400), (0, 400), (0, 250)], 0)
polygon(screen, black, [(0, 250), (60, 100), (120, 200), (200, 125), (380, 280), (430, 110), (470, 140), (600, 50), (600, 450), (350, 450), (330, 400), (0, 400), (0, 250)], 1)

#альпака
ellipse(screen, white, (200, 405, 50, 30), 0)    #голова
ellipse(screen, white, (205, 430, 35, 100), 0)   #шея
ellipse(screen, white, (85, 515, 150, 55), 0)    #туловище
ellipse(screen, white, (95, 550, 15, 35), 0)     #нога левая задняя 1
ellipse(screen, white, (95, 580, 15, 35), 0)     #нога левая задняя 2
ellipse(screen, white, (98, 610, 20, 10), 0)    #нога левая задняя 3
ellipse(screen, white, (125, 560, 15, 35), 0)   #нога правая задняя 1
ellipse(screen, white, (125, 590, 15, 35), 0)   #нога правая задняя 2
ellipse(screen, white, (128, 620, 20, 10), 0)   #нога правая задняя 3
ellipse(screen, white, (185, 550, 15, 35), 0)   #нога левая передняя 1
ellipse(screen, white, (185, 580, 15, 35), 0)   #нога левая передняя 2
ellipse(screen, white, (188, 610, 20, 10), 0)   #нога левая передняя 3
ellipse(screen, white, (210, 555, 15, 35), 0)   #нога правая передняя 1
ellipse(screen, white, (210, 585, 15, 35), 0)   #нога правая передняя 2
ellipse(screen, white, (213, 615, 20, 10), 0)   #нога правая передняя 3
circle(screen, purple, (220, 418), 8, 0)        #глаз
circle(screen, black, (224, 418), 3, 0)         #зрачок
ellipse(screen, white, (218, 415, 5, 2), 0)     #блик
arc(screen, white, (205, 385, 12, 25), np.pi, 3*np.pi/2, 2) #рог 1
arc(screen, white, (200, 380, 12, 32), np.pi, 3*np.pi/2, 2) #рог 2

circle(screen, dark_green, (510, 630), 110, 0)     #клумба

#функция цветка
def cvetok(x, y, k):
    '''   Функция, рисующая цветок
    x, y - координаты левого верхнего угла центрального верхнего лепестка
    k - относительный размер цветка'''
    ellipse(screen, white, (x, y, 22*k, 11*k), 0)
    ellipse(screen, black, (x, y, 22*k, 11*k), 1)

    ellipse(screen, white, (x+10*k, y+3*k, 22*k, 11*k), 0)
    ellipse(screen, black, (x+10*k, y+3*k, 22*k, 11*k), 1)

    ellipse(screen, white, (x-9*k, y+4*k, 22*k, 11*k), 0)
    ellipse(screen, black, (x-9*k, y+4*k, 22*k, 11*k), 1)

    ellipse(screen, yellow, (x+2*k, y+9*k, 22*k, 11*k), 0)

    ellipse(screen, white, (x-12*k, y+11*k, 22*k, 11*k), 0)
    ellipse(screen, black, (x-12*k, y+11*k, 22*k, 11*k), 1)

    ellipse(screen, white, (x-4*k, y+15*k, 22*k, 11*k), 0)
    ellipse(screen, black, (x-4*k, y+15*k, 22*k, 11*k), 1)

    ellipse(screen, white, (x+14*k, y+10*k, 22*k, 11*k), 0)
    ellipse(screen, black, (x+14*k, y+10*k, 22*k, 11*k), 1)

    ellipse(screen, white, (x+10*k, y+15*k, 22*k, 11*k), 0)
    ellipse(screen, black, (x+10*k, y+15*k, 22*k, 11*k), 1)

#рисуем цветки (идут друг за другом  по часовой стрелке, начиная с центрального верхнего(12ч))
cvetok(506, 540, 1)
cvetok(548, 570, 1)
cvetok(563, 630, 1)
cvetok(505, 660, 1)
cvetok(453, 635, 1)
cvetok(440, 580, 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:        
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()