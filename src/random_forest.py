from dataframe import DataFrame
from decision_tree import DecisionTree
class RandomForest:
  def __init__(self, n):
      self.n = n
      self.tree_list = [DecisionTree(split_metric ='random') for i in range(n)]

  def fit(self, df):
      for tree in self.tree_list:
        tree.fit(df)

  def predict(self, observation):
      class_list = []
      for tree in self.tree_list:
        prediction = tree.classify(observation)        
        class_list.append(prediction)
      class_dict = {classific : class_list.count(classific) for classific in class_list}
      print(class_dict.keys())
      return list(class_dict.keys())[0]

