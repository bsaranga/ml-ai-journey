import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

pi = np.pi
x = np.linspace(0, 2*pi, 100)

plt.figure(figsize=(10,10))
plt.plot(x, np.sin(x), label='linear', color='red')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('sine wave')
plt.legend()
plt.show()