import random

nb_choice = None
visited = []
solution_stack = []

def init_solver(grid_size_x, grid_size_y, use_seed, seed, neighbour_choice):
    global visited, nb_choice
    visited = [[False for _ in range(grid_size_x)] for _ in range(grid_size_y)]
    nb_choice = neighbour_choice
    if use_seed:
        random.seed(seed)


def maze_solver(current_pos, cells, screen, grid_size_x, grid_size_y, maze):
    current_x, current_y = current_pos
    visited[current_y][current_x] = True
    neighbours = find_neighbours(maze, current_pos, grid_size_x, grid_size_y)

    if current_pos in cells:
        cells[current_pos].solver_visited(screen)

    if len(neighbours) > 0:
        solution_stack.append(current_pos)
        if nb_choice == "1":
            goal_pos = neighbours[0]
        elif nb_choice == "2":
            goal_pos = neighbours[-1]
        else:
            goal_pos = random.choice(neighbours)
        current_pos = goal_pos

        if goal_pos in cells:
            cells[goal_pos].solver_visited(screen)
        if current_pos == ((grid_size_x - 2), grid_size_y - 1): #check for maze exit
            solution_stack.append(current_pos)
            for pos in solution_stack:
                if pos in cells:
                    cells[pos].color_solution(screen)
            return None

    else:
        if not solution_stack:
           return None
        else:
            current_pos = solution_stack.pop()

    return current_pos



def find_neighbours(maze, current_pos, grid_size_x, grid_size_y):
    current_x, current_y = current_pos
    neighbours = []
    if current_x + 1 < grid_size_x and not visited[current_y][current_x + 1] and maze[current_y][current_x + 1] == 0:   #rechts
        neighbours.append((current_x + 1, current_y))
    if current_x - 1 >= 0 and not visited[current_y][current_x - 1] and maze[current_y][current_x - 1] == 0:            #links
        neighbours.append((current_x - 1, current_y))
    if current_y + 1 < grid_size_y and not visited[current_y + 1][current_x] and maze[current_y + 1][current_x] == 0:   #onder
        neighbours.append((current_x, current_y + 1))
    if current_y - 1 >= 0 and not visited[current_y - 1][current_x] and maze[current_y - 1][current_x] == 0:            #boven
        neighbours.append((current_x, current_y - 1))
    return neighbours
