from models.Characters.Character import Character


class Oiram(Character):

    def __init__(self, image, clock):
        super().__init__(image, clock)
        self.isJumping = False
        self._isFalling = False
        self._jumpCount = 0

        self.corToFall = None

    def jump(self):
        self.isJumping = True
        if not self._isFalling:
            self._jumpCount += self.move("UP")
        if self._jumpCount >= 180 or self._isFalling:
            self._isFalling = True
            self._jumpCount -= self.move("DOWN")
            if self._jumpCount <= 0:
                self.isJumping = False
                self._isFalling = False