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
text = pygame.font.Font("assets/fonts/LeagueSpartan-ExtraBold.ttf", 12)
generated = False
max_bombs = 20
no_of_bombs = 0
bomb_coords = []
rows = 10
columns = 10

def generate():
    # Place squares
    global generated
    
    newSqr = square()
    coordinates = [(j*50, i*50) for i in range(rows) for j in range(columns)]

    mine_coords = random.sample(coordinates, max_bombs)
    cell_coords = [coord for coord in coordinates if coord not in mine_coords]
    
    if not generated:
        generated = True
        for coord in coordinates:
            if coord in mine_coords:
                newSqr.place(*coord, (255, 0, 0))
            else:
                newSqr.place(*coord, (255, 255, 255))
            
        for cell in cell_coords:
            numberText = text.render(str(coordinates.index(cell)), True, (0,0,0))
            screen.blit(numberText, cell_coords[cell_coords.index(cell)])

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