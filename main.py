# Game of life

# Rules
#
# The simulation starts in the first time step with a specified initial state.
# Each cell in the game has one of two states: "Alive" or "Dead". In the Python example,
# these states are expressed by the numbers 0 and 1. For the next time step, the states of the cells
# are calculated according to the following rules:
#
# A living cell dies if it has fewer than two living neighboring cells.
# A living cell with two or three living neighbors lives on.
# A living cell with more than three living neighboring cells dies in the next time step.
# A dead cell is revived if it has exactly three living neighboring cells.


import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (81, 155, 80)
RED = (255, 0, 0)

BACK_GROUND = (41, 42, 48)
GRID_LINES = (47, 50, 57)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 7
HEIGHT = 7

MAX_ROWS = 100

# This sets the margin between each cell
MARGIN = 1

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800, 800]

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(MAX_ROWS):
    grid.append([])
    for column in range(MAX_ROWS):
        state = random.randint(1, 10)
        grid[row].append(0 if state is not 1 else 1)


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
# Set the screen background
screen.fill(BACK_GROUND)
# Set title of screen
pygame.display.set_caption("Game of Life")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            # grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)



    # Draw the grid
    for row in range(MAX_ROWS):
        for column in range(MAX_ROWS):

            color = GRID_LINES
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
