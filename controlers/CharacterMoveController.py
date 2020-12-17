import sys

import pygame
from pygame.draw_py import Point

from models import Characters


class CharacterMoveController:

    def __init__(self, character):
        self.character = character
        self.button_is_down = {"w": False, "s": False, "a": False, "d": False}

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.button_is_down["w"] = True
            if event.key == pygame.K_s:
                self.button_is_down["s"] = True
            if event.key == pygame.K_a:
                self.button_is_down["a"] = True
            if event.key == pygame.K_d:
                self.button_is_down["d"] = True

        if self.button_is_down["w"]:
            self.character.coordinates = Point(self.character.coordinates.x, self.character.coordinates.y - 1)

        if self.button_is_down["s"]:
            self.character.coordinates = Point(self.character.coordinates.x, self.character.coordinates.y + 1)

        if self.button_is_down["a"]:
            self.character.coordinates = Point(self.character.coordinates.x - 1, self.character.coordinates.y)

        if self.button_is_down["d"]:
            self.character.coordinates = Point(self.character.coordinates.x + 1, self.character.coordinates.y)

        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            self.button_is_down["w"] = False

        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            self.button_is_down["s"] = False

        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            self.button_is_down["a"] = False

        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            self.button_is_down["d"] = False
