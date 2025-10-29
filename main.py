import pygame, time
import cell
import generator
import solver
import config as c



def setup_config():
    cfg = {
        #main stuff
        "DELAY_FRAMES": c.DELAY_FRAMES,
        "MAX_FPS": c.MAX_FPS,
        "STARTING_POS": c.STARTING_POS,
        "CELL_PIXEL_SIZE": c.CELL_PIXEL_SIZE,
        "FULLSCREEN": c.FULLSCREEN,
        "FPS": c.FPS,
        "NEIGHBOUR_CHOICE": c.NEIGHBOUR_CHOICE,

        #randomness
        "GEN_USE_SEED": c.GEN_USE_SEED,
        "GEN_SEED": c.GEN_SEED,
        "SOLV_USE_SEED": c.SOLV_USE_SEED,
        "SOLV_SEED": c.SOLV_SEED,

        #cell stuff
        "PATH_COLOR": c.PATH_COLOR,  # springgreen4
        "WALL_COLOR": c.WALL_COLOR,  # gray10
        "POS_COLOR": c.POS_COLOR,  # darkorange1
        "VISITED_COLOR": c.VISITED_COLOR,  # orange
        "SOLUTION_COLOR": c.SOLUTION_COLOR  # orangered
    }

    #screen and grid dimensions
    if cfg["FULLSCREEN"]:
        cfg["X_CELLS"] = 1920 // cfg["CELL_PIXEL_SIZE"]
        cfg["Y_CELLS"] = 1080 // cfg["CELL_PIXEL_SIZE"]
        cfg["SCREEN_WIDTH"], cfg["SCREEN_HEIGHT"] = 1920, 1080
    else:
        cfg["X_CELLS"] = c.X_CELLS
        cfg["Y_CELLS"] = c.Y_CELLS
        cfg["SCREEN_WIDTH"] = cfg["CELL_PIXEL_SIZE"] * cfg["X_CELLS"]
        cfg["SCREEN_HEIGHT"] = cfg["CELL_PIXEL_SIZE"] * cfg["Y_CELLS"]

    # make grid_size uneven
    if cfg["X_CELLS"] % 2 == 0:
        cfg["GRID_SIZE_X"] = cfg["X_CELLS"] - 1
    else:
        cfg["GRID_SIZE_X"] = cfg["X_CELLS"]
    if cfg["Y_CELLS"] % 2 == 0:
        cfg["GRID_SIZE_Y"] = cfg["Y_CELLS"] - 1
    else:
        cfg["GRID_SIZE_Y"] = cfg["Y_CELLS"]

    return cfg



def setup_pygame(cfg):
    # pygame setup
    pygame.init()

    if cfg["FULLSCREEN"]:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((cfg["SCREEN_WIDTH"], cfg["SCREEN_HEIGHT"]))
    screen.fill("grey")

    return screen, pygame.time.Clock()

def create_maze_grid(cfg):
    #set al cells to walls
    maze = [[1 for _ in range(cfg["GRID_SIZE_X"])] for _ in range(cfg["GRID_SIZE_Y"])]

    #create entrance and exit
    maze[0][1] = 0
    maze[-1][-2] = 0

    cell_width = cfg["SCREEN_WIDTH"] // cfg["GRID_SIZE_X"]
    cell_height = cfg["SCREEN_HEIGHT"] // cfg["GRID_SIZE_Y"]

    #all cels in a dict for quick lookup using (x, y) position
    cells = {}
    for y, row in enumerate(maze):
        for x, value in enumerate(row):
            x_cor = x * cell_width
            y_cor = y * cell_height
            maze_cell = cell.Cell(value, cell_width, cell_height, x_cor, y_cor, cfg["PATH_COLOR"], cfg["WALL_COLOR"], cfg["POS_COLOR"], cfg["VISITED_COLOR"], cfg["SOLUTION_COLOR"])
            cells[(x, y)] = maze_cell

    return cells, maze


def main():
    cfg = setup_config()
    generator.init_maze(cfg["GRID_SIZE_X"], cfg["GRID_SIZE_Y"], cfg["GEN_USE_SEED"], cfg["GEN_SEED"])
    solver.init_solver(cfg["GRID_SIZE_X"], cfg["GRID_SIZE_Y"], cfg["SOLV_USE_SEED"], cfg["SOLV_SEED"], cfg["NEIGHBOUR_CHOICE"])
    screen, clock = setup_pygame(cfg)
    cells, maze = create_maze_grid(cfg)


    #draw starting grid
    for grid_cell in cells.values():
        grid_cell.draw(screen)

    # setup
    current_pos = cfg["STARTING_POS"]
    solver_pos = (1, 0)
    running = True

    #start timing
    gen_end_time, solv_end_time = None, None
    maze_done = False
    solution_done = False
    start_time = time.time()

    while running:
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    cfg["DELAY_FRAMES"] = True
                    cfg["FPS"] = cfg["MAX_FPS"]

            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                cfg["DELAY_FRAMES"] = False
                cfg["FPS"] = c.FPS

        #maze generator
        if current_pos is not None:
            current_pos, maze = generator.maze_generator(current_pos, cells, screen, cfg["GRID_SIZE_X"], cfg["GRID_SIZE_Y"])
            pygame.display.flip()

        elif not maze_done:
            gen_end_time = time.time()
            print(f"Generating time is: {gen_end_time - start_time:.4f} seconds")
            maze_done = True

        #solver
        if maze_done and solver_pos is not None:
            solver_pos = solver.maze_solver(solver_pos, cells, screen, cfg["GRID_SIZE_X"], cfg["GRID_SIZE_Y"], maze)
            pygame.display.flip()

        elif maze_done and not solution_done:
            solv_end_time = time.time()
            print(f"Solution time is: {solv_end_time - gen_end_time:.4f} seconds")
            print(f"Final time is: {solv_end_time - start_time:.4f} seconds")
            solution_done = True


        if cfg["DELAY_FRAMES"]:
            clock.tick(cfg["FPS"])
    pygame.quit()


#run maze generator
main()
