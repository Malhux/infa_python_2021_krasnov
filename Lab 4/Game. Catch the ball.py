import pygame
from pygame.draw import *
from random import *

pygame.init()


def main():
    '''
    The main function. We will work in it and define other functions here
    '''
    button_width = 300                    #sizes of start_button
    button_height = 100
    started_already = False
    font = pygame.font.Font(None, 50)
    score = 0
    screen_width = 1200                  #sizes of the screen
    screen_height = 800
    FPS = 60
    TIME = 30                           #programm's time in seconds
    time_out_begin = TIME * FPS
    time_out = time_out_begin
    screen = pygame.display.set_mode((screen_width, screen_height))
    ticks = 0
    ended = False
    finished = False
    
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
    
    def highscore(score):
        '''This function count my score'''
        font = pygame.font.Font(None, 50)
        clock = pygame.time.Clock()
        input_box = pygame.Rect((screen_width - button_width) /2 + 15, screen_height / 2 - 10, button_width - 15, 50)
        color_inactive = (100, 100, 100)
        color_active = (0, 0, 0)
        color = color_inactive
        active = False
        text = ''
        done = False
        
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):          #check if the mouse is in rect of the start of the game
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            with open('desktop/Labs Python/Lab 4/highscores.txt', 'a') as f:
                                print(text + ': ' + str(score), file=f)
                                finished = True
                                return
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                    
            screen.fill((0, 0, 0))
            rect(screen, (255,218,158), ((screen_width - button_width) / 2, (screen_height - button_height) / 2, button_width, button_height))
            name_text = font.render('Enter your name ', 1, (99, 128, 255))
            screen.blit(name_text, ((screen_width - button_width) / 2 + 11, (screen_height - button_height) / 2 + 3))
            txt_surface = font.render(text, True, color)
            width = button_width - 30
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(30)

    
    def create_new_ball():
        '''Create new ball and get all information about in in dictionary
        Create random x, y coordinates of the ball's centre. Create random ball's radius. Create randon vx and vy. Switch random color from colors' list
        Return the dictionary with ball's parametres'''
        x = randint(100, 1100)
        y = randint(100, 800)
        vx = randint(-5, 5)
        vy = randint(-5, 5)
        r = randint(20, 50)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)
        return {
                'vx': vx,
                'vy': vy,
                'x': x,
                'y': y,
                'r': r,
                'color': color
                }
        
    def create_super_ball():
        '''Create surer ball and get all information about it in dictionary
        Create random x, y coordinates of the ball's centre. Create random ball's radius. Create randon vx and vy. Switch random color from colors' list
        Return the dictionary with ball's parametres'''
        x = randint(100, 1100)
        y = randint(100, 800)
        vx = randint(-10, 10)
        vy = randint(-10, 10)
        r = randint(20, 30)
        color = COLORS[randint(0, 5)]
        for i in range(r):
            red, green, blue = color
            circle(screen, ((red - i) % 255, (green - i) % 255, (blue) % 255), (x, y), r)
        return {
                'vx': vx,
                'vy': vy,
                'x': x,
                'y': y,
                'r': r,
                'color': color
                }
    
    balls = [create_new_ball() for i in range(10)]              #list of dictionaries with ball's parametres
    super_balls = [create_super_ball() for i in range(2)]
    pygame.display.update()
    clock = pygame.time.Clock()
    screen.fill(BLACK)
    
    while not finished:
        clock.tick(FPS)     
        for ball in balls:                                    #draw balls and move it
            circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
            ball['x'] += ball['vx']
            ball['y'] += ball['vy']
            if ball['x'] >= screen_width or ball['x'] <= 0:
                ball['vx'] *= -1
            if ball['y'] >= screen_height or ball['y'] <= 0:
                ball['vy'] *= -1
                
        for super_ball in super_balls:
            for i in range(super_ball['r']):
                red, green, blue = super_ball['color']
                circle(screen, ((red - i * 40) % 255, (green - i * 20) % 255, (blue) % 255), (super_ball['x'], super_ball['y']), super_ball['r'] - i)
            super_ball['x'] += super_ball['vx']
            super_ball['y'] += super_ball['vy']
            ticks += 1
            if ticks > FPS / 2:
                super_ball['vx'] = randint(-10, 10)
                super_ball['vy'] = randint(-10, 10)
                ticks = 0
            if super_ball['x'] >= screen_width or super_ball['x'] <= 0:
                super_ball['vx'] *= -1
            if super_ball['y'] >= screen_height or super_ball['y'] <= 0:
                super_ball['vy'] *= -1
        
        if not started_already:
            screen.fill(BLACK)
            clicked = False
            
            while not clicked:
                rect(screen, (255, 218, 158), ((screen_width - button_width) / 2, (screen_height - button_height) / 2, button_width, button_height))
                text = font.render('START', 1, (99, 128, 255))
                screen.blit(text, (screen_width / 2 - 53, screen_height / 2 - 13))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        if mouse_x <= (screen_width + button_width) / 2 and mouse_x >= (screen_width - button_width) / 2 and mouse_y <= (screen_height + button_height) / 2 and mouse_y >= (screen_height - button_height) / 2:
                            clicked = True                  #start the game
                            started_already = True
                          
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i, ball in enumerate(balls):
                    if (ball['x'] - mouse_x) ** 2 + (ball['y'] - mouse_y) ** 2 <= ball['r'] ** 2:
                        balls[i] = create_new_ball()
                        score += 1
                for i, super_ball in enumerate(super_balls):
                    if (super_ball['x'] - mouse_x) ** 2 + (super_ball['y'] - mouse_y) ** 2 <= super_ball['r'] ** 2:
                        super_balls[i] = create_super_ball()
                        score += 5
                        
        text = font.render('Score: ' + str(score), 1, (255, 255, 255))
        screen.blit(text, (0, 30))
        text = font.render('Time: ' + str(int(time_out/FPS * 10) / 10), 1, (255, 255, 255))
        screen.blit(text, (0, 0))
        time_out -= 1
        if time_out > 0:
            pygame.display.update()
            screen.fill(BLACK)
        else:
            highscore(score)
            with open('desktop/Labs Python/Lab 4/highscores.txt', 'r') as file:
                sorted_data=sorted(file.readlines(), 
                                   key=lambda item: int(item.rsplit(':',1)[-1].strip()))

            for i in range(int(len(sorted_data)/2)):
                b = sorted_data[i]
                sorted_data[i] = sorted_data[-1*i-1]
                sorted_data[-1*i-1] = b 

            out = open('desktop/Labs Python/Lab 4/highscores2.txt', 'w')
            for i in range(int(len(sorted_data))):
                out.write(sorted_data[i])
            out.close()
            return
            
    pygame.quit()

while True:
    main()