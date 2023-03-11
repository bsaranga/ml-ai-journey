import numpy as np
import matplotlib.pyplot as plt

def gradient_at(val, fn):
    epsilon = 0.0000001
    precision = np.log10(1/epsilon).astype(int) - 1
    grad = (fn(val + epsilon) - fn(val))/epsilon
    return np.round(grad, precision)

def dfdX(val, f):
    epsilon = 0.0000001
    precision = np.log10(1/epsilon).astype(int) - 1
    grad = (f(val[0] + epsilon, val[1]) - f(val[0], val[1]))/epsilon
    return np.round(grad, precision)

def dfdY(val, f):
    epsilon = 0.0000001
    precision = np.log10(1/epsilon).astype(int) - 1
    grad = (f(val[0], val[1] + epsilon) - f(val[0], val[1]))/epsilon
    return np.round(grad, precision)

def partialDerivative(f, vals, index=0):
    epsilon = 0.0000001
    grad = None
    if (index == 0):
        grad = (f(vals[0] + epsilon, *vals[1:]) - f(*vals))/epsilon
    elif (index == len(vals) - 1):
        grad = (f(*vals[:-1], vals[-1] + epsilon) - f(*vals))/epsilon
    else:
        grad = (f(*vals[:index], vals[index] + epsilon, *vals[index+1:]) - f(*vals))/epsilon
    if (grad != None):
        return grad
    else: return None

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

def gradient_descent2(init, l_rate, fn, threshold=0.0000001):
    x = init[0]
    y = init[1]
    path = [[x,y]]
    _iter = 0

    while (abs(dfdX([x,y], fn)) > threshold and abs(dfdY([x,y], fn)) > threshold):
        x = x - l_rate * dfdX([x,y], fn)
        y = y - l_rate * dfdY([x,y], fn)
        path.append([x,y])
        _iter += 1
    print(f'Iterations = {_iter}')
    return [[x,y], np.array(path)]


def gradient_descent3(init, l_rate, fn, indices=[0,1], threshold=0.0000001**2):
    PDparams = [init[indices[0]], init[indices[1]]]
    PDparams.extend(init[len(indices):])
    path = [[PDparams[0],PDparams[1]]]
    _iter = 0

    while (abs(partialDerivative(fn, PDparams, indices[0])) > threshold and abs(partialDerivative(fn, PDparams, indices[1])) > threshold):
        PDparams[0] = PDparams[0] - l_rate * partialDerivative(fn, PDparams, indices[0])
        PDparams[1] = PDparams[1] - l_rate * partialDerivative(fn, PDparams, indices[1])
        path.append([PDparams[0],PDparams[1]])
        _iter += 1
        
    print(f'Iterations = {_iter}')
    return [[PDparams[0],PDparams[1]], np.array(path)]