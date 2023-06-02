# Minesweeper game using the Pygame library

import pygame, sys, random

# Initialization
pygame.init()
screen = pygame.display.set_mode((500,500)) # Set window resolution
clock = pygame.time.Clock()
framerate = 60 # frames, target framerate
#----------------------------------------------------------------------
# Classes
class square:
    def __init__(self):
        self.width = 50 #px
        self.height = 50 #px
    
    # Draw square on cube
    def place(self, x, y, colour):
        pygame.draw.rect(screen, colour, pygame.Rect(x, y, self.width, self.height))
#----------------------------------------------------------------------

running = True

while running:
    deltaTime = clock.tick(framerate)
    
    # Getting input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Placing squares
    
    newSqr = square()
    coordinates = [(j*50, i*50) for i in range(10) for j in range(10)]

    for coord in coordinates:
        newSqr.place(*coord, (150, 150, 150))

    # Refresh display
    pygame.display.flip()