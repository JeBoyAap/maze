#main.py config

DELAY_FRAMES = False
FPS = 30 #max fps when delaying frames
MAX_FPS = 1 #max fps when holding space

STARTING_POS = (1,1)

CELL_PIXEL_SIZE = 5

FULLSCREEN = True

#use when windowed
X_CELLS = 50
Y_CELLS = 50


#cell.py config
PATH_COLOR = "springgreen4"   # default: "springgreen4"
WALL_COLOR = "gray10"         # default: "gray10"
POS_COLOR = "darkorange1"     # default: "darkorange1"
VISITED_COLOR = "orange"      # default: "orange"
SOLUTION_COLOR = "orangered"  # default: "orangered"


#generator.py config
GEN_USE_SEED = True #random maze every time
GEN_SEED = 2

#solver.py config
NEIGHBOUR_CHOICE = "1" #"1", focus on going right, "2" focus on going down, "random" for random choice

SOLV_USE_SEED = False
SOLV_SEED = 1