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
    cell_coords = [cell for cell in coordinates if cell not in mine_coords]
    
    if not generated:
        generated = True
        for coord in coordinates:
            if coord not in mine_coords:
                newSqr.place(*coord, (100, 100, 100))
            else:
                newSqr.place(*coord, (255, 0 ,0))
            
            # Check how many mines are neighbouring the cells
            # Skip if is a bomb
            if coord in mine_coords:
                continue
            
            neighbouring_mines = 0
            x = coordinates.index(coord)
            
            # I really do not know how to do this better
            # Calculate the amount of neighbouring mines
            
            neighbours=[]
            
            # Corners
            if x == 0: # Cell in top left corner
                neighbours = [x+1, x+rows, (x+rows)+1]
            elif x == rows-1: # Cell in top right corner
                neighbours = [x-1, x+rows, (x+rows)-1]
            elif x == len(coordinates)-1: # Cell in bottom right corner
                neighbours == [x-1, x-rows, (x-rows)-1]
            elif x == len(coordinates)-rows+1: # Cell in bottom left corner
                neighbours = [x+1, x-rows, (x-rows)+1]
            # Sides
            elif x < rows: # Cell at top of grid
                neighbours = [x-1, x+1, x+rows, (x+rows)+1, (x+rows)-1] 
            elif x > len(coordinates)-rows-1: # cell at bottom of grid
                neighbours = [x+1, x-1, x-rows, (x-rows)-1, (x-rows)+1]
            elif x % rows == 0: # Cell at left side of grid    
                neighbours = [x+1, x-rows, x+rows, (x-rows)+1, (x+rows)+1]
            elif (x+1) % rows == 0: # Cell at right side of grid
                neighbours = [x-1, x-rows, x+rows, (x-rows)-1, (x+rows)-1]
            else: # Cell is not at a corner or side
                neighbours = [x+1, x-1, x-rows, x+rows, (x-rows)+1, (x-rows)-1, (x+rows)+1, (x+rows)-1]
                
            for n in neighbours:
                if coordinates[n] in mine_coords:
                    neighbouring_mines += 1
            
            # Leave cells without any neighbouring mines blank
            if neighbouring_mines == 0:
                continue
            
            numberText = text.render(str(neighbouring_mines), True, (0,0,0))
            screen.blit(numberText, cell_coords[cell_coords.index(coord)])

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