from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor(LinearRegressor):

    def __init__(self, data_class, prediction_column, max_value):
        super().__init__(data_class, prediction_column)
        self.data = data_class
        self.prediction = prediction_column
        self.current_input = None
        self.max_val = max_value
        # self.data.ordered_dict[prediction_column] = [math.log((self.max_val/y) - 1) for y in self.data.ordered_dict[prediction_column]]
        self.multipliers = self.solve_coefficients()

    def set_coefficients(self,coeff):
        self.multipliers=coeff

    def predict(self, input_set, coefficients = None):
        print("INPUT SET"+str(input_set))
        if coefficients == None:
            coefficients = self.multipliers
        print("COEFS"+str(coefficients))
        inputs = self.gather_all_inputs(input_set)
        result = self.max_val/(1+(math.exp(sum([input_set[key]*coefficients[key] for key in input_set if key!='constant']))))
        return result


    def get_point_gradient(self,delta):
        gradient = {key:0 for key in self.multipliers}
        for key in self.multipliers:
            forward = dict(self.multipliers)
            forward[key] = self.multipliers[key]+delta
            backward = dict(self.multipliers)
            backward[key] = self.multipliers[key]-delta
            gradient[key] = (self.calc_rss(forward) - self.calc_rss(backward)) / (2 * delta)
        return gradient
    
    def calc_rss(self,coefficients):
        error = []
        for coord in self.data.to_array():
            guess = self.predict({self.data.columns[i]:coord[i] for i in range(len(self.multipliers))},coefficients)
            error.append(coord[-1]-guess)

    def calc_gradient(self,alpha, delta, num_steps, debug_mode = False):
        for i in range(num_steps):
            gradient = self.get_point_gradient(delta)
            coefficients = {key:self.multipliers[key] for key in self.multipliers}
            for key in self.multipliers:
                self.multipliers[key] = coefficients[key] - (alpha * gradient[key])
            if debug_mode:
                print('step '+str(_))
                print('\tgradient: '+str(gradient))
                print('\tcoeffs: '+str(self.multipliers))
                print('\trss: '+str(self.calc_rss(self.multipliers)))
                
                print('\n')


    
        
