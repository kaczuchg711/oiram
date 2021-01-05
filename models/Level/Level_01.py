import pygame
 
import constants
from models.Level import platforms
from models.Level.Level import Level
from models.Characters.Mob import Mob

class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("static/img/world1_1.png").convert()
        self.background2 = pygame.image.load("static/img/world1_2.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.background2.set_colorkey(constants.BLUE)
        self.level_limit = -100 * 64
 
        # Array with type of platform, and x, y location of the platform.
        bricks = [[platforms.BRICK2,20, 6],
                [platforms.BRICK2,22, 6],
                [platforms.BRICK2,24,6],
                ]

        for platform in bricks:
            block = platforms.DestroPlatform(platform[0])
            block.rect.x = platform[1]*64
            block.rect.y = constants.SCREEN_HEIGHT - (platform[2]*64)
            block.player = self.player
            self.platform_list.add(block)


        question_blocks = [[platforms.QUESTION,16, 6],
                          [platforms.QUESTION,21, 6],
                           [platforms.QUESTION,22, 10],
                           [platforms.QUESTION,23, 6],]

        for platform in question_blocks:
            block = platforms.QuestionPlatform(platform[0])
            block.rect.x = platform[1]*64
            block.rect.y = constants.SCREEN_HEIGHT - (platform[2]*64)
            block.player = self.player
            self.platform_list.add(block)

        floor = [[platforms.PIPE_TOP_LEFT,28, 4],
                [platforms.PIPE_TOP_RIGHT,29,4],
                [platforms.PIPE_LEFT,28, 3],
                [platforms.PIPE_RIGHT,29,3],
                [platforms.PIPE_TOP_LEFT,38, 5],
                [platforms.PIPE_TOP_RIGHT,39,5],
                [platforms.PIPE_LEFT,38, 4],
                [platforms.PIPE_RIGHT,39,4],
                [platforms.PIPE_LEFT,38, 3],
                [platforms.PIPE_RIGHT,39,3],]
                
        for x in range(112):
            if x in [69, 70, 86,87,88]:
                continue
            floor.append([platforms.BRICK1, x, 2])
            floor.append([platforms.BRICK1, x, 1])
 
        # Go through the array above and add platforms
        for platform in floor:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]*64
            block.rect.y = constants.SCREEN_HEIGHT - (platform[2]*64)
            block.player = self.player
            self.platform_list.add(block)
 
        # # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.BRICK3)
        block.rect.x = 45 * 64
        block.rect.y = constants.SCREEN_HEIGHT - 5 * 64
        block.boundary_left = 45 * 64
        block.boundary_right = 50 * 64
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.BRICK3)
        block.rect.x = 55 * 64
        block.rect.y = constants.SCREEN_HEIGHT - 4 * 64
        block.boundary_bottom = constants.SCREEN_HEIGHT - 3 * 64
        block.boundary_top = constants.SCREEN_HEIGHT - 8 * 64
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

             # # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.BRICK3)
        block.rect.x = 61 * 64
        block.rect.y = constants.SCREEN_HEIGHT - 4 * 64
        block.boundary_bottom = constants.SCREEN_HEIGHT - 3 * 64
        block.boundary_top = constants.SCREEN_HEIGHT - 8 * 64
        block.change_y = 1
        block.boundary_left = 60 * 64
        block.boundary_right = 65 * 64
        block.change_x = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

     
        mob = Mob(player)
        mob.level = self
        mob.rect.x = 10*64
        mob.rect.y = 5*64
        self.enemy_list.add(mob)
        mob = Mob(player)
        mob.level = self
        mob.rect.x = 12*64
        mob.rect.y = 5*64
        self.enemy_list.add(mob)