# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    my_clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # limit the fps to 60
        dt = my_clock.tick(60) / 1000

        for obj in updateable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen) 

        pygame.display.flip()
        
        

        

if __name__ == "__main__":
    main()