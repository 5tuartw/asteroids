# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    my_clock = pygame.time.Clock()
    dt = 0

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # limit the fps to 60
        dt = my_clock.tick(60) / 1000

        for obj in updateable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.collision_detect(player):
                sys.exit("Game over!")

        for obj1 in asteroids:
            for obj2 in shots:
                if obj1.collision_detect(obj2):
                    obj1.split()
                    obj2.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen) 

        pygame.display.flip()
        
        

        

if __name__ == "__main__":
    main()