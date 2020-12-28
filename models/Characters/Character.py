import pygame
from pygame.draw_py import Point

class Character:
    def __init__(self, clock):
        self.coordinates = Point(0, 190)
        self.last_coordinates = None
        self.images = None
        self.clock = clock
        self.lastHoriontalDirection = "RIGHT"
        self.isJumping = False
        self._isFalling = False


    def move(self, direction: str):
        direction = direction.upper()
        dx = self.clock.tick(60) / 10

        if dx > 2:
            dx = 2

        if (self.isJumping and direction == "RIGHT") or (self.isJumping and direction == "LEFT"):
            dx *= 3.2

        if direction == "UP":
            self.coordinates = Point(self.coordinates.x, self.coordinates.y - dx)
        elif direction == "DOWN":
            self.coordinates = Point(self.coordinates.x, self.coordinates.y + dx)
        elif direction == "LEFT":
            self.lastHoriontalDirection = "LEFT"
            self.coordinates = Point(self.coordinates.x - dx, self.coordinates.y)
        elif direction == "RIGHT":
            self.lastHoriontalDirection = "RIGHT"
            self.coordinates = Point(self.coordinates.x + dx, self.coordinates.y)
        else:
            raise ValueError

        return dx
