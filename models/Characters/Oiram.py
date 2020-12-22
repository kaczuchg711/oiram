from models.Characters.Character import Character


class Oiram(Character):

    def __init__(self, image, clock):
        super().__init__(image, clock)
        self.isJumping = False
        self._isFalling = False
        self._jumpCount = 0

        # Todo
        self.corToFall = None

    def jump(self):
        self.isJumping = True
        if not self._isFalling:
            self._jumpCount += 1
            self.move("UP")
        if self._jumpCount == 50 or self._isFalling:
            self._isFalling = True
            self.move("DOWN")
            self._jumpCount -= 1
            if self._jumpCount == 0:
                self.isJumping = False
                self._isFalling = False