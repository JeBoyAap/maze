import pygame, time
import cell
import generator

#config
DELAY_FRAMES = True
MAX_FPS = 1 #max fps

USE_SEED = False
SEED = 2

STARTING_POS = (1,1)

CELL_PIXEL_SIZE = 5

FULLSCREEN = False

if FULLSCREEN:
    X_CELLS = 1920 // CELL_PIXEL_SIZE
    Y_CELLS = 1080 // CELL_PIXEL_SIZE
else:
    X_CELLS = 50
    Y_CELLS = 50



# pygame setup
pygame.init()

#make grid_size uneven
GRID_SIZE_X = int(X_CELLS)
if GRID_SIZE_X % 2 == 0:
    GRID_SIZE_X -= 1
GRID_SIZE_Y = int(Y_CELLS)
if GRID_SIZE_Y % 2 == 0:
    GRID_SIZE_Y -= 1

#calculate screen dimensions
if FULLSCREEN:
    SCREEN_HEIGHT = 1080
    SCREEN_WIDTH = 1920
else:
    SCREEN_HEIGHT = CELL_PIXEL_SIZE * GRID_SIZE_Y
    SCREEN_WIDTH = CELL_PIXEL_SIZE * GRID_SIZE_X

generator.init_maze(GRID_SIZE_X, GRID_SIZE_Y, USE_SEED, SEED)


if FULLSCREEN:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

cell_width = int(SCREEN_WIDTH / GRID_SIZE_X)
cell_height = int(SCREEN_HEIGHT / GRID_SIZE_Y)


#set al cells to walls
maze = [[1 for _ in range(GRID_SIZE_X)] for _ in range(GRID_SIZE_Y)]

#create entrance and exit
maze[0][1] = 0
maze[GRID_SIZE_Y - 1][GRID_SIZE_X - 2] = 0


#all cels in a dict for quick lookup using (x, y) position
cells = {}
for y, row in enumerate(maze):
    for x, value in enumerate(row):
        x_cor = x * cell_width
        y_cor = y * cell_height
        maze_cell = cell.Cell(value, cell_width, cell_height, x_cor, y_cor)
        cells[(x, y)] = maze_cell

screen.fill("grey")

cell_index = 0
clock = pygame.time.Clock()
current_pos = STARTING_POS
traceback = 0

has_drawn_grid = False
FPS = 30

#start timing
maze_done = False
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                DELAY_FRAMES = True
                FPS = MAX_FPS
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                DELAY_FRAMES = False
                FPS = 15

    #keypresses
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False


    if not has_drawn_grid:
        for cell in cells.values():
            cell.draw(screen)
        has_drawn_grid = True

    if current_pos is not None:
        current_pos, traceback = generator.maze_generator(traceback, current_pos, cells, screen, GRID_SIZE_X, GRID_SIZE_Y)
        pygame.display.flip()

    elif current_pos is None and not maze_done:
        end_time = time.time()
        print(f"Final time is: {end_time - start_time:.4} seconds")
        maze_done = True


    if DELAY_FRAMES:
        clock.tick(FPS)

pygame.quit()
