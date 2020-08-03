import os
import pygame

def Game():

    x = 50
    y = 50
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.init()

    displayX = 1000
    displayY = 700
    window = pygame.display.set_mode((displayX, displayY))
    
    run = True

    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = false

def main():
    Game()

if __name__ == "__main__":
    main()