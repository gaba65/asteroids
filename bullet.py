import pygame
from constants import *
from circleshape import CircleShape

class Shot (CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
