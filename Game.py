import os
import pygame
import random

def Game_Intro():

    x = 50
    y = 50
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.init()

    displayX = 1000
    displayY = 700
    
    window = pygame.display.set_mode((displayX,displayY))
    displayAliens_event = pygame.USEREVENT + 1
    pygame.event.post(pygame.event.Event(displayAliens_event))

    xCord = 25
    yCord = 25
    width = 50
    height = 50
    spacing = 25
    red = 0
    green = 0
    blue = 0
    RGB = (red, green, blue)
    run = True



    while run:
        pygame.time.delay(5)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                run = False
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False    
            if event.type == displayAliens_event:
                    pygame.draw.rect(window, RGB, (xCord, yCord, width, height))
                    pygame.display.update()
                    xCord += spacing + width
                    if xCord + width < displayX:
                        pygame.event.post(pygame.event.Event(displayAliens_event))
                    else :
                        xCord = 25
                        yCord += spacing + height
                        if yCord+height < displayY:
                            pygame.event.post(pygame.event.Event(displayAliens_event))
                        else :
                            xCord = 25
                            yCord = 25
                            red = random.randint(0,255)
                            green = random.randint(0,255)
                            blue = random.randint(0,255)
                            RGB = (red, green, blue)
                            pygame.event.post(pygame.event.Event(displayAliens_event))
                            

def main():
    Game_Intro()

if __name__ == "__main__":
    main()