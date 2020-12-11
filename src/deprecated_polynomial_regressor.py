import sys
sys.path.append('src')
from Matrix import Matrix

class polynomial_regressor():

    def __init__(self,degree=1):
        self.deg = degree
        self.coefficients = [0 for i in range(degree + 1)]
        self.data = None

    def ingest_data(self,data):
        self.data = data

    def evaluate(self, num):
        equation = []
        for i in range(len(self.coefficients)):
            equation.append((num**i) * self.coefficients[i])
        return sum(equation)

    def sum_squared_error(self):
        squared_errors = []
        for (x,y) in self.data:
            squared_errors.append((self.evaluate(x) - y)**2)
        return sum(squared_errors)

    def solve_coefficients (self):
        coeff = self.linear_approx(self.data, self.deg).elements
        self.coefficients = []
        for elem in coeff:
            for element in elem:
                self.coefficients.append(element)
        return self.coefficients

    def solve_coefficients_with_inputs(self, x, y):
        coeff = self.approx_with_inputs(x, y).elements
        self.coefficients = []
        for elem in coeff:
            for element in elem:
                self.coefficients.append(element)
        return self.coefficients
  
    def evaluate_with_inputs(self, input):
        evaluation = 0
        for i in range(len(self.coefficients)):
            evaluation += self.coefficients[i] * input[i]
        return evaluation

    def approx_with_inputs(self, x, y):
        x_transpose = x.transpose()
        square = x_transpose.multiply(x)
        inverse = square.inverse_by_minors()
        matr  = x_transpose.multiply(y)
        return inverse.multiply(matr)

    def linear_approx(self,data, deg):
        X = Matrix(shape = (len(data),deg + 1))
        Y = Matrix(shape = (len(data),1))
        for i,(x,y) in enumerate(data):
            X.elements[i] = [x**i for i in range(deg + 1)]
            Y.elements[i] = [y]
        x_transpose = X.transpose()
        square = x_transpose.multiply(X)
        inverse = square.inverse_by_minors()
        matr  = x_transpose.multiply(Y)
        return inverse.multiply(matr)

    # def plot(self):
    #     Title = 'y = {} + {}x + {}x^2'.format(round(self.coeff[0],2), round(self.coeff[1],2), round(self.coeff[2],2))
    #     plot_approximation(self.evaluate, self.coeff[0], self.coeff[1], self.coeff[2], self.data, Title)
