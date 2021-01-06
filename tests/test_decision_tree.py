import sys
sys.path.append('src')
from decision_tree import DecisionTree
from dataframe import DataFrame

# df = DataFrame.from_array(
#     [[1, 11, 'A'],
#     [1, 12, 'A'],
#     [2, 11, 'A'],
#     [1, 13, 'B'],
#     [2, 13, 'B'],
#     [3, 13, 'B'],
#     [3, 11, 'B']],
#     columns = ['x', 'y', 'class']
# )
# dt = DecisionTree(df)

# assert dt.root.row_indices == [0, 1, 2, 3, 4, 5, 6], 'row_indices test failed'
# print('row_indices test succeeded')

# assert dt.root.class_counts == {
#     'A': 3,
#     'B': 4
# }, 'class_counts test failed'
# print('class_counts test succeeded')

# assert round(dt.root.impurity,3) == 0.490 , 'impurity test failed, instead showed '+str(round(dt.root.impurity,3))
# print('impurity test succeeded')

# assert dt.root.possible_splits.to_array() == [['x', 1.5,  0.085],
#  ['x', 2.5,  0.147],
#  ['y', 11.5, 0.085],
#  ['y', 12.5, 0.276]], 'possible_splits test failed, is instead '+str(dt.root.possible_splits.to_array())
# print('possible_splits test succeeded')

# assert dt.root.best_split == ('y', 12.5) , 'best_split test failed, instead showed '+str(dt.root.best_split)
# print('best_split test succeeded')

# dt.split()

# assert dt.root.low.row_indices == [0, 1, 2, 6], 'low.row_indices test failed'
# print('low.row_indices test succeeded')

# assert dt.root.high.row_indices == [3, 4, 5], 'high.row_indices test failed'
# print('high.row_indices test succeeded')

# assert dt.root.low.impurity == 0.375, 'low.impurity test failed'
# print('low.impurity test succeeded')

# assert dt.root.high.impurity == 0, 'high.impurity test failed'
# print('high.impurity test succeeded')

# assert dt.root.low.possible_splits.to_array() == [['x', 1.5,  0.125],
#  ['x', 2.5,  0.375],
#  ['y', 11.5, 0.042]], 'low.possible_splits test failed'
# print('low.possible_splits test succeeded')

# assert dt.root.low.best_split == ('x', 2.5), 'low.best_split test failed'
# print('low.best_split test succeeded')

# dt.split()

# assert dt.root.low.low.row_indices == [0, 1, 2], 'low.low.row_indices test failed'
# print('low.low.row_indices test succeeded')

# assert dt.root.low.high.row_indices == [6], 'low.high.row_indices test failed'
# print('low.high.row_indices test succeeded')

# assert dt.root.low.low.impurity == 0, 'low.low.impurity test failed'
# print('low.low.impurity test succeeded')

# assert dt.root.low.high.impurity == 0, 'low.high.impurity test failed'
# print('low.high.impurity test succeeded')

# df2 = DataFrame.from_array(
#     [[1, 11, 'A'],
#     [1, 12, 'A'],
#     [2, 11, 'A'],
#     [1, 13, 'B'],
#     [2, 13, 'B'],
#     [3, 13, 'B'],
#     [3, 11, 'B']],
#     columns = ['x', 'y', 'class']
# )
# dt2 = DecisionTree(df2)

# dt2.fit()

# print("fit tests:")

# assert dt2.root.high.row_indices == [3, 4, 5], 'high.row_indices test failed'
# print('high.row_indice test succeeded')

# assert dt2.root.low.low.row_indices == [0, 1, 2], 'low.low.row_indices test failed'
# print('low.low.row_indices test succeeded')

# assert dt2.root.low.high.row_indices == [6], 'low.high.row_indices test failed'
# print('low.high.row_indices test succeeded')

print("Advanced tests:")

df = DataFrame.from_array(
    [[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],
    [3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],
    [2,12,'B'],[2,12,'B'],
    [3,12,'A'],[3,12,'A'],
    [3,11,'A'],[3,11,'A'],
    [3,11.5,'A'],[3,11.5,'A'],
    [4,11,'A'],[4,11,'A'],
    [4,11.5,'A'],[4,11.5,'A'],
    [2,10.5,'A'],[2,10.5,'A'],
    [3,10.5,'B'],
    [4,10.5,'A']],
    columns = ['x', 'y', 'class']
)
dt = DecisionTree(split_metric = 'gini')
dt.fit(df)

assert dt.root.best_split == ('y', 12.5), 'best_split test failed'
print('best_split test succeeded')

assert dt.root.low.best_split == ('x', 2.5), 'low.best_split test failed'
print('low.best_split test succeeded')

assert dt.root.low.low.best_split == ('y', 11.25), 'low.low.best_split test failed'
print('low.low.best_split test succeeded')
#--
# assert dt.root.low.high.best_split == ('y', 10.75), 'best_split test failed, is instead:'+str(dt.root.low.high.best_split)
# print('best_split test succeeded')

assert dt.root.low.high.low.best_split == ('x', 3.5), 'best_split test failed'
print('best_split test succeeded')

assert dt.classify({'x': 2, 'y': 11.5}) == 'B', 'Classification failed'
assert dt.classify({'x': 2.5, 'y': 13}) == 'B', 'Classification failed'
assert dt.classify({'x': 4, 'y': 12}) == 'A', 'Classification failed'
assert dt.classify({'x': 3.25, 'y': 10.5}) == 'B', 'Classification failed'
assert dt.classify({'x': 3.75, 'y': 10.5}) == 'A', 'Classification failed'

print("Random Tests")

df = DataFrame.from_array(
    [[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],
    [3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],
    [2,12,'B'],[2,12,'B'],
    [3,12,'A'],[3,12,'A'],
    [3,11,'A'],[3,11,'A'],
    [3,11.5,'A'],[3,11.5,'A'],
    [4,11,'A'],[4,11,'A'],
    [4,11.5,'A'],[4,11.5,'A'],
    [2,10.5,'A'],[2,10.5,'A'],
    [3,10.5,'B'],
    [4,10.5,'A']],
    columns = ['x', 'y', 'class']
)
dt = DecisionTree(split_metric = 'random')
dt.fit(df)

print("root.best_split"+str(dt.root.best_split))
print("root.low.best_split"+str(dt.root.low.best_split))
print("Run multiple times to see if random")
# >>> dt.root.best_split
# ('y', 12.5)
# >>> dt.root.low.best_split
# ('x', 2.5)
# >>> dt.root.low.low.best_split
# ('y', 11.25)
# >>> dt.root.low.high.best_split
# ('y', 10.75)
# >>> dt.root.low.high.low.best_split
# ('x', 3.5)

# >>> dt.classify({'x': 2, 'y': 11.5})
# 'B'
# >>> dt.classify({'x': 2.5, 'y': 13})
# 'B'
# >>> dt.classify({'x': 4, 'y': 12})
# 'A'
# >>> dt.classify({'x': 3.25, 'y': 10.5})
# 'B'
# >>> dt.classify({'x': 3.75, 'y': 10.5})
# 'A'