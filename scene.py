import pygame
import sys

class Scene(object):
    grey = (150, 150, 150)
    red = (255,0,0)
    green = (0,255,0)
    white = (200, 200, 200)

    def __init__(self, size, grid):
        self.size = size
        self.grid = grid
        self.rect_size = size / grid

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.size, self.size))
        self.screen.fill(self.white)

    def draw_rect(self, x, y, color='green'):
        self.screen.fill(self.white)
        pygame.draw.rect(self.screen, self.green, (x, y, self.rect_size, self.rect_size), 0)
        pygame.display.update()
