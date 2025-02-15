import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"  # Suppresses the message
import pygame
from constants import *


def main():
    pygame.init() # initializes pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    fps = pygame.time.Clock()
    
    while True:
        #This is what starts the window/screen and gives it is size and color (pygame.Surface.fill(screen, "black") did thing
        screen.fill("black") 

        pygame.display.flip() # refreshes the screen ## Call this last ##

        dt = fps.tick(60) / 1000 # limit the framerate to 60 fps


        for event in pygame.event.get():  # allows you to click "X" to close game window
            if event.type == pygame.QUIT:
                return
            


if __name__ == "__main__": #executes code only from main.py
    main()