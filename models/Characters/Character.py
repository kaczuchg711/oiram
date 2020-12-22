import pygame
from pygame.draw_py import Point


class Character:
    id = 0

    def __init__(self, image, clock):
        self.id = self.id + 1
        self.coordinates = Point(0, 0)
        self.images = {"go": image}
        self.clock = clock

    def move(self, direction: str):
        # todo make
        dx = self.clock.tick(1000) / 10

        if direction == "UP":
            print( self.clock.get_rawtime())
            self.coordinates = Point(self.coordinates.x, self.coordinates.y - dx)

        if direction == "DOWN":
            self.coordinates = Point(self.coordinates.x, self.coordinates.y + dx)

        if direction == "LEFT":
            self.coordinates = Point(self.coordinates.x - dx, self.coordinates.y)

        if direction == "RIGHT":
            self.coordinates = Point(self.coordinates.x + dx, self.coordinates.y)
