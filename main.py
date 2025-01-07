# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    pygame.display.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    Player.containers = (drawable,updateable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        for sprite in updateable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60)/1000





if __name__ == "__main__":
    main()