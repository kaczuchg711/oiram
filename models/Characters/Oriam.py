"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants

from models.Level.platforms import MovingPlatform, DestroPlatform, QuestionPlatform
from models.spritesheet_functions import SpriteSheet


class Oriam(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.standing_frames_l = []
        self.standing_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet("static/img/oiram/OIRAM_walk2.png")
        
        image = sprite_sheet.get_image(517, 31, 62, 128)
        self.standing_frames_r.append(image)

        image = sprite_sheet.get_image(129, 31, 62, 128)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(226, 31, 62, 128)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(32, 31, 62, 128)
        self.walking_frames_r.append(image)
        
        

        for image_to_rotate in self.walking_frames_r:
            image_to_rotate = pygame.transform.flip(image_to_rotate.copy(), True, False)
            self.walking_frames_l.append(image_to_rotate)

        

        for image_to_rotate in self.standing_frames_r:
            image_to_rotate = pygame.transform.flip(image_to_rotate.copy(), True, False)
            self.standing_frames_l.append(image_to_rotate)    
    

        # Set the image the player starts with
        self.image = self.standing_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def move_character_depend_on_key(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.go_left()
            if event.key == pygame.K_LEFT:
                self.go_right()
            if event.key == pygame.K_UP:
                self.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and self.change_x < 0:
                self.stop()
            if event.key == pygame.K_LEFT and self.change_x > 0:
                self.stop()

    def _is_under_block(self, block):
        return block.rect.centerx - block.rect.width / 2 < self.rect.centerx < block.rect.centerx + block.rect.width / 2 and self.rect.y - block.rect.y + block.rect.height > 0

    def _is_close_under(self, block):
        return self.rect.y - (block.rect.y + block.rect.height) < 1

    def _check_fatal_fall(self):
        if self.level.world_shift_y < -200:
            exit(0)

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift_x
        if self.direction == "R":
            if self.change_x == 0:
                frame = (pos // 60) % len(self.standing_frames_r)
                self.image = self.standing_frames_r[frame]
            else:
                frame = (pos // 60) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
        else:
            if self.change_x == 0:
                frame = (pos // 60) % len(self.standing_frames_l)
                self.image = self.standing_frames_l[frame]
            else:
                frame = (pos // 60) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]

        self._check_fatal_fall()

        blocks = self.level.platform_list
        for block in blocks:
            if self._is_close_under(block) and self._is_under_block(block) :
                if isinstance(block, DestroPlatform):
                    block.kill()
                    constants.score += 1
                if isinstance(block, QuestionPlatform):
                    block.hit_count_up()




        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        # if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
        #    self.change_y = 0
        #    self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -14

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -4
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 4
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
