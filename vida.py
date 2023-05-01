import numpy as np

# tamaño de la cuadricula
N = 5
grid = np.array([[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]])

def update(grid):
    # crea una nueva cuadricula para almacenar el estado actualizado
    new_grid = np.zeros_like(grid)

    # recorre cada celda de la cuadricula
    for i in  range(N):
        for j in range(N):
            # cuenta el numero de vecinos vivos
            neighbors = np.sum(grid[i-1:i+2,j-1:j+2]) - grid[i,j]

            # Aplica las reglas del Juego de la Vida
            if grid[i, j] == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[i, j] = 1
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    # devuelve la cuadricula actualizada
    return new_grid

# numero de iteraciones
iterations =  5

#ejecuta el juego
for i in range (iterations):
    print(f"iterations {i}:")
    print(grid)
    grid =  update(grid)