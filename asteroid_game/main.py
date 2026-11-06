import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0.0


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Groups creations
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    players = Player(x= SCREEN_WIDTH/2, y= SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for draws in drawable:
            draws.draw(screen)

        updatable.update(dt)

        for item in asteroid:
            if item.collides_with(players) == False:
                log_event("player_hit")
                print("Game Over!")
                sys.exit("")

        for item in asteroid:
            for shoot in shots:
                if shoot.collides_with(item) == False :
                    log_event("asteroid_shot")
                    shoot.kill()
                    item.split()

        players.shoot_timer -= dt
        pygame.display.flip()
        dt = Clock.tick(60) / 1000




if __name__ == "__main__":
    main()
