import pygame
from pygame.draw_py import Point



class Character:
    id = 0

    def __init__(self, clock):
        self.coordinates = Point(0, 190)
        self.last_coordinates = None
        self.images = None
        self.clock = clock
        self.last_direction = None
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
            self.last_direction = "UP"
            self.coordinates = Point(self.coordinates.x, self.coordinates.y - dx)
        elif direction == "DOWN":
            self.last_direction = "DOWN"
            self.coordinates = Point(self.coordinates.x, self.coordinates.y + dx)
        elif direction == "LEFT":
            self.last_direction = "LEFT"
            self.coordinates = Point(self.coordinates.x - dx, self.coordinates.y)
        elif direction == "RIGHT":
            self.last_direction = "RIGHT"
            self.coordinates = Point(self.coordinates.x + dx, self.coordinates.y)
        else:
            raise ValueError

        return dx
