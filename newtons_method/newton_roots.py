import numpy as np
import matplotlib.pyplot as plt

#x = x_0 - f(x)/f'(x)

x = np.linspace(-2, 7, 100)

def polynomial(x):
    return (x - np.e)**2 - 2*np.pi

plt.plot(x, polynomial(x))
plt.plot(0,0, 'ro')
plt.grid(True, 'both')
plt.axhline(y=0, color='k')
plt.show()