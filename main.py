import sys, pygame
from time import sleep

from pygame.time import Clock

from controlers.CharacterMoveController import CharacterMoveController
from models.Characters.Oiram import Oiram

pygame.init()

size = width, height = 320, 240
color = 0, 0, 0

screen = pygame.display.set_mode(size)

mario = pygame.image.load("static/img/oiram_stay.png")
marioImage = pygame.transform.scale(mario, (int(width/5), int(height/5)))
ballrect = mario.get_rect()


clock = Clock()

oiram = Oiram(marioImage,clock)
oiramMoveController = CharacterMoveController(oiram)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keyboardState = pygame.key.get_pressed()
    oiramMoveController.move_character_depend_on_key(keyboardState)


    print(oiram._jumpCount)
    screen.fill(color)
    screen.blit(oiram.images["go"], (oiram.coordinates.x, oiram.coordinates.y))
    pygame.display.flip()
    pygame.time.delay(10)
