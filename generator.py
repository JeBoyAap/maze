import random
debug = False

maze = []
visited = []
traceback_stack = []

def init_maze(grid_size_x, grid_size_y, use_seed, seed):
    global maze, visited
    maze = [[1 for _ in range(grid_size_x)] for _ in range(grid_size_y)]
    visited = [[False for _ in range(grid_size_x)] for _ in range(grid_size_y)]
    if use_seed:
        random.seed(seed)

def maze_generator(current_pos, prev_pos, cells, screen, grid_size_x, grid_size_y):
    current_x, current_y = current_pos
    visited[current_y][current_x] = True
    neighbours = find_neighbours(current_pos, grid_size_x, grid_size_y)

    if current_pos in cells:
        cells[current_pos].color_current_pos(screen)
    if prev_pos in cells:
        cells[prev_pos].make_path(screen)
    prev_pos = current_pos
    if len(neighbours) > 0:
        goal_pos = random.choice(neighbours)
        wall_pos = ((goal_pos[0] + current_pos[0]) // 2, (goal_pos[1] + current_pos[1]) // 2)

        if goal_pos in cells:
            cells[goal_pos].make_path(screen)
        if wall_pos in cells:
            cells[wall_pos].make_path(screen)

        traceback_stack.append(current_pos)
        maze[current_y][current_x] = 0
        current_pos = goal_pos


    else:
        if not traceback_stack:
            if prev_pos in cells:
                cells[prev_pos].make_path(screen)
            return None, None
        else:
            current_pos = traceback_stack.pop()

    return current_pos, prev_pos

def find_neighbours(current_pos, grid_size_x, grid_size_y):
    current_x, current_y = current_pos
    neighbours = []
    if current_x + 2 < grid_size_x and not visited[current_y][current_x + 2]:
        neighbours.append((current_x + 2, current_y))
    if current_x - 2 >= 0 and not visited[current_y][current_x - 2]:
        neighbours.append((current_x - 2, current_y))
    if current_y + 2 < grid_size_y and not visited[current_y + 2][current_x]:
        neighbours.append((current_x, current_y + 2))
    if current_y - 2 >= 0 and not visited[current_y - 2][current_x]:
        neighbours.append((current_x, current_y - 2))

    if debug: print(f"current pos: {current_pos}, unvisited neighbours: {neighbours}") #debug
    if debug: print(f"traceback stack: {traceback_stack}")
    if debug: print(f"visited: {visited}")

    #print(f"current pos: {current_pos}")
    return neighbours
