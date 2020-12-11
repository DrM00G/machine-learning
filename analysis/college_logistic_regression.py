import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

data_dict = {
    'percentile': [95, 95, 92, 85, 80, 85, 95, 87, 99, 95],
    'ACT': [33, 34, 35, 30, 36, 29, 36, 31, 36, 32],
    'extracurricular': [1,0,1,1,1,1,1,1,0,0],
    'acceptance': [0.999,0.001,0.999,0.001,0.999,0.001,0.999,0.001,0.999,0.001]
}
df = DataFrame(data_dict, column_order = ['percentile', 'ACT', 'extracurricular'])
# print(df.ordered_dict)
df = df.append_pairwise_interactions()
# print(df.ordered_dict)
df = df.append_columns({
    'constant': [1 for _ in range(len(data_dict['percentile']))],
    'acceptance': [0.999,0.001,0.999,0.001,0.999,0.001,0.999,0.001,0.999,0.001]
})
# print(df.ordered_dict)
df = df.apply('acceptance', lambda x: 0.1 if x==0 else x)
# print(df.ordered_dict)

regressor = LogisticRegressor(df, prediction_column = 'acceptance', max_value = 1)
print(regressor.coefficients)
print("Martha: "+str(regressor.predict({
    'percentile':95,
    'ACT':33,
    'extracurricular':1
})))
print("Jeremy: "+str(regressor.predict({
    'percentile':95,
    'ACT':34,
    'extracurricular':0
})))
print("Alphie: "+str(regressor.predict({
    'percentile':92,
    'ACT':35,
    'extracurricular':1
})))
print("Dennis: "+str(regressor.predict({
    'percentile':85,
    'ACT':30,
    'extracurricular':1
})))
print("Jennifer: "+str(regressor.predict({
    'percentile':80,
    'ACT':36,
    'extracurricular':1
})))
print("Martin: "+str(regressor.predict({
    'percentile':85,
    'ACT':29,
    'extracurricular':1
})))
print("Mary: "+str(regressor.predict({
    'percentile':95,
    'ACT':36,
    'extracurricular':1
})))
print("Dean: "+str(regressor.predict({
    'percentile':87,
    'ACT':31,
    'extracurricular':1
})))
print("Adam: "+str(regressor.predict({
    'percentile':99,
    'ACT':36,
    'extracurricular':0
})))
print("Jeremy: "+str(regressor.predict({
    'percentile':95,
    'ACT':32,
    'extracurricular':0
})))
print("David: "+str(regressor.predict({'percentile':95,'ACT':34,'extracurricular':1})))


