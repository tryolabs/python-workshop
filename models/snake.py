from enum import Enum

import pygame

from constants import GRID_DIMENSIONS, TILE_SIZE


class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

    @classmethod
    # Chequear si dos direcciones son opuestas
    def are_opposite(cls, dir1, dir2):
        return {dir1, dir2} in [
            {Direction.LEFT, Direction.RIGHT},
            {Direction.UP, Direction.DOWN},
        ]


class SnakeSegment:
    SNAKE_COLOR = (0, 255, 0)

    def __init__(self, position, in_direction, out_direction=None):
        self.position = position
        self.in_direction = in_direction
        self.out_direction = in_direction if out_direction is None else out_direction

        if out_direction is None:
            out_direction = in_direction

    def render(self, screen):
        pygame.draw.rect(
            screen,
            SnakeSegment.SNAKE_COLOR,
            (
                self.position[0] * TILE_SIZE,
                self.position[1] * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            ),
        )


class Snake:
    def __init__(self, initial_position=(2, 0), initial_speed=2):
        # Cada cuántos segundos debe moverse la serpiente
        self.speed = initial_speed

        # Reloj brindado por pygame para calcular el tiempo que pasó
        # desde la última vez que se movió la serpiente
        self.clock = pygame.time.Clock()
        # Segundos desde el último movimiento
        self.time_since_last_move = 0

        self.position = initial_position
        self.current_direction = Direction.RIGHT

        self.increase_size = False

        # Inicializo una serpiente de 3 segmentos
        body_positions = [
            (initial_position[0] - i, initial_position[1]) for i in range(2, -1, -1)
        ]
        self.body = [
            # la cola de la serpiente
            SnakeSegment(body_positions[0], Direction.RIGHT),
            # el cuerpo de la serpiente
            SnakeSegment(body_positions[1], Direction.RIGHT),
            # la cabeza de la serpiente
            SnakeSegment(body_positions[2], Direction.RIGHT),
        ]

    def render(self, screen):
        for segment in self.body:
            segment.render(screen)

    def grow(self):
        self.increase_size = True

    def update(self, direction):
        if Direction.are_opposite(self.current_direction, direction):
            direction = None
        if direction is not None:
            self.current_direction = direction


        self.time_since_last_move += self.clock.tick()

        # Obtengo la posicion de la cabeza anterior
        old_head = self.body[-1]
        self.time_since_last_move += self.clock.tick()
        
        if self.time_since_last_move >= self.speed * 1000:
            self.time_since_last_move = 0 
            # Calcular la nueva posición de la cabeza de la serpiente
            new_head_x, new_head_y = old_head.position
            if self.current_direction == Direction.UP:
                new_head_y = (new_head_y - 1) % GRID_DIMENSIONS[1]
            elif self.current_direction == Direction.DOWN:
                new_head_y = (new_head_y + 1) % GRID_DIMENSIONS[1]
            elif self.current_direction == Direction.RIGHT:
                new_head_x = (new_head_x + 1) % GRID_DIMENSIONS[0]
            else:
                new_head_x = (new_head_x - 1) % GRID_DIMENSIONS[0]

            # Agregar la nueva cabeza a la lista de segmentos
            self.body.append(SnakeSegment((new_head_x, new_head_y), self.current_direction))

            # Solo remuevo la antigua cola si la serpiente no crecio
            if not self.increase_size:
                # Remover la antigua cola de la serpiente
                self.body.pop(0)
            else:
                # Una vez que ya crecio (no elimino la cola), vuelve a su estado normal (increase_size = False)
                self.increase_size = False


    def increase_speed(self):
        self.speed -= self.speed * 0.1

    def has_eaten_apple(self, apple_position):
        # Ahora que tiene cuerpo, hay que chequear si la cabeza coincide con la manzana
        return self.body[-1].position == apple_position

    def has_collided(self):
        all_positions = [segment.position for segment in self.body]
        return all_positions[-1] in all_positions[:-1]
