import pygame

from circleshape import CircleShape
from constants import (PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN,
                       PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED,
                       SHOT_RADIUS)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right_rotation = self.rotation + 90
        right = pygame.Vector2(0, 1).rotate(right_rotation) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(surface=screen, color="white",
                            points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        x, y = self.position
        shot = Shot(x, y, SHOT_RADIUS)
        angle = self.rotation
        shot.velocity = pygame.Vector2(0, 1).rotate(angle) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer -= dt
