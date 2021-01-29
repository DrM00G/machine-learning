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


class Node:
  def __init__(self, df, split_metric):
    self.df = df
    self.split_metric = split_metric
    self.row_indices = df.ordered_dict['node_index']
    self.class_counts = self.calc_class_counts()
    self.impurity = self.calc_impurity()
    self.high = 0
    self.low = 0
    self.unsplit = True
    self.bottom = False
    if self.impurity != 0:
      self.possible_splits = self.calc_possible_splits()
      self.best_split = self.find_best_split()

  def calc_class_counts(self):
    classes = []
    for classification in self.df.ordered_dict['class']:
      if classification not in classes:
        classes.append(classification)
    # print(classes)
    cd={classification: 0 for classification in classes}
    for classification in self.df.ordered_dict['class']:
      cd[classification]+=1
    return cd

  def calc_impurity(self):
    node_classes = self.df.ordered_dict['class']
    return sum([(self.class_counts[classification]/len(node_classes)) * (1 - (self.class_counts[classification]/len(node_classes)) ) for classification in self.class_counts.keys()])

  def calc_possible_splits(self):
    points = [[],'x',[],'y']
    for x in self.df.ordered_dict['x']:
      if x not in points[0]:
        points[0].append(x)
    for y in self.df.ordered_dict['y']:
      if y not in points[2]:
        points[2].append(y)
    splits = []
    for n in range(2):
      for i in range(len(points[2*n])-1):
        splits.append([points[2*n+1],(points[2*n][i]+points[2*n][i+1])/2,self.calc_goodness((points[2*n][i]+points[2*n][i+1])/2, n)])
    return DataFrame.from_array(splits, ['feature', 'value', 'goodness of split'])

  def calc_goodness(self, split, axis):
      goodness = self.impurity
      low = []
      high = []
      for point in self.df.to_array():
          if point[axis] < split:
              low.append(point)
          elif point[axis] >= split:
              high.append(point)
      low_node = Node(DataFrame.from_array(low, self.df.columns),self.split_metric)
      high_node = Node(DataFrame.from_array(high, self.df.columns),self.split_metric)
      new_nodes = [low_node, high_node]
      for split_node in new_nodes:
          goodness -= (len(split_node.row_indices)/len(self.row_indices)) * split_node.impurity
      return round(goodness,3)
  
  def find_best_split(self):
    # print("testing")
    if self.split_metric == "gini":
      best_goodness = 0
      for split in self.possible_splits.to_array():
        if split[2]>best_goodness:
          best_split=(split[0],split[1])
          best_goodness=split[2]
      return best_split
    elif self.split_metric == "random":
      rand_axis=random.choice(['x','y'])
      best_goodness = 0
      for split in self.possible_splits.to_array():
        if split[2]>best_goodness and split[0]==rand_axis:
          best_split=(split[0],split[1])
          best_goodness=split[2]
      return best_split

  def split(self,max_depth, depth):
    # print("testing")
    if self.impurity != 0 and (max_depth>depth or max_depth==False):
      if self.unsplit :
        if self.best_split[0] == 'x':
          axis = 0
        else:
          axis = 1
        low_points = []
        high_points = []
        for point in self.df.to_array():
            if point[axis] < self.best_split[1]:
                low_points.append(point)
            elif point[axis] >= self.best_split[1]:
                high_points.append(point)
        self.low = Node(DataFrame.from_array(low_points, self.df.columns),self.split_metric)
        self.high = Node(DataFrame.from_array(high_points, self.df.columns),self.split_metric)
        self.unsplit = False
      elif max_depth>depth+1 or max_depth==False:
        if self.low.impurity != 0:
          self.low.split(max_depth, depth+1)
        if self.high.impurity != 0:
          self.high.split(max_depth, depth+1)
    else:
      self.unsplit = False

  def unfitted(self):
    if self.impurity == 0:
      return False
    elif self.unsplit:
      return True
    elif self.low.unfitted() == True or self.high.unfitted() == True:
      return True
    else:
      return False
      