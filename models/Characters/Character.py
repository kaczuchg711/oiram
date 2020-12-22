import pygame
from pygame.draw_py import Point



class Character:
    id = 0

    def __init__(self, image, clock):
        self.id = self.id + 1
        self.coordinates = Point(0, 215)
        self.images = {"go": image}
        self.clock = clock
        self.last_direction = None

    def move(self, direction: str):
        direction = direction.upper()
        dx = self.clock.tick(60) / 10

        if dx > 2:
            dx = 2

        if self.last_direction == "UP" or self.last_direction == "Down":
            dx *= 2

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
