import matplotlib.pyplot as plt
import numpy as np

def gradient_at(val, fn):
    epsilon = 0.000001
    precision = np.log10(1/epsilon).astype(int) - 1
    grad = (fn(val + epsilon) - fn(val))/epsilon
    return np.round(grad, precision)

def plot_grad_line_at(val, fn):
    l_width = 2
    
    def lineFn(var):
        grad = gradient_at(val, fn).astype(float)
        print(grad)
        return grad*var + fn(var)
    
    plt.plot([val], [fn(val)], 'ro')
    plt.plot([val - l_width, val + l_width], [lineFn(val - l_width), lineFn(val + l_width)])



def basic_quad(x):
    return (x-2.5)**2 + 1

x = np.linspace(start=-5, stop=15)

plt.figure(figsize=[8,8])

plt.plot(x, basic_quad(x))

plot_grad_line_at(2.4, basic_quad)

plt.show()