import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            a = random.uniform(20 , 50)
            first = self.velocity.rotate(a)
            second = self.velocity.rotate(-a)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            Asteroid_1 = Asteroid(self.position.x,self.position.y, new_radius)
            Asteroid_2 = Asteroid(self.position.x,self.position.y, new_radius)

            Asteroid_1.velocity  = first * 1.2
            Asteroid_2.velocity = second
