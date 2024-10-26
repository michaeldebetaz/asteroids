import sys

import pygame
from pygame.sprite import Group

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (ASTEROID_KINDS, ASTEROID_MAX_RADIUS,
                       ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE, SCREEN_HEIGHT,
                       SCREEN_WIDTH)
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")

        for up in updatable:
            up.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.split()
                    shot.kill()

            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

        for dr in drawable:
            dr.draw(screen)

        pygame.display.flip()

        time_ms = clock.tick(60)
        time_s = time_ms / 1000
        dt = time_s


if __name__ == "__main__":
    main()
