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
        self.data.ordered_dict[prediction_column] = [math.log((self.max_val/y) - 1) for y in self.data.ordered_dict[prediction_column]]
        self.multipliers = self.solve_coefficients()

    def predict(self, input_dict):
        self.current_input = self.gather_all_inputs(input_dict)
        inputs = [val[0] for val in self.current_input.values()]
        # result = round(self.max_val/(1+ math.exp(sum([inputs[i]*self.self.multipliers[i] for i in range(len(inputs))]))), 5)
        return round(self.max_val/(1+ math.exp(sum([inputs[i]*self.multipliers[i] for i in range(len(inputs))]))), 5)

    def predict(self, input_set):
        inputs = self.gather_all_inputs(input_set)
        result = self.max_val/(1+(math.exp(sum([inputs[key]*self.multipliers[key] for key in inputs]))))
        return result
        
