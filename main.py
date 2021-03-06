# Game of life

# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which
# is in one of two possible states, alive or dead, (or populated and unpopulated, respectively).

# Rules
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
DARK = (47, 50, 57)

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
        state = random.randint(1, 15)
        grid[row].append(0 if state != 1 else 1)


def is_living(cell):
    return cell == 1


def check_bounds(grid, val):
    if val == -1:
        return len(grid) - 1
    if val == len(grid):
        return 0
    return val


def is_alive_at(grid, row, column):
    row = check_bounds(grid, row)
    column = check_bounds(grid, column)
    return is_living(grid[row][column])


def count_neighbors(grid, row, column):
    neighbors = 0

    # sides
    if is_alive_at(grid, row, column + 1):
        neighbors += 1
    if is_alive_at(grid, row, column - 1):
        neighbors += 1

    # top, down
    if is_alive_at(grid, row + 1, column):
        neighbors += 1
    if is_alive_at(grid, row - 1, column):
        neighbors += 1

    # diagonal
    if is_alive_at(grid, row + 1, column + 1):
        neighbors += 1
    if is_alive_at(grid, row - 1, column - 1):
        neighbors += 1

    # other diagonal
    if is_alive_at(grid, row - 1, column + 1):
        neighbors += 1
    if is_alive_at(grid, row + 1, column - 1):
        neighbors += 1

    return neighbors


def kill(grid, row, column):
    grid[row][column] = 0


def revive(grid, row, column):
    grid[row][column] = 1


def run_this():
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

                neighbors = count_neighbors(grid, row, column)
                import pudb
                pu.db
                # Update game state here:
                if is_living(grid[row][column]):
                    if neighbors < 2 or neighbors > 3:
                        # A living cell dies if it has fewer than two living neighboring cells.
                        # A living cell with more than three living neighboring cells dies in the next time step.
                        kill(grid, row, column)
                    elif neighbors == 2 or neighbors == 3:
                        # A living cell with two or three living neighbors lives on.
                        pass
                elif not is_living(grid[row][column]):
                    if neighbors == 3:
                        # A dead cell is revived if it has exactly three living neighboring cells.
                        revive(grid, row, column)

                color = GREEN if is_living(grid[row][column]) else DARK

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


if __name__ == '__main__':
    run_this()
