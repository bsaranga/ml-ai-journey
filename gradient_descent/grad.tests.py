import unittest
import numpy as np
import pandas as pd

from gradient_descent import grad as g

path = '/home/bsaranga/repos/ml-ai-journey/linear-regression/data/tvmarketing.csv'
adv = pd.read_csv(path)

X = adv['TV']
Y = adv['Sales']

X_norm = (X - np.mean(X))/np.std(X)
Y_norm = (Y - np.mean(Y))/np.std(Y)

# Cost function
def E(m, b, X, Y):
    return (1/(2*len(Y))) * np.sum((m*X + b - Y)**2)

class test_generic_partial_derivative_fn_against_sample_data(unittest.TestCase):
    
    def test_pd_fn_1(self):
        self.assertEqual(g.partialDerivative(E, [0,0,X_norm,Y_norm], 0), -0.782224)
    
    def test_pd_fn_1(self):
        self.assertEqual(g.partialDerivative(E, [0,0,X_norm,Y_norm], 1), 0.0)

    def test_pd_fn_1(self):
        self.assertEqual(g.partialDerivative(E, [1,5,X_norm,Y_norm], 0), 0.217776)

    def test_pd_fn_1(self):
        self.assertEqual(g.partialDerivative(E, [1,5,X_norm,Y_norm], 1), 5.0)

if __name__ == '__main__':
    unittest.main()