import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from gradient_descent import grad as g

def fn(x,y):
    return x**2 + y**2


# Make data
X = np.arange(-5, 5, .1)
Y = np.arange(-5, 5, .1)
X, Y = np.meshgrid(X, Y)
Z = fn(X,Y)

minimum = [0,0,0]

# Plot the surface
fig, ax = plt.subplots(figsize=(8,8), subplot_kw={"projection": "3d"})

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues, zorder=1)

ax.plot(minimum[0], minimum[1], minimum[2], marker='o', color='red', zorder=10)

plt.show()