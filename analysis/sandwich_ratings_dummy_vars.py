import sys
sys.path.append('src')
from polynonomial_regression import polynomial_regressor
from Matrix import Matrix


# B = roast beef
# P = peanut butter
# M = Mayo
# J = jelly
# R = rating
sandwich_data = Matrix(elements = [[1, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0],
 [1, 0, 0, 1, 0,  0,  0,  0,  0,  0,  0],
 [1, 0, 0, 0, 1,  0,  0,  0,  0,  0,  0],
 [1, 0, 0, 1, 1,  0,  0,  0,  0,  0,  1],
 [1, 5, 0, 0, 0,  0,  0,  0,  0,  0,  0],
 [1, 5, 0, 1, 0,  0,  5,  0,  0,  0,  0],
 [1, 5, 0, 0, 1,  0,  0,  5,  0,  0,  0],
 [1, 5, 0, 1, 1,  0,  5,  5,  0,  0,  1],
 [1, 0, 5, 0, 0,  0,  0,  0,  0,  0,  0],
 [1, 0, 5, 1, 0,  0,  0,  0,  5,  0,  0],
 [1, 0, 5, 0, 1,  0,  0,  0,  0,  5,  0],
 [1, 0, 5, 1, 1,  0,  0,  0,  5,  5,  1],
 [1, 5, 5, 0, 0, 25,  0,  0,  0,  0,  0],
 [1, 5, 5, 1, 0, 25,  5,  0,  5,  0,  0],
 [1, 5, 5, 0, 1, 25,  0,  5,  0,  5,  0],
 [1, 5, 5, 1, 1, 25,  5,  5,  5,  5,  1]])

ratings = Matrix(elements = [[1], [1], [4], [0], [4], [8], [1], [0], [5], [0], [9], [0],[0], [0], [0], [0]])

sandwich_regressor = polynomial_regressor(10)
print("1")
sandwich_regressor.solve_coefficients_with_inputs(sandwich_data, ratings)
print("1")
coeffs = sandwich_regressor.coefficients
print("1")
coeffs = [round(coeffs[i], 5) for i in range(len(coeffs))]
print("1")


terms = ['Bias Term', 'Beef Slices', 'Peanut Butter', 'Mayo', 'Jelly', 'Beef & PB', 'Beef & Mayo', 'Beef & Jelly',
'PB & Mayo', 'PB & Jelly', 'Mayo & Jelly']

print('Sandwich Rating Equations:')
equation_string = 'Rating ='

for i in range(len(coeffs)):
    equation_string += ' '
    if i > 0:
        equation_string += '+ '
    equation_string += str(coeffs[i])
    equation_string += ' * ('+ terms[i]+')'


print()
print(equation_string)