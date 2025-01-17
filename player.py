import circleshape
from constants import *
import pygame
import numpy

class Player(circleshape.CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.dash_timer = 0
        self.__score = 0
       
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move_forward(self, dt):
        #This is not how its done in the course.
        #They use a constant of PLAYER_SPEED to change the speed and .rotate
        #pygame Vector2's have a .rotate func built in as well
        #theta = (self.rotation + 90) * (numpy.pi/180)
        #accleration = pygame.Vector2((PLAYER_ACCLERATION * dt) * numpy.cos(theta),(PLAYER_ACCLERATION * dt) * numpy.sin(theta))
        #self.velocity += accleration

        dst = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SPEED * dt
        self.position += dst

    def shoot(self,dt):
        
        if self.shoot_timer <= 0:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    
    def increase_score(self):
        self.__score += 1

    def get_score(self):
        return self.__score
    
    def dash(self, dt):
        if self.dash_timer <= 0:
            self.dash_timer = PLAYER_DASH_COOLDOWN
            dst = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SPEED * dt * 10
            self.position += dst

    def report_situation(self):
        print("=======================================================")
        print(f"Rotation: {self.rotation}")
        print(f"Velocity: {self.velocity}")
        print(f"Position: {self.position}")

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt
        self.dash_timer -= dt
        #self.position += self.velocity

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move_forward(dt)
        if keys[pygame.K_r]:
            self.report_situation()
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        if keys[pygame.K_e]:
            self.dash(dt)

class Shot(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt