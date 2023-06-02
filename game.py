# Minesweeper game using the Pygame library

import pygame, sys

# Initialization
pygame.init()
screen = pygame.display.set_mode((350,500)) # Set window resolution
clock = pygame.time.Clock()
framerate = 60 # frames, target framerate
#----------------------------------------------------------------------

running = True

while running:
    deltaTime = clock.tick(framerate)
    
    # Getting input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Refresh display
        pygame.display.flip()