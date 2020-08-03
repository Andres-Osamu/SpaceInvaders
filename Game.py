import os
import pygame
from colour import Color
from PIL import ImageColor

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
    run = True

    counter = 0
    xred = Color("red")
    colors = list(xred.range_to(Color("blue"), 13))
    rgb = ImageColor.getcolor(str(colors[0]), "RGB")

    while run:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False    
            if event.type == displayAliens_event:
                    RGB = ImageColor.getcolor(str(colors[counter]), "RGB")
                    pygame.draw.rect(window, RGB, (xCord, yCord, width, height))
                    pygame.display.update()
                    xCord += spacing + width
                    counter +=1
                    if counter == 13:
                        counter = 0
                    if xCord + width < displayX:
                        pygame.event.post(pygame.event.Event(displayAliens_event))
                    else :
                        xCord = 25
                        yCord += spacing + height
                        if yCord+height < displayY:
                            pygame.event.post(pygame.event.Event(displayAliens_event))
                        # else :
                        #     xCord = 25
                        #     yCord = 25
                        #     # pygame.event.post(pygame.event.Event(displayAliens_event))
                            

def main():
    Game_Intro()

if __name__ == "__main__":
    main()