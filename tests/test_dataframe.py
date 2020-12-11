import sys
sys.path.append('src')
from dataframe import DataFrame

# # data_dict = {
# #     'Pete': [1, 0, 1, 0],
# #     'John': [2, 1, 0, 2],
# #     'Sara': [3, 1, 4, 0]
# # }

# # df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sara'])
# # print(df1.ordered_dict)
# # # {
# # #     'Pete': [1, 0, 1, 0],
# # #     'John': [2, 1, 0, 2],
# # #     'Sara': [3, 1, 4, 0]
# # # }

# # print(df1.to_array())
# # # [[1, 2, 3]
# # #  [0, 1, 1]
# # #  [1, 0, 4]
# # #  [0, 2, 0]]

# # print(df1.columns)
# # #['Pete', 'John', 'Sara']

# # # df2 = df1.filter_columns(['Sara', 'Pete'])
# # # print(df2.to_array())
# # # # [[3, 1],
# # # #  [1, 0],
# # # #  [4, 1],
# # # #  [0, 0]]

# # # print(df2.columns)
# # # # ['Sara', 'Pete']

# # # def multiply_by_4(x):
# # #         return 4*x

# # # df2 = df1.apply('John', multiply_by_4)
# # # print(df2.to_array())

# # # [[1, 8, 3]
# # #  [0, 4, 1]
# # #  [1, 0, 4]
# # #  [0, 8, 0]]

# # df2 = df1.append_pairwise_interactions()
# # print(df2.columns)
# # print(df2.to_array())
# # #['Pete', 'John', 'Sarah', 'Pete_John', 'Pete_Sarah', 'John_Sarah']

# # data_dict = {
# #     'id': [1, 2, 3, 4],
# #     'color': ['blue', 'yellow', 'green', 'yellow']
# # }

# # df3 = DataFrame(data_dict, column_order = ['id', 'color'])
# # df4 = df3.create_dummy_variables()
# # print(df4.columns)
# # #['id', 'color_blue', 'color_yellow', 'color_green']
# # print(df4.to_array())
# # #[[1, 1, 0, 0]
# # # [2, 0, 1, 0]
# # # [3, 0, 0, 1]
# # # [4, 0, 1, 0]]

# # df6 = df4.remove_columns(['id', 'color_yellow'])
# # print(df6.columns)
# # #['color_blue', 'color_green']
# # print(df6.to_array())
# # #[[1, 0]
# # # [0, 0]
# # # [0, 1]
# # # [0, 0]]

# # df7 = df6.append_columns({
# #     'name': ['Anna', 'Bill', 'Cayden', 'Daphnie'],
# #     'letter': ['a', 'b', 'c', 'd']
# # })
# # print(df7.columns)
# # #['color_blue', 'color_green', 'name', 'letter']
# # print(df7.to_array())
# # #[[1, 0, 'Anna', 'a']
# # # [0, 0, 'Bill', 'b']
# # # [0, 1, 'Cayden', 'c']
# # # [0, 0, 'Daphnie', 'd']]

# # data_dict = {
# #     'beef': [0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5],
# #     'pb': [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
# #     'condiments': [[],['mayo'],['jelly'],['mayo','jelly'],
# #                    [],['mayo'],['jelly'],['mayo','jelly'],
# #                    [],['mayo'],['jelly'],['mayo','jelly'],
# #                    [],['mayo'],['jelly'],['mayo','jelly']],
# #     'rating': [1, 1, 4, 0, 4, 8, 1, 0, 5, 0, 9, 0, 0, 0, 0, 0]
# # }
# # df = DataFrame(data_dict, column_order = ['beef', 'pb', 'condiments'])
# # print("test 1")
# # assert df.columns == ['beef', 'pb', 'condiments'],'Incorrect columns'
# # print("passed")
# # # ['beef', 'pb', 'condiments']
# # print()
# # print("test 2")
# # assert df.to_array() ==    [[ 0,  0,  []],[ 0,  0,  ['mayo']],[ 0,  0,  ['jelly']],[ 0,  0,  ['mayo','jelly']],[ 5,  0,  []],[ 5,  0,  ['mayo']],[ 5,  0,  ['jelly']],[ 5,  0,  ['mayo','jelly']],[ 0,  5,  []],[ 0,  5,  ['mayo']],[ 0,  5,  ['jelly']],[ 0,  5,  ['mayo','jelly']],[ 5,  5,  []],[ 5,  5,  ['mayo']],[ 5,  5,  ['jelly']],[ 5,  5,  ['mayo','jelly']]],'Incorrect Matrix data'
# # print("passed")
#   #  [[ 0,  0,  []],
#   #   [ 0,  0,  ['mayo']],
#   #   [ 0,  0,  ['jelly']],
#   #   [ 0,  0,  ['mayo','jelly']],
#   #   [ 5,  0,  []],
#   #   [ 5,  0,  ['mayo']],
#   #   [ 5,  0,  ['jelly']],
#   #   [ 5,  0,  ['mayo','jelly']],
#   #   [ 0,  5,  []],
#   #   [ 0,  5,  ['mayo']],
#   #   [ 0,  5,  ['jelly']],
#   #   [ 0,  5,  ['mayo','jelly']],
#   #   [ 5,  5,  []],
#   #   [ 5,  5,  ['mayo']],
#   #   [ 5,  5,  ['jelly']],
#   #   [ 5,  5,  ['mayo','jelly']]]

# df = df.create_dummy_variables()


# print()
# print("test 3")
# assert df.columns == ['beef', 'pb', 'mayo', 'jelly'],'Incorrect columns, is acualy '+str(df.columns)+'.'
# #not sure why this isnt working
# print("passed")
# # ['beef', 'pb', 'mayo', 'jelly']
# # print(df.to_array())
# print()
# print("test 4")
# assert df.to_array() ==    [[ 0,  0,  0,  0],[ 0,  0,  1,  0],[ 0,  0,  0,  1],[ 0,  0,  1,  1],[ 5,  0,  0,  0],[ 5,  0,  1,  0],[ 5,  0,  0,  1],[ 5,  0,  1,  1],[ 0,  5,  0,  0],[ 0,  5,  1,  0],[ 0,  5,  0,  1],[ 0,  5,  1,  1],[ 5,  5,  0,  0],[ 5,  5,  1,  0],[ 5,  5,  0,  1],[ 5,  5,  1,  1]],'Incorrect Matrix data'
# print("passed")
#   #  [[ 0,  0,  0,  0],
#   #   [ 0,  0,  1,  0],
#   #   [ 0,  0,  0,  1],
#   #   [ 0,  0,  1,  1],
#   #   [ 5,  0,  0,  0],
#   #   [ 5,  0,  1,  0],
#   #   [ 5,  0,  0,  1],
#   #   [ 5,  0,  1,  1],
#   #   [ 0,  5,  0,  0],
#   #   [ 0,  5,  1,  0],
#   #   [ 0,  5,  0,  1],
#   #   [ 0,  5,  1,  1],
#   #   [ 5,  5,  0,  0],
#   #   [ 5,  5,  1,  0],
#   #   [ 5,  5,  0,  1],
#   #   [ 5,  5,  1,  1]]

# df = df.append_pairwise_interactions()
# print()
# print("test 5")
# assert df.columns == ['beef', 'pb', 'mayo', 'jelly', 'beef_jelly','pb_beef', 'mayo_pb','jelly_mayo'],'Incorrect columns, is instead '+ str(df.columns)
# print("passed")
# # print(df.columns)
# # ['beef', 'pb', 'mayo', 'jelly',
# #  'beef_pb', 'beef_mayo', 'beef_jelly',
# #  'pb_mayo', 'pb_jelly',
# #  'mayo_jelly']
# # print(df.to_array())
# print()
# print("test 6")
# assert df.to_array() ==   [[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],[ 0,  0,  1,  0,  0,  0,  0,  0,  0,  0],[ 0,  0,  0,  1,  0,  0,  0,  0,  0,  0],[ 0,  0,  1,  1,  0,  0,  0,  0,  0,  1],[ 5,  0,  0,  0,  0,  0,  0,  0,  0,  0],[ 5,  0,  1,  0,  0,  5,  0,  0,  0,  0],[ 5,  0,  0,  1,  0,  0,  5,  0,  0,  0],[ 5,  0,  1,  1,  0,  5,  5,  0,  0,  1],[ 0,  5,  0,  0,  0,  0,  0,  0,  0,  0],[ 0,  5,  1,  0,  0,  0,  0,  5,  0,  0],[ 0,  5,  0,  1,  0,  0,  0,  0,  5,  0],[ 0,  5,  1,  1,  0,  0,  0,  5,  5,  1],[ 5,  5,  0,  0, 25,  0,  0,  0,  0,  0],[ 5,  5,  1,  0, 25,  5,  0,  5,  0,  0],[ 5,  5,  0,  1, 25,  0,  5,  0,  5,  0],[ 5,  5,  1,  1, 25,  5,  5,  5,  5,  1]],'Incorrect Matric data'
# print("passed")
#   #  [[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#   #   [ 0,  0,  1,  0,  0,  0,  0,  0,  0,  0],
#   #   [ 0,  0,  0,  1,  0,  0,  0,  0,  0,  0],
#   #   [ 0,  0,  1,  1,  0,  0,  0,  0,  0,  1],
#   #   [ 5,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#   #   [ 5,  0,  1,  0,  0,  5,  0,  0,  0,  0],
#   #   [ 5,  0,  0,  1,  0,  0,  5,  0,  0,  0],
#   #   [ 5,  0,  1,  1,  0,  5,  5,  0,  0,  1],
#   #   [ 0,  5,  0,  0,  0,  0,  0,  0,  0,  0],
#   #   [ 0,  5,  1,  0,  0,  0,  0,  5,  0,  0],
#   #   [ 0,  5,  0,  1,  0,  0,  0,  0,  5,  0],
#   #   [ 0,  5,  1,  1,  0,  0,  0,  5,  5,  1],
#   #   [ 5,  5,  0,  0, 25,  0,  0,  0,  0,  0],
#   #   [ 5,  5,  1,  0, 25,  5,  0,  5,  0,  0],
#   #   [ 5,  5,  0,  1, 25,  0,  5,  0,  5,  0],
#   #   [ 5,  5,  1,  1, 25,  5,  5,  5,  5,  1]]

# df.append_columns({'constant': [1 for _ in range(len(data_dict['rating']))], 'rating': data_dict['rating']}, column_order = ['constant', 'rating'])
# print(df.columns)
# # ['beef', 'pb', 'mayo', 'jelly',
# #  'beef_pb', 'beef_mayo', 'beef_jelly',
# #  'pb_mayo', 'pb_jelly',
# #  'mayo_jelly',
# #  'constant', 'rating]
# print(df.to_array())
#   #  [[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1],
#   #   [ 0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  1],
#   #   [ 0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  1,  4],
#   #   [ 0,  0,  1,  1,  0,  0,  0,  0,  0,  1,  1,  0],
#   #   [ 5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  4],
#   #   [ 5,  0,  1,  0,  0,  5,  0,  0,  0,  0,  1,  8],
#   #   [ 5,  0,  0,  1,  0,  0,  5,  0,  0,  0,  1,  1],
#   #   [ 5,  0,  1,  1,  0,  5,  5,  0,  0,  1,  1,  0],
#   #   [ 0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  1,  5],
#   #   [ 0,  5,  1,  0,  0,  0,  0,  5,  0,  0,  1,  0],
#   #   [ 0,  5,  0,  1,  0,  0,  0,  0,  5,  0,  1,  9],
#   #   [ 0,  5,  1,  1,  0,  0,  0,  5,  5,  1,  1,  0],
#   #   [ 5,  5,  0,  0, 25,  0,  0,  0,  0,  0,  1,  0],
#   #   [ 5,  5,  1,  0, 25,  5,  0,  5,  0,  0,  1,  0],
#   #   [ 5,  5,  0,  1, 25,  0,  5,  0,  5,  0,  1,  0],
#   #   [ 5,  5,  1,  1, 25,  5,  5,  5,  5,  1,  1,  0]]

columns = ['firstname', 'lastname', 'age']
arr = [['Kevin', 'Fray', 5],
           ['Charles', 'Trapp', 17],
           ['Anna', 'Smith', 13],
           ['Sylvia', 'Mendez', 9]]
df = DataFrame.from_array(arr, columns)

print(df.to_array())

print(df.select_columns(['firstname','age']).to_array())
# [['Kevin', 5],
# ['Charles', 17],
# ['Anna', 13],
# ['Sylvia', 9]]


print(df.select_rows([1,3]).to_array())
# [['Charles', 'Trapp', 17],
# ['Sylvia', 'Mendez', 9]]


print(df.select_rows_where(
    lambda row: len(row['firstname']) >= len(row['lastname'])
                and row['age'] > 10
    ).to_array())
#[['Charles', 'Trapp', 17]]



print(df.order_by('age', ascending=True).to_array())
# [['Kevin', 'Fray', 5],
# ['Sylvia', 'Mendez', 9],
# ['Anna', 'Smith', 13],
# ['Charles', 'Trapp', 17]]

print(df.order_by('firstname', ascending=False).to_array())
# [['Sylvia', 'Mendez', 9],
# ['Kevin', 'Fray', 5],
# ['Charles', 'Trapp', 17],
# ['Anna', 'Smith', 13]]