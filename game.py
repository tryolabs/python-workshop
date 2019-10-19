from enum import Enum

import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP

# FPS (Frames Per Second): número de veces que la pantalla se redibuja por segundo
FPS = 60

# Dimensiones de la pantalla (medida en cudrantes)
GRID_DIMENSIONS = (20, 15)
# Ancho de la pantalla
WIDTH = 800

# El tamaño en píxeles de cada cuadrante y el ancho de la pantalla se calculan a partir
# del ancho en píxeles y las dimensiones de la grilla
TILE_SIZE = WIDTH // GRID_DIMENSIONS[0]
HEIGHT = GRID_DIMENSIONS[1] * TILE_SIZE


class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


class Snake:
    SNAKE_COLOR = (0, 255, 0)

    def __init__(self, initial_position=(0, 0)):
        self.position = initial_position

    def render(self, screen):
        pygame.draw.rect(
            screen,
            Snake.SNAKE_COLOR,
            (
                self.position[0] * TILE_SIZE,
                self.position[1] * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            ),
        )

    def update(self, direction):
        if direction == Direction.UP:
            update_vector = (0, -1)
        elif direction == Direction.DOWN:
            update_vector = (0, 1)
        elif direction == Direction.LEFT:
            update_vector = (-1, 0)
        else:  # direction == Direction.RIGHT
            update_vector = (1, 0)

        self.position = (
            (self.position[0] + update_vector[0]) % GRID_DIMENSIONS[0],
            (self.position[1] + update_vector[1]) % GRID_DIMENSIONS[1],
        )


class SnakeGame:
    """Clase principal que maneja el juego"""

    BACKGROUND_COLOR = (0, 0, 0)

    def __init__(self, width=WIDTH, height=HEIGHT):
        self.width = width
        self.height = height

        # Inicializar el motor de pygame y la pantalla
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tryolabs Python Workshop Project")

        # Reloj usado para mantener una tasa de refresco constante
        self.clock = pygame.time.Clock()

        self.snake = Snake()

    def cleanup(self):
        """Función llamada al cerrar el juego"""
        pygame.quit()

    def check_key(self, events, key):
        for event in events:
            if event.type == pygame.KEYUP and event.key == key:
                return True
        return False

    def update(self, events):
        """Ejecuta la lógica del juego y actualiza la pantalla"""

        # Mover la serpiente
        if self.check_key(events, K_RIGHT):
            self.snake.update(Direction.RIGHT)
        elif self.check_key(events, K_LEFT):
            self.snake.update(Direction.LEFT)
        elif self.check_key(events, K_UP):
            self.snake.update(Direction.UP)
        elif self.check_key(events, K_DOWN):
            self.snake.update(Direction.DOWN)

    def render(self):
        """Dibuja el frame actual en pantalla"""
        # Mostrar el fondo
        self.screen.fill(SnakeGame.BACKGROUND_COLOR)

        # Mostrar la serpiente
        self.snake.render(self.screen)

        # Actualizar la pantalla
        pygame.display.flip()

    def execute(self):
        """Loop principal que mantiene el juego funcionando"""
        running = True
        while running:
            # Mantener el loop corriendo a la velocidad correcta
            self.clock.tick(FPS)

            events = pygame.event.get()

            # Verificar si el usuario quiere cerrar la ventana
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            # Actualizar el juego y dibujar en pantalla
            self.update(events)
            self.render()

        # Ejecutar rutina de limpieza
        self.cleanup()


# Instanciar el juego y comenzar la ejecución
snake_game = SnakeGame()
snake_game.execute()
