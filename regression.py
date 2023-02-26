import numpy as np
import matplotlib.pyplot as plt
# A function to create a dataset.
from sklearn.datasets import make_regression
# A library for data manipulation and analysis.
import pandas as pd
# Some functions defined specifically for this notebook.
import w3_tools

import w3_unittest

# Set a seed so that the results are consistent.
np.random.seed(3)

m = 30

X, Y = make_regression(n_samples=m, n_features=1, noise=20, random_state=1)

X = X.reshape((1, m))
Y = Y.reshape((1, m))

#Plotting
""" 
plt.scatter(X,  Y, c="black")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show() """

# Shape of variable X.
shape_X = X.shape
# Shape of variable Y.
shape_Y = Y.shape
# Training set size.
m = X.size

w3_unittest.test_shapes(shape_X, shape_Y, m)

def layer_sizes(X, Y):
    """
    Arguments:
    X -- input dataset of shape (input size, number of examples)
    Y -- labels of shape (output size, number of examples)
    
    Returns:
    n_x -- the size of the input layer
    n_y -- the size of the output layer
    """
    ### START CODE HERE ### (~ 2 lines of code)
    # Size of input layer.
    n_x = X.shape[0]
    # Size of output layer.
    n_y = Y.shape[0]
    ### END CODE HERE ###
    return (n_x, n_y)

w3_unittest.test_layer_sizes(layer_sizes)

def initialize_parameters(n_x, n_y):
    """
    Returns:
    params -- python dictionary containing your parameters:
                    W -- weight matrix of shape (n_y, n_x)
                    b -- bias value set as a vector of shape (n_y, 1)
    """
    
    ### START CODE HERE ### (~ 2 lines of code)
    W = np.random.randn(n_y, n_x) * 0.01
    b = np.zeros((n_y, 1))
    ### END CODE HERE ###
    
    assert (W.shape == (n_y, n_x))
    assert (b.shape == (n_y, 1))
    
    parameters = {"W": W,
                  "b": b}
    
    return parameters

init_params = initialize_parameters(layer_sizes(X,Y)[0], layer_sizes(X,Y)[1])
print(init_params['W'])
print(init_params['b'])