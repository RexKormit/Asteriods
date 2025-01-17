# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def draw_text(text, font, text_col, x, y, scrn):
    img = font.render(text, True, text_col)
    scrn.blit(img, (x, y))

def main():
    pygame.init()
    pygame.display.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    text_font = pygame.font.Font(None, 30)

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)
    Shot.containers = (bullets, drawable, updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        screen.blit(pygame.font.Font.render(text_font,f"Score: {player.get_score()}",True,(255,255,255)),(50,50))

        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game Over!")
                print(f"Final score: {player.get_score()}")
                exit()

            for bullet in bullets:
                if asteroid.check_collisions(bullet):
                    asteroid.split()
                    bullet.kill()
                    player.increase_score()

            
        pygame.display.flip()
        
        dt = clock.tick(60)/1000





if __name__ == "__main__":
    main()