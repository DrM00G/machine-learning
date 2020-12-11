# import sys
# sys.path.append('src')
# from Matrix import Matrix
import sys
sys.path.append('src')
from Riley_matrix import Matrix
from polynonomial_regression import polynomial_regressor


sandwich_data  = Matrix(elements = [[1,0,0],[1,1,0],[1,2,0],[1,4,0],[0,6,0],[0,0,2],[0,0,4],[0,0,6],[0,0,8]])
sandwich_results = Matrix(elements = [[1],[2],[4],[8],[9],[2],[5],[7],[6]])

def regress(Inputs,Results):
    x_tpose = Inputs.transpose()
    return ((x_tpose @ Inputs).inverse() @ (x_tpose @ Results)).elements

betas = regress(sandwich_data,sandwich_results)
rating = str(betas[0][0]) +" + "+ str(betas[1][0])+" * (slices of beef) "+ str(betas[2][0])+" * (tbsp peanut butter)"
print("\n Formula for rating of sandwich:")
print("\n   "+str(rating))
def evaluate(coefficients,coords):
    return coefficients[0]+coefficients[1]*coords[0]+coefficients[2]*coords[1]
print("\n Rating of Sandwich with 5 slices Roast Beef and 0 Tablespoons Peanut Butter:")
print("\n   Rating: "+str(evaluate([betas[0][0],betas[1][0],betas[2][0]],[5,0])))
print("\n Rating of Sandwich with 5 slices Roast Beef and 5 Tablespoons Peanut Butter:")
print("\n  Rating: "+str(evaluate([betas[0][0],betas[1][0],betas[2][0]],[5,5])))