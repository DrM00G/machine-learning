from dataframe import DataFrame
import random


class DecisionTree:
    def __init__(self, split_metric = 'gini', max_depth = False):
      if split_metric == "random":
         self.max_depth =  max_depth
      else:
         self.max_depth = False
      self.df = "Not yet"
      self.root = "Not yet"
      self.split_metric = split_metric

    def split(self):
        self.root.split()

    def fit(self, df):
      self.df = df
      self.df = self.df.append_columns({'node_index': [n for n in range(len(df.to_array()))]})
      self.root = Node(self.df,self.split_metric)
      while self.root.unfitted():
        self.split()

    def classify(self, point, node = None):
        if node is None:
            node = self.root
        if node.impurity == 0:
            class_type = list(node.class_counts)[0]
            for classification in list(node.class_counts):
              # print(classification)
              # print(node.class_counts)
              # print("Classes:"+str(list(node.class_counts)))
              if node.class_counts[classification] > node.class_counts[class_type]:
                class_type = classification
            return class_type
        if point[node.best_split[0]] < node.best_split[1]:
            return self.classify(point, node = node.low)
            # print("yes")
        if point[node.best_split[0]] >= node.best_split[1]:
            return self.classify(point, node = node.high)
            # print("yes")
