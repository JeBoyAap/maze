import pygame

class Cell:
    def __init__(self, cell_type, width, height, x_cor, y_cor, path_color="springgreen4" ,wall_color="gray10", pos_color="darkorange1", visited_color="orange", solution_color="orangered"):
        self.cell_type = cell_type
        self.width = width
        self.height = height
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.path_color = path_color            #"springgreen4"
        self.wall_color = wall_color            #"gray10"
        self.pos_color = pos_color              #"darkorange1"
        self.visited_color = visited_color      #"orange"
        self.solution_color = solution_color    #"orangered1"

    def draw(self, screen):
        if self.cell_type == 0:
            pygame.draw.rect(screen, pygame.Color(self.path_color), (self.x_cor, self.y_cor, self.width, self.height))
        elif self.cell_type == 1:
            pygame.draw.rect(screen, pygame.Color(self.wall_color), (self.x_cor, self.y_cor, self.width, self.height))

    def make_path(self, screen):
        pygame.draw.rect(screen, pygame.Color(self.path_color), (self.x_cor, self.y_cor, self.width, self.height))

    def color_current_pos(self, screen):
        pygame.draw.rect(screen, pygame.Color(self.pos_color), (self.x_cor, self.y_cor, self.width, self.height))

    def solver_visited(self, screen):
        pygame.draw.rect(screen, pygame.Color(self.visited_color), (self.x_cor, self.y_cor, self.width, self.height))

    def color_solution(self, screen):
        pygame.draw.rect(screen, pygame.Color(self.solution_color), (self.x_cor, self.y_cor, self.width, self.height))