import sys, pygame
from time import sleep

from pygame.time import Clock

from controlers.CharacterMoveController import CharacterMoveController
from models.Characters.Oiram import Oiram

pygame.init()

size = width, height = 500, 300
color = 0, 0, 0

screen = pygame.display.set_mode(size)

mario = pygame.image.load("static/img/oiram/oiram_stay.png")

ballrect = mario.get_rect()

clock = Clock()

oiram = Oiram(clock, "static/img/oiram")
oiramMoveController = CharacterMoveController(oiram)

while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keyboardState = pygame.key.get_pressed()
    oiramMoveController.move_character_depend_on_key(keyboardState)

    screen.fill(color)
    oiram.draw(screen)
    pygame.display.flip()
    # pygame.time.delay(10)
