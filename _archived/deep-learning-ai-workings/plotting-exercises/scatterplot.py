import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

radius_mult = 2000

data = {
    'a': np.arange(50),
    'c': np.random.randint(0,50,50),
    'd': np.abs(np.random.randn(50)) * radius_mult
}

data['b'] = data['a'] + 10 * np.random.randn(50)

fig, ax = plt.subplots(figsize=(10,8), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('Entry A')
ax.set_ylabel('Entry B')

plt.show()