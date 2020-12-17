import sys

import pygame
from pygame.draw_py import Point

from models import Characters


class CharacterMoveController:

    def __init__(self, character):
        self.character = character
        self.button_is_down = {"w": False, "s": False, "a": False, "d": False}

    def check_event(self, event):

        self._check_that_keys_are_pressed(event)

        self._move_character_depend_on_key()

        self._check_that_keys_are_not_pressed(event)

    def _move_character_depend_on_key(self):
        if self.button_is_down["w"]:
            self.character.move("UP")

        if self.button_is_down["s"]:
            self.character.move("DOWN")

        if self.button_is_down["a"]:
            self.character.move("LEFT")

        if self.button_is_down["d"]:
            self.character.move("RIGHT")

    def _check_that_keys_are_pressed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.button_is_down["w"] = True
            if event.key == pygame.K_s:
                self.button_is_down["s"] = True
            if event.key == pygame.K_a:
                self.button_is_down["a"] = True
            if event.key == pygame.K_d:
                self.button_is_down["d"] = True

    def _check_that_keys_are_not_pressed(self, event):
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            self.button_is_down["w"] = False

        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            self.button_is_down["s"] = False

        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            self.button_is_down["a"] = False

        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            self.button_is_down["d"] = False

