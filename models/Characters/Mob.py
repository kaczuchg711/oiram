import pygame

from models.spritesheet_functions import SpriteSheet
from models.Level.platforms import MovingPlatform
import constants

class Mob(pygame.sprite.Sprite):

    def __init__(self, player):
        """ Constructor function """
        self.player = player
        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        # Set speed vector of player
           # -- Attributes
        # Set speed vector of player
        self.delta_y = 0
        self.delta_x = 1

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet("static/img/mob1.png")
        image = sprite_sheet.get_image(0, 0, 32, 32)
        self.walking_frames_r.append(pygame.transform.scale2x(image).convert_alpha())
        image = sprite_sheet.get_image(32, 0, 32, 32)
        self.walking_frames_r.append(pygame.transform.scale2x(image).convert_alpha())

        for image_to_rotate in self.walking_frames_r:
            image_to_rotate = pygame.transform.flip(image_to_rotate.copy(), True, False)
            self.walking_frames_l.append(image_to_rotate)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
          # Gravity
        self.calc_grav()
        

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            leg_height = self.player.rect.y + self.player.rect.height
            if self.player.rect.colliderect(self):
                if leg_height - 20 < self.rect.y:
                    self.kill()
                else:
                    self.player.kill()
                    exit(0)
        # Move left/right

        self.rect.x += self.delta_x
        
        pos = self.rect.x + self.level.world_shift_x
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.delta_x == 1:
                self.delta_x = -1
            else:
                self.delta_x = 1

         # Move up/down
        self.rect.y += self.delta_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.delta_y > 0:
                self.rect.bottom = block.rect.top
            elif self.delta_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.delta_y = 0
 
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.delta_y == 0:
            self.delta_y = 1
        else:
            self.delta_y += .35
 