import pygame
 
import constants
from models.Level import platforms
from models.Level.Level import Level

class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("static/img/background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
 
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.BRICK1, 500, 500],
                  [platforms.BRICK1, 570, 500],
                  [platforms.BRICK1, 640, 500],
                  [platforms.BRICK1, 800, 400],
                  [platforms.BRICK1, 870, 400],
                  [platforms.BRICK1, 940, 400],
                  [platforms.BRICK1, 1000, 500],
                  [platforms.BRICK1, 1070, 500],
                  [platforms.BRICK1, 1140, 500],
                  [platforms.BRICK1, 1120, 280],
                  [platforms.BRICK1, 1190, 280],
                  [platforms.BRICK1, 1260, 280],
                  ]
 
 
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
 
        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
 