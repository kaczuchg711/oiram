from pygame.draw_py import Point


class Character:
    id = 0

    def __init__(self, image):
        self.id = self.id + 1
        self.coordinates = Point(0, 0)
        self.images = {"go": image}

    def move(self, direction: str):
        if direction == "UP":
            self.coordinates = Point(self.coordinates.x, self.coordinates.y - 1)

        if direction == "DOWN":
            self.coordinates = Point(self.coordinates.x, self.coordinates.y + 1)

        if direction == "LEFT":
            self.coordinates = Point(self.coordinates.x - 1, self.coordinates.y)

        if direction == "RIGHT":
            self.coordinates = Point(self.coordinates.x + 1, self.coordinates.y)
