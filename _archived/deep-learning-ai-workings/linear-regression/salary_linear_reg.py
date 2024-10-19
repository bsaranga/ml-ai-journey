import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from gradient_descent import grad as g

path = '/home/bsaranga/repos/ml-ai-journey/linear-regression/data/Salary_Data.csv'
adv = pd.read_csv(path)

X = adv['YearsExperience']
Y = adv['Salary']

X_norm = (X - np.mean(X))/np.std(X)
Y_norm = (Y - np.mean(Y))/np.std(Y)


# Cost function
def E(m, b, X, Y):
    return (1/(2*len(Y))) * np.sum((m*X + b - Y)**2)

result, path = g.gradient_descent3([0,0,X_norm,Y_norm], 1, E, [0,1])
m = result[0]
b = result[1]

plt.scatter(X_norm, Y_norm)
plt.plot(X_norm, m*X_norm + b, color='red')
plt.show()