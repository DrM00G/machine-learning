from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor(LinearRegressor):

    def __init__(self, data_class, prediction_column, max_value,delta,constant = True):
        super().__init__(data_class, prediction_column)
        self.prediction = prediction_column
        self.current_input = None
        self.max_val = max_value
        self.original_data = DataFrame.from_array(data_class.to_array(),data_class.columns)
        print("#0"+str(self.original_data.to_array()))
        self.original_data = self.original_data.append_columns({'constant':[1 for _ in range(len(data_class.to_array()))]},['constant']+data_class.columns)
        self.data = data_class.apply(self.prediction_column, lambda x: self.set_bound_replacements(delta,x))
        if constant:
            self.data = self.data.append_columns({'constant':[1 for _ in range(len(self.data.to_array()))]},['constant']+self.data.columns)
        self.multipliers = self.solve_coefficients()
        print("#1"+str(self.multipliers))
        print("#2"+str(self.original_data.to_array()))

    def set_coefficients(self,coeff):
        self.multipliers=coeff

    def set_bound_replacements(self,delta,x):
        if x == 0:
            return math.log((self.max_val/(delta)) - 1)
        elif x == self.max_val:
            return math.log((self.max_val/(1-delta)) - 1)
        else:
            print(x)
            return math.log((self.max_val/(x)) - 1)


    def predict(self, input_set, coefficients = None):
        # print("INPUT SET"+str(input_set))
        if coefficients == None:
            coefficients = self.multipliers
        # print("COEFS"+str(coefficients))
        inputs = self.gather_all_inputs(input_set)
        result = self.max_val/(1+(math.exp(sum([input_set[key]*coefficients[key] for key in input_set]))))
        return result


    def get_point_gradient(self,delta):
        gradient = {key:0 for key in self.multipliers}
        # print("Multipliers"+str(self.multipliers))
        for key in self.multipliers:
            forward = dict(self.multipliers)
            forward[key] = self.multipliers[key]+delta
            backward = dict(self.multipliers)
            backward[key] = self.multipliers[key]-delta
            gradient[key] = (self.calc_rss(forward) - self.calc_rss(backward)) / (2 * delta)
        return gradient
    
    def calc_rss(self,coefficients):
        error = []
        for coord in self.original_data.to_array():
            guess = self.predict({self.data.columns[i]:coord[i] for i in range(len(self.multipliers))},coefficients)
            error.append(coord[-1]-guess)
        return sum([x**2 for x in error])

    def calc_gradient(self,alpha, delta, num_steps, debug_mode = False):
        for i in range(num_steps):
            gradient = self.get_point_gradient(delta)
            print("#3"+str(gradient))
            coefficients = {key:self.multipliers[key] for key in self.multipliers}
            for key in self.multipliers:
                self.multipliers[key] = coefficients[key] - (alpha * gradient[key])
            if debug_mode:
                print('step '+str(i))
                # print('\tgradient: '+str(gradient))
                # print('\tcoeffs: '+str(self.multipliers))
                # print('\trss: '+str(self.calc_rss(self.multipliers)))
                print('\n')


    
        
