import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
from node import Node
from random_forest import RandomForest


data =[
["M", 159, 130, 22.02, 18.14],
["M", 214, 190, 19.70, 17.44],
["M", 163, 152, 24.09, 22.43],
["M", 205, 194, 26.97, 25.57],
["F", 150, 141, 21.51, 20.10],
["M", 130, 121, 18.69, 17.40],
["F", 141, 132, 24.24, 22.88],
["F", 123, 117, 21.23, 20.23],
["F", 154, 150, 30.26, 29.24],
["F", 128, 123, 21.88, 21.02],
["F", 110, 104, 17.63, 16.89],
["M", 156, 152, 24.57, 23.85],
["M", 148, 145, 20.68, 20.15],
["F", 123, 121, 20.97, 20.36],
["F", 154, 150, 27.30, 26.73],
["F", 134, 132, 23.30, 22.88],
["F", 117, 115, 19.48, 19.24],
["M", 203, 203, 24.74, 24.69],
["F", 126, 128, 20.69, 20.79],
["M", 148, 148, 20.49, 20.60],
["F", 128, 128, 21.09, 21.24],
["F", 108, 110, 18.37, 18.53],
["M", 150, 150, 22.40, 22.61],
["F", 152, 152, 28.17, 28.43],
["M", 192, 194, 23.60, 23.81],
["M", 179, 181, 26.52, 26.78],
["M", 132, 134, 18.89, 19.27],
["F", 115, 117, 19.31, 19.75],
["M", 154, 156, 20.96, 21.32],
["F", 139, 141, 21.78, 22.22],
["F", 123, 126, 19.78, 20.23],
["M", 150, 152, 22.40, 22.82],
["M", 150, 152, 22.76, 23.19],
["F", 119, 123, 20.15, 20.69],
["M", 176, 181, 22.14, 22.57],
["M", 141, 145, 20.27, 20.76],
["F", 126, 130, 22.15, 22.93],
["F", 139, 143, 23.87, 24.67],
["F", 119, 123, 18.61, 19.34],
["F", 123, 128, 21.73, 22.58],
["M", 119, 123, 18.93, 19.72],
["M", 161, 165, 25.88, 26.72],
["M", 170, 174, 28.59, 29.53],
["F", 139, 145, 21.89, 22.79],
["F", 112, 119, 18.31, 19.28],
["F", 130, 137, 19.64, 20.63],
["F", 143, 150, 23.02, 24.10],
["F", 117, 123, 20.63, 21.91],
["F", 137, 143, 22.61, 23.81],
["F", 121, 128, 22.03, 23.42],
["M", 163, 170, 20.31, 21.34],
["M", 163, 172, 20.31, 21.36],
["M", 141, 150, 19.59, 20.77],
["M", 141, 150, 21.05, 22.31],
["F", 126, 134, 23.47, 25.11],
["F", 141, 150, 22.84, 24.29],
["F", 132, 141, 19.50, 20.90],
["M", 141, 150, 18.51, 19.83],
["M", 145, 156, 21.40, 22.97],
["F", 115, 126, 17.72, 19.42],
["M", 156, 170, 22.26, 23.87],
["F", 121, 132, 21.64, 23.81],
["M", 143, 156, 22.51, 24.45],
["M", 165, 181, 23.69, 25.80],
["F",  93, 108, 15.08, 17.74],
["M", 163, 181, 22.64, 25.33],
["M", 207, 231, 36.57, 40.86]]

df = DataFrame.from_array(data, columns = ["class", "y", "Weight_Apr", "x", "BMI_Apr"])
df = df.remove_columns(["Weight_Apr", "BMI_Apr"])
df = df.swap_columns(0,2)
df = df.append_columns({'node_index':[i for i in range(len(df.to_array()))]})
print(df.columns)


def make_training_sets(data, num_sets):
    training_sets = []
    testing_sets = []
    break_point = len(data.to_array())//num_sets
    for i in range(num_sets):
        sets = [[],[]]
        for j in range(len(data.to_array())):
            if j > (i*break_point) and j <= (i*break_point + break_point):
                sets[1].append(data.to_array()[j])
            else:
                sets[0].append(data.to_array()[j])
        training_sets.append(DataFrame.from_array(sets[0],data.columns))
        testing_sets.append(DataFrame.from_array(sets[1],data.columns))
    print('splits finished')
    return [training_sets, testing_sets]

sets = make_training_sets(df, 5)


for i in range(len(sets[0])):
    total = 0
    correct = 0
    print("testing0")
    dt = DecisionTree('gini')
    print(sets[0][i].to_array())
    dt.fit(sets[0][i])
    print("testing0.2")
    

        