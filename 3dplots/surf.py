import matplotlib.pyplot as plt
import numpy as np

from gradient_descent import grad as g

def fn(x,y):
    return x**2 + y**2

def f_example_3(x,y):
    return (85+ 0.1*(- 1/9*(x-6)*x**2*y**3 + 2/3*(x-6)*x**2*y**2))

result = g.gradient_descent2([2,0.5], 0.26, f_example_3)

minima = result[0]
path_x_coords, path_y_coords = np.split(result[1], 2, axis=1)
path_z_coords = f_example_3(path_x_coords, path_y_coords)

# Make data
X = np.linspace(0, 5, 50)
Y = np.linspace(0, 5, 50)
X, Y = np.meshgrid(X, Y)
Z = f_example_3(X, Y)

# Plot the surface
fig, ax = plt.subplots(figsize=(8,8), subplot_kw={"projection": "3d"})

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

ax.plot_surface(X, Y, Z, antialiased=True, cmap='coolwarm', zorder=1)
ax.plot(path_x_coords, path_y_coords, path_z_coords, zorder=10, color='blue')
ax.plot(path_x_coords, path_y_coords, path_z_coords, '*', zorder=11, color='yellow')
ax.plot(minima[0], minima[1], f_example_3(minima[0], minima[1]), 'ro', zorder=12)

plt.show()