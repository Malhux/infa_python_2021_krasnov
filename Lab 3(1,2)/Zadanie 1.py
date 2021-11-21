import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((800, 800))
grey = (192, 192, 192)
black = (0, 0, 0)
rect(screen, grey, (0, 0, 800, 800), 0)
yellow = (255, 255, 0)
circle(screen, yellow, (400, 400), 300, 0)
circle(screen, black, (400, 400), 300, 2)
red = (255, 0, 0)
circle(screen, (0, 0, 255), (260, 300), 60, 0)
circle(screen, black, (260, 300), 60, 2)
circle(screen, (0, 0, 255), (560, 300), 40, 0)
circle(screen, black, (560, 300), 40, 2)
circle(screen, black, (260, 300), 25, 0)
circle(screen, black, (560, 300), 20, 0)
rect(screen, black, (260, 550, 300, 50), 0)
polygon(screen, black, [(323, 280), (338, 265), (198, 125), (183, 140)], 0)
polygon(screen, black, [(513, 290), (498, 275), (578, 195), (593, 210)], 0)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:        
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()