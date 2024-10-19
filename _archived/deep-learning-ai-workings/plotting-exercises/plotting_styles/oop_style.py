import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

pi = np.pi
x = np.linspace(0,2*pi,100)

# OO-style usage
fig, ax = plt.subplots(figsize=(8,8), layout='constrained')

#ax.plot(x, x, label='linear')
#ax.plot(x, x**2, label='quadratic')
#ax.plot(x, x**3, label='cubic')
ax.plot(x, np.sin(x), label='sine')

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('Simple Plot')
ax.legend()

plt.show()