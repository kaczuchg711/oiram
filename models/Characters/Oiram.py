import pygame
from os import listdir
from os.path import isfile, join
from models.Characters.Character import Character


class Oiram(Character):

    def __init__(self, clock,path_to_images_directory):
        super().__init__(clock)
        self.load_images(path_to_images_directory)
        self._jumpCount = 0

    def jump(self):
        self.isJumping = True
        if not self._isFalling:
            self._jumpCount += self.move("UP") + self.move("UP")
        if self._jumpCount >= 180 or self._isFalling:
            self._isFalling = True
            self._jumpCount -= self.move("DOWN")
            if self._jumpCount <= 0:
                self.isJumping = False
                self._isFalling = False

    def load_images(self,path_to_images_directory):
        # "static/img/oiram"
        # pygame.image.load()

        files_images = [f for f in listdir(path_to_images_directory) if isfile(join(path_to_images_directory, f))]
        marioImages = [pygame.image.load(path_to_images_directory + "/" + file) for file in files_images]
        marioTransformedImages = [pygame.transform.scale(img, (int(500 / 5), int(300 / 5))) for img in marioImages]

        self.images = {
            "run1": marioTransformedImages[0],
            "jump1": marioTransformedImages[1],
            "fall2": marioTransformedImages[2],
            "fall1": marioTransformedImages[3],
            "swap": marioTransformedImages[4],
            "stay": marioTransformedImages[5],
            "run3": marioTransformedImages[6],
            "run2": marioTransformedImages[7]
        }

    def draw(self, screen):
        cor = (self.coordinates.x, self.coordinates.y)
        if not self.isJumping and self.last_direction == "RIGHT":
            screen.blit(self.images["stay"], cor)
