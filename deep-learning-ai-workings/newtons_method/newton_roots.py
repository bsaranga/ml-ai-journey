import numpy as np
import matplotlib.pyplot as plt
from gradient_descent import grad as g

#x = x_0 - f(x)/f'(x)

x = np.linspace(-2, 7, 100)

def polynomial(x):
    return (x - np.e)**2 - 2*np.pi

def newtons_method_root(f, x0, threshold=0.01):
    x = x0
    iteration = 0
    while abs(f(x)) >= threshold:
        x = x - f(x)/g.gradient_at(x, f)
        iteration += 1

    print(f"Iterations: {iteration}")
    return x

root1 = newtons_method_root(polynomial, 2)
root2 = newtons_method_root(polynomial, 4)

plt.plot(x, polynomial(x))
plt.plot(root1, 0, 'ro')
plt.plot(root2, 0, 'ro')
plt.grid(True, 'both')
plt.axhline(y=0, color='k')
plt.show()