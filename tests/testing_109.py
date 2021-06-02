import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame
import matplotlib.pyplot as plt

list_data=[[1,0],
    [2,0],
    [3,0],
    [2,1],
    [3,1],
    [4,1]]

delta_table=[0.1,0.01,0.001,0.0001]
all_coords = []

for delta_low in delta_table:
    # new_list=[]
    # for pair in list_data:
    #     if pair[1] == 0:
    #         new_list.append([pair[0],delta])
    #     else:
    #         new_list.append([pair[0],1-delta])

    df = DataFrame.from_array(
        list_data,
        columns = ['x', 'y'])

    regressor = LogisticRegressor(df, prediction_column = 'y', max_value = 1,delta=delta_low)

    coords = [[],[]]
    for x in range(20):
        coords[0].append(x/100)
        coords[1].append(regressor.predict({'constant':1,'x':x}))
    all_coords.append(coords)
print(all_coords)
plt.style.use('bmh')
for coords in all_coords:
    plt.plot(coords[0],coords[1],linewidth=2.5)
plt.legend(['0.1','0.01','0.001','0.0001'])
plt.savefig('logistic_regressor_109.png')


# dfgd = DataFrame.from_array(
#     [[1,0],
#     [2,0],
#     [3,0],
#     [2,1],
#     [3,1],
#     [4,1]],
#     columns = ['x', 'y'])

# gd_regressor = LogisticRegressor(dfgd, prediction_column = 'y', max_value = 1,delta=0.01)

# gd_regressor.set_coefficients({'constant': 0.5, 'x': 0.5})


# alpha = 0.01
# delta = 0.01
# num_steps = 20000
# gd_regressor.calc_gradient(alpha, delta, num_steps, debug_mode = False)
# print('reg')
# print('init mults: '+str(gd_regressor.multipliers))
# coords = [[],[]]
# for x in range(20):
#     coords[0].append(x/100)
#     coords[1].append(gd_regressor.predict({'constant':1,'x':x}))

# plt.style.use('bmh')
# plt.plot(coords[0],coords[1],linewidth=2.5)
# plt.legend(['gradient_descent'])
# plt.savefig('gradient_descent_109.png')
# plt.close()