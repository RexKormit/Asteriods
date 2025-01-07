import circleshape
import constants
import pygame
import numpy

class Player(circleshape.CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

   
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
        self.rotation += constants.PLAYER_TURN_SPEED * dt
    
    def move_forward(self, dt):
        #This is not how its done in the course.
        #They use a constant of PLAYER_SPEED to change the speed and .rotate
        #pygame Vector2's have a .rotate func built in as well
        theta = (self.rotation + 90) * (numpy.pi/180)
        accleration = pygame.Vector2((constants.PLAYER_ACCLERATION * dt) * numpy.cos(theta),(constants.PLAYER_ACCLERATION * dt) * numpy.sin(theta))
        self.velocity += accleration

        
    def report_situation(self):
        print("=======================================================")
        print(f"Rotation: {self.rotation}")
        print(f"Velocity: {self.velocity}")
        print(f"Position: {self.position}")

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.position += self.velocity

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move_forward(dt)
        if keys[pygame.K_r]:
            self.report_situation()