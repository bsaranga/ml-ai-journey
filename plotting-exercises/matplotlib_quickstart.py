import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1,2,3,4],[1,4,2,3])

ax.set_title('Hello World')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')

plt.show()