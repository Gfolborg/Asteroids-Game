import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"  # Suppresses the message
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() # initializes pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = (updatable)

    shot = pygame.sprite.Group()
    Shot.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()



    while True:
        #This is what starts the window/screen and gives it is size and color (pygame.Surface.fill(screen, "black") did thing
        screen.fill("black") 

        
        updatable.update(dt)

        for obj in asteroids_group:
            if obj.collision(player):
                print("Game Over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip() # refreshes the screen ## Call this last ##

        dt = fps.tick(60) / 1000 # limit the framerate to 60 fps


        for event in pygame.event.get():  # allows you to click "X" to close game window
            if event.type == pygame.QUIT:
                return




if __name__ == "__main__": #executes code only from main.py
    main()