import pygame

from models.spritesheet_functions import SpriteSheet

class Mob(pygame.sprite.Sprite):

    def __init__(self,player):
        """ Constructor function """
        self.player = player
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
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            leg_height = self.player.rect.y + self.player.height
            if self.player.rect.colliderect(self):
                if leg_height - 10 < self.rect.y:
                    self.kill()
                else:
                    self.player.kill()
                    exit(0)



