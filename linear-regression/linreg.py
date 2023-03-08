import numpy as np
# A library for programmatic plot generation.
import matplotlib.pyplot as plt
# A library for data manipulation and analysis.
import pandas as pd

path = '/home/bsaranga/repos/ml-ai-journey/linear-regression/data/tvmarketing.csv'
adv = pd.read_csv(path)

X = adv['TV']
Y = adv['Sales']

X_norm = (X - np.mean(X))/np.std(X)
Y_norm = (Y - np.mean(Y))/np.std(Y)

# Cost function
def E(m, b, X, Y):
    return (1/(2*len(Y))) * np.sum((m*X + b - Y)**2)