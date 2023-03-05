import matplotlib.pyplot as plt
import numpy as np

def gradient_at(val, fn):
    epsilon = 0.0000001
    precision = np.log10(1/epsilon).astype(int) - 1
    grad = (fn(val + epsilon) - fn(val))/epsilon
    return np.round(grad, precision)

def plot_grad_line_at(val, fn):
    l_width = 2
    
    def lineFn(var):
        grad = gradient_at(val, fn).astype(float)
        return grad*(var - val) + fn(val)
    
    plt.plot([val], [fn(val)], 'o')
    plt.plot([val - l_width, val + l_width], [lineFn(val - l_width), lineFn(val + l_width)])

def gradient_descent(init, l_rate, fn, threshold=0.0000001):
    '''
    Returns the minimum point and the path taken by the gradient
    descent process
    '''
    x = init
    path = [x]
    _iter = 0
    while abs(gradient_at(x, fn)) > threshold:
        x = x - l_rate * gradient_at(x, fn)
        path.append(x)
        _iter += 1
    print(f'Iterations = {_iter}')
    return [x, np.array(path)]


# Test function
def basic_quad(x):
    return (x-3.557)**2 + 1.5568

desc = gradient_descent(15, .1, basic_quad)
print(f'Minimum is at {desc[0]}')

x = np.linspace(start=-5, stop=15)
plt.figure(figsize=[8,8])
plt.plot(x, basic_quad(x))
for i in desc[1]:
    plt.plot(i, basic_quad(i), 'ro')

plt.show()