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

# Puntaje de cada manzana
APPLE_POINTS = 10