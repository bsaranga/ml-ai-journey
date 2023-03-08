import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from gradient_descent import grad as g

def fn(x,y):
    return x**2 + y**2

def f_example_3(x,y):
    return (85+ 0.1*(- 1/9*(x-6)*x**2*y**3 + 2/3*(x-6)*x**2*y**2))

# Make data
X = np.linspace(0, 5, 50)
Y = np.linspace(0, 5, 50)
X, Y = np.meshgrid(X, Y)
Z = f_example_3(X,Y)

minimum = [0,0,0]

# Plot the surface
fig, ax = plt.subplots(figsize=(8,8), subplot_kw={"projection": "3d"})

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

ax.plot_surface(X, Y, Z, antialiased=True, cmap='coolwarm', zorder=1)
ax.autoscale(enable=False)

plt.show()