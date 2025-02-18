import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"  # Suppresses the message
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init() # initializes pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroid = pygame.sprite.Group()
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()


    while True:
        #This is what starts the window/screen and gives it is size and color (pygame.Surface.fill(screen, "black") did thing
        screen.fill("black") 

        
        updatable.update(dt)

        


        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip() # refreshes the screen ## Call this last ##

        dt = fps.tick(60) / 1000 # limit the framerate to 60 fps


        for event in pygame.event.get():  # allows you to click "X" to close game window
            if event.type == pygame.QUIT:
                return




if __name__ == "__main__": #executes code only from main.py
    main()