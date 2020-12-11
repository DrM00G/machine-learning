import sys
sys.path.append('src')
from polynonomial_regression import polynomial_regressor

data = [(1, 3.1), (2, 10.17), (3, 20.93), (4, 38.71), (5, 60.91), (6, 98.87), (7, 113.92), (8, 146.95), (9, 190.09), (10, 232.65)]

constant_regressor = polynomial_regressor(degree=2)
constant_regressor.ingest_data(data)
constant_regressor.solve_coefficients()
print()
print("Drgree 2")
print("Coefficents: "+str(constant_regressor.coefficients))
print()
print("Aprox pos: "+str(constant_regressor.evaluate(200)))
print()

print("eRROR: "+str(constant_regressor.sum_squared_error()))
print()


constant_regressor = polynomial_regressor(degree=3)
constant_regressor.ingest_data(data)
constant_regressor.solve_coefficients()
print()
print("Drgree 3")
print("Coefficents: "+str(constant_regressor.coefficients))
print()
print("Aprox pos: "+str(constant_regressor.evaluate(200)))
print()

print("eRROR: "+str(constant_regressor.sum_squared_error()))
print()