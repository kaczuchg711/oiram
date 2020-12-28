import sys

import pygame
from pygame.draw_py import Point

from models.Characters.Character import Character
from models.Characters.Oiram import Oiram


class CharacterMoveController:

    def __init__(self, character: Oiram):
        self.character = character

    def move_character_depend_on_key(self, keyIsPressed):
        if keyIsPressed[pygame.K_a]:
            self.character.move("LEFT")
        elif keyIsPressed[pygame.K_d]:
            self.character.move("RIGHT")

        if keyIsPressed[pygame.K_SPACE] or self.character.isJumping:
            self.character.jump()
