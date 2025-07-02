#%matplotlib ipympl
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate synthetic data with wider x distribution
np.random.seed(42)
m = 100
X = np.random.uniform(-5, 5, m)
true_w = 3
true_b = 2
noise = np.random.randn(m) * 1.0
y = true_w * X + true_b + noise

# 2. Create tighter meshgrid around true_w, true_b
w_vals = np.linspace(1, 5, 100)
b_vals = np.linspace(-4, 10, 100)
W, B = np.meshgrid(w_vals, b_vals)

# 3. Compute cost
J_vals = np.zeros_like(W)
for i in range(W.shape[0]):
    for j in range(W.shape[1]):
        w = W[i, j]
        b = B[i, j]
        predictions = w * X + b
        J_vals[i, j] = (1 / (2 * m)) * np.sum((predictions - y) ** 2)

# 4. Plot true bowl
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(W, B, J_vals, cmap='viridis', edgecolor='k', alpha=0.95)
ax.set_xlabel('w')
ax.set_ylabel('b')
ax.set_zlabel('Cost J(w, b)')
ax.set_title('True Bowl-Shaped Cost Function')
plt.show()
