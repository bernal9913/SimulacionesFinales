import random
import matplotlib.pyplot as plt

# Define the vertices of the triangle
vertices = [(0, 0), (0.5, 1), (1, 0)]

# Choose a random starting point
x, y = random.choice(vertices)

# Initialize lists to store the x and y coordinates of the points
x_coords = []
y_coords = []

# Iterate for a large number of points
for i in range(100000):
    # Choose a random vertex
    vertex = random.choice(vertices)
    # Compute the midpoint between the current point and the chosen vertex
    x = (x + vertex[0]) / 2
    y = (y + vertex[1]) / 2
    # Append the new point to the lists
    x_coords.append(x)
    y_coords.append(y)

# Plot the points
plt.scatter(x_coords, y_coords, s=0.1)
plt.show()