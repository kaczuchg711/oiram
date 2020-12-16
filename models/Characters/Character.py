from pygame.draw_py import Point


class Character:
    id = 0

    def __init__(self,image):
        self.id = self.id + 1
        self.coordinates = Point(0,0)
        self.images = {"go": image}
