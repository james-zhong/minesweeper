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
generated = False
max_bombs = 20
no_of_bombs = 0
bomb_coords = []

def generate():
    # Place squares
    global generated
    
    newSqr = square()
    coordinates = [(j*50, i*50) for i in range(10) for j in range(10)]

    bomb_coords = random.choices(coordinates, k=max_bombs)
    
    if not generated:
        generated = True
        for coord in coordinates:
            if coord in bomb_coords:
                newSqr.place(*coord, (255, 0, 0))
            else:
                newSqr.place(*coord, (255, 255, 255))

while running:
    deltaTime = clock.tick(framerate)
    
    # Getting input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    generate()

    # Refresh display
    pygame.display.flip()