import math, sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor

def transform_polynomial_data(data, degree):
    new_data = [[data[x][0]**i for i in range(degree+1)] + [data[x][1]] for x in range(len(data))]
    data_dict = {}
    for x in range(len(new_data)):
        for y in range(len(new_data[0])):
            if str(y) in data_dict:
                data_dict[str(y)].append(new_data[x][y])
            else:
                data_dict[str(y)] = [new_data[x][y]]
    return data_dict
    
def transform_trigonometric_data(data):
    new_data = [[math.sin(data[x][0]),math.cos(data[x][0]),math.sin(2*(data[x][0])),math.cos(2*(data[x][0]))] + [data[x][1]] for x in range(len(data))]
    data_dict = {}
    for x in range(len(new_data)):
        for y in range(len(new_data[0])):
            if str(y) in data_dict:
                data_dict[str(y)].append(new_data[x][y])
            else:
                data_dict[str(y)] = [new_data[x][y]]
    return data_dict

polynomial_data = [(0.0, 4.0),
 (0.2, 8.9),
 (0.4, 17.2),
 (0.6, 28.3),
 (0.8, 41.6),
 (1.0, 56.5),
 (1.2, 72.4),
 (1.4, 88.7),
 (1.6, 104.8),
 (1.8, 120.1),
 (2.0, 134.0),
 (2.2, 145.9),
 (2.4, 155.2),
 (2.6, 161.3),
 (2.8, 163.6),
 (3.0, 161.5),
 (3.2, 154.4),
 (3.4, 141.7),
 (3.6, 122.8),
 (3.8, 97.1),
 (4.0, 64.0),
 (4.2, 22.9),
 (4.4, -26.8),
 (4.6, -85.7),
 (4.8, -154.4)]

trigonometry_data = [(0.0, 7.0),
 (0.2, 5.6),
 (0.4, 3.56),
 (0.6, 1.23),
 (0.8, -1.03),
 (1.0, -2.89),
 (1.2, -4.06),
 (1.4, -4.39),
 (1.6, -3.88),
 (1.8, -2.64),
 (2.0, -0.92),
 (2.2, 0.95),
 (2.4, 2.63),
 (2.6, 3.79),
 (2.8, 4.22),
 (3.0, 3.8),
 (3.2, 2.56),
 (3.4, 0.68),
 (3.6, -1.58),
 (3.8, -3.84),
 (4.0, -5.76),
 (4.2, -7.01),
 (4.4, -7.38),
 (4.6, -6.76),
 (4.8, -5.22)]


data_dict = transform_polynomial_data(polynomial_data,3)
df = DataFrame(data_dict)
regression = LinearRegressor(df,"4")
print("polynomial_data"+str(regression.coefficients))


data_dict = transform_trigonometric_data(trigonometry_data)
df = DataFrame(data_dict)
regression = LinearRegressor(df,"4")
print("trigonometry_data"+str(regression.coefficients))