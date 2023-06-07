# Minesweeper game using the Pygame library

import pygame, sys, random
from timeit import default_timer as timer

# Initialization
pygame.init()
screen = pygame.display.set_mode((500,550)) # Set window resolution
#----------------------------------------------------------------------
# Classes
class square:
    def __init__(self):
        self.width = 49 #px
        self.height = 49 #px
    
    # Draw square on cube
    def place(self, x, y, colour):
        pygame.draw.rect(screen, colour, pygame.Rect(x, y, self.width, self.height))
#----------------------------------------------------------------------

running = True
mine_num_text = pygame.font.Font("assets/fonts/LeagueSpartan-ExtraBold.ttf", 24)
instruction_text = pygame.font.Font("assets/fonts/LeagueSpartan-ExtraBold.ttf", 16)
mine_img = pygame.image.load("assets/images/mine.png")
generated = False
get_time = False
max_bombs = 20
no_of_bombs = 0
bomb_coords = []
rows = 10
columns = 10
time_taken = 0 # In seconds

coordinates = [(j*50, i*50) for i in range(rows) for j in range(columns)]
mine_coords = random.sample(coordinates, max_bombs)

def generate():
    # Place squares
    global generated, coordinates, mine_coords, time_taken, get_time

    time_begun = timer()
    newSqr = square()
    coordinates = [(j*50, i*50) for i in range(rows) for j in range(columns)]
    
    if not generated:
        get_time = True
        generated = True
        mine_coords = random.sample(coordinates, max_bombs)
        
    for coord in coordinates:
        # Draw cells
        if coord not in mine_coords:
            newSqr.place(*coord, (100, 100, 100))
        else:
            newSqr.place(*coord, (255, 0 ,0))
            screen.blit(mine_img, coord)
        
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
            time_taken = timer() - time_begun
        
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