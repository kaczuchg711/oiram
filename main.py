import pygame

import constants
from models.Characters.Mob import Mob
from models.Level.Level import Level
from models.Level.Level_01 import Level_01
from models.Level.Level_02 import Level_02

from models.Characters.Oriam import Oriam


def main():
    pygame.init()
    
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("ORIAM: " + str(constants.score))

    player = Oriam()

    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height - 128
    active_sprite_list.add(player)


    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            player.move_character_depend_on_key(event)

        # Update the player.
        active_sprite_list.update()
        
        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world_x(-diff)
        # self.rect.colliderect(sprite.rect)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world_x(diff)


        # If the player gets near the top, shift the world down (-y)
        tmp = 64
        if player.rect.top <= tmp:
            diff = player.rect.top - tmp
            player.rect.top = tmp
            current_level.shift_world_y(-diff)
        # self.rect.colliderect(sprite.rect)

        # If the player gets near the bottom, shift the world up (+y)
        tmp = constants.SCREEN_HEIGHT - 128
        if player.rect.bottom >= tmp:
            diff = tmp - player.rect.bottom
            player.rect.bottom = tmp
            current_level.shift_world_y(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift_x
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
               current_level_no += 1
               current_level = level_list[current_level_no]
               player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)
        pygame.display.set_caption("OIRAM: " + str(constants.score))
        # Go ahead and update the screen with what we've drawn.
        
        screen.blit(pygame.transform.flip(screen, True, False), (0, 0))

        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
