import circleshape
import pygame
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            for i in range(0,2):
                daughter_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
                if i == 0:
                    daughter_asteroid.velocity = self.velocity.rotate(angle) * 1.2
                elif i == 1:
                    daughter_asteroid.velocity = self.velocity.rotate(-angle)  * 1.2
