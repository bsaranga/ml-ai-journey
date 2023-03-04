import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
plt.plot(np.sin(x))
plt.plot(np.cos(x))

at_x1 = np.pi
plt.plot([np.sin(at_x1)], 'ro')
plt.show()