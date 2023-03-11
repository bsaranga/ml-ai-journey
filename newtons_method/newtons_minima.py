import numpy as np
import matplotlib.pyplot as plt
from gradient_descent import grad as g

x = np.linspace(-2, 7, 100)

def polynomial(x):
    return (x - np.e)**2 - 2*np.pi

def newtons_method_min(f, x0, threshold=0.01):
    x = x0
    iteration = 0
    while abs(g.gradient_at(x,f)) >= threshold:
        x = x - g.gradient_at(x, f)/g.second_derivative_at(x, f, epsilon=0.001)
        iteration += 1

    print(f"Iterations: {iteration}")
    return x

minima = newtons_method_min(polynomial, 6, threshold=0.001)
print(minima)

plt.plot(x, polynomial(x))
plt.plot(minima, polynomial(minima), 'ro')
plt.grid(True, 'both')
plt.axhline(y=0, color='k')
plt.show()