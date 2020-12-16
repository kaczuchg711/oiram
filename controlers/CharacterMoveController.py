import sys

import pygame
from pygame.draw_py import Point

from models import Characters


class CharacterMoveController:

    def __init__(self, character):
        self.character = character
        self.button_is_down = False

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.button_is_down = True

        if self.button_is_down:
            self.character.coordinates = Point(self.character.coordinates.x + 1,self.character.coordinates.y)

        if event.type == pygame.KEYUP:
            self.button_is_down = False
