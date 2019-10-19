import os

import pygame

from models import Direction, SnakePart


class GraphicsUtils:

    def __init__(self, window_size, game_tile_size, images_folder):
        self.window_size = window_size
        self.tile_size = game_tile_size

        self.grass_path = os.path.join(images_folder, "pasto.jpg")

        self.apple_path = os.path.join(images_folder, "manzana.png")

        self.snake_graphics_map = {
            SnakePart.HEAD: os.path.join(images_folder, "cabeza.png"),
            SnakePart.HEAD_WITH_TONGUE: os.path.join(
                images_folder, "cabeza-lengua.png"
            ),
            SnakePart.STRAIGHT_BODY: os.path.join(images_folder, "cuerpo.png"),
            SnakePart.CURVED_BODY: os.path.join(images_folder, "esquina.png"),
            SnakePart.TAIL: os.path.join(images_folder, "cola.png"),
        }

        for body_part, path in self.snake_graphics_map.items():
            self.snake_graphics_map[body_part] = pygame.image.load(path).convert_alpha()

        self.apple_graphics = pygame.transform.scale(
            pygame.image.load(self.apple_path).convert_alpha(),
            (self.tile_size, self.tile_size),
        )

        # Crear la imagen con pasto para ser usada en el fondo
        grass_tile = pygame.transform.scale(
            pygame.image.load(self.grass_path).convert(),
            (self.tile_size * 3, self.tile_size * 3),
        )
        grass_tile_width = grass_tile.get_width()
        grass_tile_height = grass_tile.get_height()

        # Crear la imagen de fondo repitiendo el patrón con pasto
        self.background_graphics = pygame.Surface(self.window_size)
        for x in range(0, self.window_size[0], grass_tile_width):
            for y in range(0, self.window_size[1], grass_tile_height):
                self.background_graphics.blit(grass_tile, (x, y))

    def get_rotation(self, in_direction, out_direction):
        if out_direction is None:
            out_direction = in_direction

        return {
            (Direction.RIGHT, Direction.RIGHT): 0,
            (Direction.DOWN, Direction.DOWN): 270,
            (Direction.LEFT, Direction.LEFT): 180,
            (Direction.UP, Direction.UP): 90,
            (Direction.RIGHT, Direction.UP): 0,
            (Direction.DOWN, Direction.LEFT): 0,
            (Direction.DOWN, Direction.RIGHT): 270,
            (Direction.LEFT, Direction.UP): 270,
            (Direction.LEFT, Direction.DOWN): 180,
            (Direction.UP, Direction.RIGHT): 180,
            (Direction.UP, Direction.LEFT): 90,
            (Direction.RIGHT, Direction.DOWN): 90,
        }[in_direction, out_direction]

    def get_snake_part(self, body_part, in_direction, out_direction=None):
        graphics = self.snake_graphics_map[body_part]
        rotation = self.get_rotation(in_direction, out_direction)
        return pygame.transform.scale(
            pygame.transform.rotate(graphics, rotation),
            (self.tile_size, self.tile_size),
        )

    def get_apple(self):
        return self.apple_graphics

    def get_background(self):
        return self.background_graphics
