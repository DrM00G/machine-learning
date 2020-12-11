from dataframe import DataFrame


class KNearestNeighborsClassifier:
  def __init__(self,df, prediction_column,k):
    self.prediction_column = prediction_column
    self.df = df
    self.k


  def compute_distances(self, observation):
    distances = []
    for data in self.df.to_array():
      distances.append(self.compute_distance(observation,[data[n] for n in range(len(data)) if n!=self.df.columns.index(self.prediction_column)]))
    result=[[n] for n in distances]
    for n in range(len(distances)):
      result[n].append(self.df.to_array()[n][self.df.columns.index(self.prediction_column)])
    return DataFrame.from_array(result,columns =['distance','Cookie Type'])

  def compute_distance(self, observation, comp_data):
    observ_data = []
    for column in self.df.columns:
      if self.prediction_column != column:
        observ_data.append(observation[column])
    compared_stats = [(observ_data[n]-comp_data[n])**2 for n in range(len(observ_data))]
    return(sum(compared_stats)**(1/2))

  def sort_closest_cookie(self,cookie_data):
    highest_rated = cookie_data[0]
    for cookie in cookie_data:
      if cookie[0] > highest_rated[0]:
        highest_rated = cookie
    return (cookie_data.index(highest_rated))

  def nearest_neighbors(self,observation):
    close_list = self.compute_distances(observation).to_array()
    sorted_list = []
    for n in range(len(close_list)):
      sorted_list.append(close_list.pop(self.sort_closest_cookie(close_list)))
    return DataFrame.from_array(sorted_list[::-1],columns =['distance','Cookie Type'])

  def cagagory_average(self,data_list):
    catagories=['Shortbread',[0],'Sugar',[0],'Fortune',[0]]
    for data in data_list:
      catagories[catagories.index(data[1])+1].append(data[0])
    # print(range(len(catagories)//2))
    for n in range(len(catagories)//2):
      print(catagories[(n)*2]+": "+str(sum(catagories[(n)*2+1])/len(catagories[(n)*2+1])))


  def classify(self,observation):
    sorted_list = self.nearest_neighbors(observation).to_array()
    catagories=['Shortbread',[0],'Sugar',[0],'Fortune',[0]]
    for n in range(self.k):
      catagories[catagories.index(sorted_list[n][1])+1].append(1)
    if sum(catagories[1])>sum(catagories[3]) and sum(catagories[1])>sum(catagories[5]):
      return(catagories[0])
    if sum(catagories[3])>sum(catagories[1]) and sum(catagories[3])>sum(catagories[5]):
      return(catagories[2])
    if sum(catagories[5])>sum(catagories[3]) and sum(catagories[5])>sum(catagories[1]):
      return(catagories[4])



df = DataFrame.from_array(
    [['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
    ['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
    ['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
    ['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
    ['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
    ['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
    ['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
    ['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
    ['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
    ['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
    ['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
    ['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
    ['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ]],
    columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
    )
knn = KNearestNeighborsClassifier(df, prediction_column = 'Cookie Type')
observation = {
    'Portion Eggs': 0.10,
    'Portion Butter': 0.15,
    'Portion Sugar': 0.30,
    'Portion Flour': 0.45
}

#print(knn.compute_distances(observation).to_array())

print(knn.nearest_neighbors(observation).to_array())

knn.cagagory_average(knn.compute_distances(observation).to_array())

knn.classify(observation, k=5)

