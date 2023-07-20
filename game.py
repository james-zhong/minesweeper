# Minesweeper game using the Pygame library

import pygame, sys, random
from timeit import default_timer as timer

# Initialization
pygame.init()
screen = pygame.display.set_mode((500,550)) # Set window resolution
#----------------------------------------------------------------------
# Variables
running = True
mine_num_text = pygame.font.Font("assets/fonts/LeagueSpartan-ExtraBold.ttf", 24)
instruction_text = pygame.font.Font("assets/fonts/LeagueSpartan-ExtraBold.ttf", 16)
generated = False
get_time = False
max_bombs = 20
no_of_bombs = 0
bomb_coords = []
rows = 10
columns = 10
time_taken = 0 # In seconds

coordinates = []
mine_coords = None
#----------------------------------------------------------------------
# Classes
class square:
    def __init__(self):
        # Dimensions are 1 pixel smaller to get a "border" effect
        self.width = (500/rows)-1 #px
        self.height = (500/rows)-1 #px
    
    # Draw square on cube
    def place(self, x, y, colour):
        pygame.draw.rect(screen, colour, pygame.Rect(x, y, self.width, self.height))
#----------------------------------------------------------------------
# Functions

def generate():
    # Place squares
    global generated, coordinates, max_bombs, mine_coords, time_taken, get_time

    time_begun = timer()
    newSqr = square()
    
    if not generated:
        get_time = True
        generated = True
        coordinates = [(j*(500/rows), i*(500/rows)) for i in range(rows) for j in range(columns)]
        
        # Prevent too many mines being placed with insuffiencient amount of cells, otherwise random.sample throws an error
        if max_bombs > rows*columns:
            max_bombs = rows*columns-1
        
        mine_coords = random.sample(coordinates, max_bombs)
        
    for coord in coordinates:
        # Draw cells
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
        # Cell is not at corner or side
        else:
            neighbours = [x+1, x-1, x-rows, x+rows, (x-rows)+1, (x-rows)-1, (x+rows)+1, (x+rows)-1]
            
        for n in neighbours:
            if coordinates[n] in mine_coords:
                neighbouring_mines += 1
        
        # Leave cells without any neighbouring mines blank
        if neighbouring_mines == 0:
            continue
        
        numberText = mine_num_text.render(str(neighbouring_mines), True, (0,0,0))
        # Center the text on cells
        xPos = coordinates[x][0] + newSqr.width / 2
        yPos = coordinates[x][1] + newSqr.height / 2
        # Display text number on cells
        screen.blit(numberText, numberText.get_rect(center=(xPos, yPos)))
        
        if get_time:
            get_time = False
            time_taken = round(timer() - time_begun, 10)
        
def instructions():
    generateText = instruction_text.render("Press 'Space' to generate", True, (255,255,255))
    screen.blit(generateText, (10, 505))
    
    timeTaken = instruction_text.render(f"Time taken: {time_taken}s", True, (255,255,255))
    screen.blit(timeTaken, (10, 525))
    
while running:
    # Getting input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                generated = False
    
    # Display
    screen.fill((0,0,0))
    
    generate()
    instructions()

    # Refresh display
    pygame.display.flip()