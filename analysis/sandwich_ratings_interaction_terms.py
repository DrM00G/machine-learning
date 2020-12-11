
import sys
sys.path.append('src')
from polynonomial_regression import polynomial_regressor
from Matrix import Matrix

sandwich_data  = Matrix(elements = [[1,0,0],[1,1,0],[1,2,0],[1,4,0],[1,6,0],[1,0,2],[1,0,4],[1,0,6],[1,0,8],[1,2,2],[1,3,4]])
sandwich_ratings = Matrix(elements = [[1],[2],[4],[8],[9],[2],[5],[7],[6],[0],[0]])

sandwich_regressor = polynomial_regressor(2)
sandwich_regressor.solve_coefficients_with_inputs(sandwich_data, sandwich_ratings)

coeffs = sandwich_regressor.coefficients

print('Sandwich Rating Equation:')
print('Rating = ',coeffs[0], ' + ',coeffs[1], 'x (Slices of Beef) +', coeffs[2], 'x (Tbsp of peanut butter)')
print('\n')
rating = sandwich_regressor.evaluate_with_inputs([1,5,5])
print('Predicted Rating With 5,5 of peanut butter and beef:')
print(rating)
print('\n')
print("The company shouldn't trust this yet though because")
print('even thought the rating went down, it probably')
print("should be lower considering common sense with roast")
print("beef and peanut butter. and plus, and plus all the")
print("combinations showed a rating of 0. So I don't trust")
print("the rating.")

sandwich_data  = Matrix(elements = [[1,0,0,0],[1,1,0,0],[1,2,0,0],[1,4,0,0],[1,6,0,0],[1,0,2,0],[1,0,4,0],[1,0,6,0],[1,0,8,0],[1,2,2,4],[1,3,4,12]])
sandwich_ratings = Matrix(elements = [[1],[2],[4],[8],[9],[2],[5],[7],[6],[0],[0]])

sandwich_regressor = polynomial_regressor(2)
sandwich_regressor.solve_coefficients_with_inputs(sandwich_data, sandwich_ratings)

