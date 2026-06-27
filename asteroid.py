from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius) 
        
    def draw(self, screen: pygame.Surface):
         return  pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        first_asteroid_velocity = self.velocity.rotate(random_angle)
        secound_asteroid_velocity  = self.velocity.rotate(-random_angle)
        new_radius =  self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_one.velocity = first_asteroid_velocity * 1.2
        asteroid_two.velocity = secound_asteroid_velocity * 1.2
        