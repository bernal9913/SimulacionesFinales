import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    if n == max_iter:
        return max_iter
    return n

# Tamaño de la imagen (en píxeles)
width = 600
height = 400

# Rango de valores para el eje x y y
xmin = -2.0
xmax = 1.0
ymin = -1.4
ymax = 1.4

# Máximo número de iteraciones
max_iter = 256

# Creamos una imagen en blanco con los valores RGB en cero (negro)
image = np.zeros((height, width, 3))

# Generamos los valores para cada pixel
for i in range(width):
    for j in range(height):
        x = i / width * (xmax - xmin) + xmin
        y = j / height * (ymax - ymin) + ymin
        c = x + y * 1j
        m = mandelbrot(c, max_iter)
        color = 1 - np.sqrt(m / max_iter)
        image[j, i] = (color, color, color)

# Mostramos la imagen generada con matplotlib
plt.imshow(image)
plt.axis('off')
plt.show()