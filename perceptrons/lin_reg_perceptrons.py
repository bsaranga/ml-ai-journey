import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.random.seed(3)

path = '/home/bsaranga/repos/ml-ai-journey/perceptrons/data/tvmarketing.csv'
adv = pd.read_csv(path)

# General methodology to build a neural network
# 1. Define the structure of the neural network (no. of inputs, no.of hidden units, etc)
# 2. Initialize the model's parameters
# 3. Loop:
#   - Implement Forward Propagation (calculate the perceptron's output)
#   - Implement Backward Propagation (to get the required corrections for the parameters)
#   - Update parameters
# 4. Make predictions

adv_norm = (adv - adv.mean())/np.std(adv)
X_norm, Y_norm = adv_norm['TV'], adv_norm['Sales']

X_norm = np.array(X_norm).reshape((1, len(X_norm)))
Y_norm = np.array(Y_norm).reshape((1, len(Y_norm)))

def layer_sizes(X, Y):
    return (X.shape[0], Y.shape[0])

def initialize_parameters(n_x, n_y):
    W = np.random.randn(n_y, n_x) * 0.01
    b = np.zeros((n_y, 1))
    return {
        "W": W,
        "b": b
    }

def forward_propagation(X, parameters):
    W = parameters["W"]
    b = parameters["b"]
    return np.matmul(W, X) + b

def compute_cost(Y_hat, Y):
    m = Y_hat.shape[1]
    return np.sum((Y_hat - Y)**2)/(2*m)

def backward_propagation(Y_hat, X, Y):
    m = X.shape[1]
    dZ = Y_hat - Y
    dW = 1/m * np.dot(dZ, X.T)
    db = 1/m * np.sum(dZ, axis=1, keepdims=True)
    return {
        "dW": dW,
        "db": db
    }

def update_parameters(parameters, grads, learning_rate=1.2):
    W = parameters["W"]
    b = parameters["b"]

    dW = grads["dW"]
    db = grads["db"]

    W = W - learning_rate * dW
    b = b - learning_rate * db

    return {
        "W": W,
        "b": b
    }

def nn_model(X, Y, iterations=10, learning_rate=1.2, print_cost=False):
    nx, ny = layer_sizes(X_norm, Y_norm)
    parameters = initialize_parameters(nx, ny)

    for i in range(0, iterations):
        Y_hat = forward_propagation(X, parameters)
        cost = compute_cost(Y_hat, Y)
        grads = backward_propagation(Y_hat, X, Y)
        parameters = update_parameters(parameters, grads, learning_rate)
        if (print_cost):
            print("Cost at iteration %i: %f" %(i, cost))
    
    return parameters

out = nn_model(X_norm, Y_norm, 10, learning_rate=.8, print_cost=True)

print(out["W"])
print(out["b"])