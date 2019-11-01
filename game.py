import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP

from constants import FPS, HEIGHT, WIDTH
from models import Apple, Direction, Snake


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

        self.apple = Apple()

    def initialize(self):
        """Reinicia el juego a su estado inicial"""
        # Instanciar la serpiente y la manzana
        self.snake = Snake()
        self.apple = Apple()

    def cleanup(self):
        """Función llamada al cerrar el juego"""
        pygame.quit()

    def check_collisions(self):
        """Chequea si la serpiente comió la manzana"""
        # Chequear si la serpiente se comió la manzana
        if self.snake.has_eaten_apple(self.apple.position):
            # Crear una manzana nueva
            self.apple = Apple()

            # Aumentar el tamaño de la serpiente
            self.snake.grow()
            self.snake.increase_speed()
        # Chequear si la serpiente se golpeó consigo misma
        if self.snake.has_collided():
            self.initialize()

    def update(self, events):
        """Ejecuta la lógica del juego y actualiza la pantalla"""
        direction = None
        # Mover la serpiente
        for event in events:
            if event.type == pygame.KEYUP and event.key == K_RIGHT:
                direction = Direction.RIGHT
            elif event.type == pygame.KEYUP and event.key == K_LEFT:
                direction = Direction.LEFT
            elif event.type == pygame.KEYUP and event.key == K_UP:
                direction = Direction.UP
            elif event.type == pygame.KEYUP and event.key == K_DOWN:
                direction = Direction.DOWN

        self.snake.update(direction)
        # Chequear si la serpiente comió la manzana
        self.check_collisions()

    def render(self):
        """Dibuja el frame actual en pantalla"""
        # Mostrar el fondo
        self.screen.fill(SnakeGame.BACKGROUND_COLOR)

        # Mostrar la serpiente
        self.snake.render(self.screen)

        # Mostrar la manzana
        self.apple.render(self.screen)

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
if __name__ == "__main__":
    snake_game = SnakeGame()
    snake_game.execute()
