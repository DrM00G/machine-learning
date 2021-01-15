import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
from node import Node
from random_forest import RandomForest

path_to_datasets = '/home/runner/machine-learning1/datasets/'
filename="freshman_lbs.csv"
filepath =path_to_datasets+filename

df = DataFrame.from_csv(filepath)
df = df.remove_columns(["Weight (lbs, Apr)", "BMI (Apr)"])
df = df.swap_columns(0,2)
df = df.append_columns({'node_index':[i for i in range(len(df.to_array()))]})
print(df.columns)


def make_training_sets(data, num_sets):
    training_sets = []
    testing_sets = []
    break_point = len(data.to_array())
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

# sets = make_training_sets(df, 5)


# for i in range(len(sets[0])):
#     total = 0
#     correct = 0
#     print("testing0")
#     dt = DecisionTree('gini')
#     print(sets[0][i].to_array())
#     dt.fit(sets[0][i])
#     print("testing0.2")
    

        
