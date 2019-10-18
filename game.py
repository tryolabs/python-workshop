import pygame

# Dimensiones de la pantalla (medida en cudrantes)
GRID_DIMENSIONS = (20, 15)
# Ancho de la pantalla
WIDTH = 800

# El tamaño en píxeles de cada cuadrante y el ancho de la pantalla se calculan a partir
# del ancho en píxeles y las dimensiones de la grilla
TILE_SIZE = WIDTH // GRID_DIMENSIONS[0]
HEIGHT = GRID_DIMENSIONS[1] * TILE_SIZE

# deinicion de los colores en RGB
SNAKE_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Inicializar el motor de pygame y la pantalla
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tryolabs Python Workshop Project")

# loop principal
running = True
while running:
    events = pygame.event.get()

    # Verificar si el usuario quiere cerrar la ventana
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Actualizar el juego y dibujar en pantalla
    screen.fill(BACKGROUND_COLOR)

# Ejecutar rutina de limpieza
pygame.quit()
