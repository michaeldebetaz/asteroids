import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white",
                           center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        x, y = self.position
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        if new_radius < ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        asteroid1 = Asteroid(x, y, new_radius)
        random_angle1 = self.velocity.rotate(random_angle) * 1.2
        asteroid1.velocity = random_angle1

        asteroid2 = Asteroid(x, y, new_radius)
        random_angle2 = self.velocity.rotate(-random_angle)
        asteroid2.velocity = random_angle2
