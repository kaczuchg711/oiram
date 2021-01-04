import pygame

from models.spritesheet_functions import SpriteSheet

class Mob(pygame.sprite.Sprite):

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

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet("static/img/mob1.png")
        image = sprite_sheet.get_image(0, 0, 32, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(32, 0, 32, 32)
        self.walking_frames_r.append(image)

        for image_to_rotate in self.walking_frames_r:
            image_to_rotate = pygame.transform.flip(image_to_rotate.copy(), True, False)
            self.walking_frames_l.append(image_to_rotate)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()