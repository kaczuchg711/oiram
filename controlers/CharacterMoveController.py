import sys

import pygame
from pygame.draw_py import Point

from models.Characters.Character import Character


class CharacterMoveController:

    def __init__(self, character:Character):
        self.character = character

    def move_character_depend_on_key(self,keyIsPressed):
        if keyIsPressed[pygame.K_w]:
            self.character.move("UP")
        elif keyIsPressed[pygame.K_s]:
            self.character.move("DOWN")

        if keyIsPressed[pygame.K_a]:
            self.character.move("LEFT")
        elif keyIsPressed[pygame.K_d]:
            self.character.move("RIGHT")

    def _check_that_keys_are_pressed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.button_is_down["w"] = True
            elif event.key == pygame.K_s:
                self.button_is_down["s"] = True
            if event.key == pygame.K_a:
                self.button_is_down["a"] = True
            elif event.key == pygame.K_d:
                self.button_is_down["d"] = True

    def _check_that_keys_are_not_pressed(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.button_is_down["w"] = False

            if event.key == pygame.K_s:
                self.button_is_down["s"] = False

            if event.key == pygame.K_a:
                self.button_is_down["a"] = False

            if event.key == pygame.K_d:
                self.button_is_down["d"] = False

