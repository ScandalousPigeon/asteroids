import pygame
import sys
from constants import *
from shot import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # group creation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for thing in updatable:
            thing.update(0.1)
            if isinstance(thing, Player):
                if thing.timer > 0:
                    thing.timer -= 0.1
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            ded = asteroid.check_collision(player)
            if ded:
                sys.exit("Game over!")
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
