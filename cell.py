import pygame

class Cell:
    def __init__(self, cell_type, width, height, x_cor, y_cor):
        self.cell_type = cell_type
        self.width = width
        self.height = height
        self.x_cor = x_cor
        self.y_cor = y_cor

    def draw(self, screen):
        print(self.x_cor, self.y_cor)
        if self.cell_type == 0:
            pygame.draw.rect(screen, "orange", (self.x_cor, self.y_cor, self.width, self.height))
        elif self.cell_type == 1:
            pygame.draw.rect(screen, "black", (self.x_cor, self.y_cor, self.width, self.height))
