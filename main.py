import pygame, cell, time

# pygame setup
pygame.init()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

DELAY = 0

maze = [
    [1,0,1,1,0,0,1,0,0,1],
    [0,0,1,0,1,1,0,1,0,0],
    [1,0,0,0,0,1,0,0,1,1],
    [1,1,0,1,0,0,1,0,0,0],
    [0,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [0,0,0,1,0,1,0,0,1,0],
    [1,1,0,0,0,1,1,0,0,1],
    [0,0,1,1,0,0,1,0,1,0],
    [1,0,0,0,1,1,0,0,0,1]
]

import random

maze = [[random.randint(0, 1) for _ in range(100)] for _ in range(100)]

cell_width = int(SCREEN_WIDTH / len(maze[0]))
cell_height = int(SCREEN_HEIGHT / len(maze))

cells = []
y_cor = 0
for row in maze:
    x_cor = 0
    for value in row:
        maze_cell = cell.Cell(value, cell_width, cell_height, x_cor, y_cor)
        cells.append(maze_cell)
        x_cor += cell_width
    y_cor += cell_height

# fill background
screen.fill("grey")

# index of the next cell to draw
cell_index = 0

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cell_index < len(cells):
        cells[cell_index].draw(screen)
        pygame.display.flip()
        cell_index += 1
        pygame.time.wait(DELAY)  # 100 ms pause per cell

    clock.tick(60)


pygame.quit()