import sys
sys.path.append('src')
from polynomial_regression import PolynomialRegressor 

def single_variable_function(x):
    return (x-1)**2


def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3


def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4


def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6

data = [(0, 1), (1, 2), (2, 5), (3, 10), (4, 20), (5, 30)]


regressor = PolynomialRegressor(0)
regressor.ingest_data(data)    
regressor.solve_coefficients()
assert regressor == [11.333333333333332], ' should be (-2.0000000000000018, 0.0, 0.0) but was actually '+str(egressor)
