import pygame
from circleshape import CircleShape
from constants import *
from bullet import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.shoot_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, PLAYER_SPEED, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            pass
        else:
            Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation)
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()
        inversed_dt = 0 - dt
        if keys[pygame.K_a]:
            self.rotate(inversed_dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(PLAYER_SPEED, dt)
        if keys[pygame.K_s]:
            self.move(PLAYER_SPEED, inversed_dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shoot_timer -= dt

    def collision(self, circle):
        super().collision(circle)