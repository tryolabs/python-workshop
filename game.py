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

# definicion de los colores en RGB
SNAKE_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)


def render(screen, snake_position):
    """dibuja en la pantalla el fondo y la vibora"""
    screen.fill(BACKGROUND_COLOR)

    # dibujar la vabeza de la vibora
    pygame.draw.rect(
        screen,
        SNAKE_COLOR,
        (
            snake_position[0] * TILE_SIZE,
            snake_position[1] * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE,
        ),
    )

    # Actualizar la pantalla
    pygame.display.flip()


def check_key(events, key):
    """Verifica si la tecla fue apretada"""
    for event in events:
        if event.type == pygame.KEYUP and event.key == key:
            return True
    return False


def move(events, current_position):
    """calcula la nueva posicion de la vibora"""
    update_vector = None
    # calcular el vector hacia donde deberia moverse
    if check_key(events, K_RIGHT):
        update_vector = (1, 0)
    if check_key(events, K_LEFT):
        update_vector = (-1, 0)
    if check_key(events, K_UP):
        update_vector = (0, -1)
    if check_key(events, K_DOWN):
        update_vector = (0, 1)

    # no hacer nada si ninguna de esas teclas fue apretada
    if update_vector is None:
        return current_position

    # calcular la nueva posicion
    return (
        (current_position[0] + update_vector[0]) % GRID_DIMENSIONS[0],
        (current_position[1] + update_vector[1]) % GRID_DIMENSIONS[1],
    )


snake_position = (0, 0)

# Reloj usado para mantener una tasa de refresco constante
clock = pygame.time.Clock()

# Inicializar el motor de pygame y la pantalla
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tryolabs Python Workshop Project")

# loop principal
running = True
while running:
    # Mantener el loop corriendo a la velocidad correcta
    clock.tick(FPS)

    events = pygame.event.get()

    # Verificar si el usuario quiere cerrar la ventana
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Actualizar el juego y dibujar en pantalla
    snake_position = move(events, snake_position)
    render(screen, snake_position)
# Ejecutar rutina de limpieza
pygame.quit()
