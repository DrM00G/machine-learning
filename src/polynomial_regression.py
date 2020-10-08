from Matrix import Matrix
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

class PolynomialRegressor:
    def __init__(self, degree):
        self.degree = degree
        self.coefficients = [0] * degree

    def evaluate(self, x):
        return sum([self.default_guess[i] * x ** (i) for i in range(0, self.degree)])

    def ingest_data(self, data):
        self.data = data

    def sum_squared_error(self):
        return sum((self.evaluate(x)-y)**2 for x, y in self.data)
    
    def solve_coefficients(self):
        X_data = []
        y_data = []
        for i, n in self.data:
            y_data.append([n])
            X_data.append([1, i, i**2])
        X_matrix = Matrix(elements=X_data)
        y_matrix = Matrix(elements=y_data)
        X_transpose = X_matrix.transpose() 
        X_transpose_times_X = X_transpose @ X_matrix 
        result = X_transpose_times_X.inverse() @ X_transpose @ y_matrix
        print(result.elements)
        for i in result.elements:
            index = result.elements.index(i)
            self.coefficients.append(i[0])

  
    def plot(self):
        x_data, y_data = zip(*self.data)
        y = [self.evaluate(x) for x in x_data]
        plt.scatter(x_data, y_data, zorder=2, color='black')
        x_max, y_max = 20, 20
        plt.xlim(-0.5, x_max-0.5)
        plt.ylim(-0.5, y_max-0.5)
        plt.grid(which='minor')
        plt.title("y = " + ' + '.join(f"{round(coef, 5)}x^{i}" for i,
                                      coef in enumerate(self.coefficients)))
        plt.plot(x_data, y, zorder=1)
        plt.show()