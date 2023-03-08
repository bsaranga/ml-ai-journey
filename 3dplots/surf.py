import matplotlib.pyplot as plt
import numpy as np

from gradient_descent import grad as g

def fn(x,y):
    return x**2 + y**2

def f_example_3(x,y):
    return (85+ 0.1*(- 1/9*(x-6)*x**2*y**3 + 2/3*(x-6)*x**2*y**2))

result = g.gradient_descent2([0.5,0.5], 0.25, f_example_3)
print(result[0])
print(result[1])

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
ax.plot([0,2,5],[0,2,5],[80,80,80], zorder=10, color='green')
ax.autoscale(enable=False)

plt.show()