import sys, pygame
from time import sleep

from controlers.CharacterMoveController import CharacterMoveController
from models.Characters.Oiram import Oiram

pygame.init()

size = width, height = 320, 240
color = 0, 0, 0

screen = pygame.display.set_mode(size)

mario = pygame.image.load("static/img/mario_jump.png")
marioImage = pygame.transform.scale(mario,(int(width/10),int(height/10)))
ballrect = mario.get_rect()



oiram = Oiram(marioImage)
oiramMoveController = CharacterMoveController(oiram)

clock = pygame.time.Clock()
dt = clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        oiramMoveController.check_event(event)

    screen.fill(color)
    screen.blit(oiram.images["go"], (oiram.coordinates.x, oiram.coordinates.y))
    pygame.display.flip()


