import random

import pygame

from constants import GRID_DIMENSIONS, TILE_SIZE


class Apple:
    APPLE_COLOR = (255,0,0)
    def __init__(self):
        self.position = (
            random.randint(0, GRID_DIMENSIONS[0] -1),
            random.randint(0, GRID_DIMENSIONS[1] -1),
        )

    def render(self, screen):
        pygame.draw.rect(
            screen,
            Apple.APPLE_COLOR,
            (
                self.position[0] * TILE_SIZE,
                self.position[1] * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            ),
        )
        