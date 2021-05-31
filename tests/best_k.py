import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from k_nearest_neighbors_classifier import KNearestNeighborsClassifier
from dataframe import DataFrame

df = DataFrame.from_array(
   [['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
['Sugar'       ,     0.02     ,       0.08     ,      0.45     ,     0.45      ],
['Sugar'       ,     0.10     ,       0.15     ,      0.35     ,     0.40      ],
['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ],
['Shortbread'  ,     0.05     ,       0.12     ,      0.28     ,     0.55      ],
['Shortbread'  ,     0.14     ,       0.27     ,      0.31     ,     0.28      ],
['Shortbread'  ,     0.15     ,       0.23     ,      0.30     ,     0.32      ],
['Shortbread'  ,     0.20     ,       0.10     ,      0.30     ,     0.40      ]],

    columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
    )

plot_data = []
k = 18
arr = []

for n in range(1,k):
    knn = KNearestNeighborsClassifier(df, 'Cookie Type',n)
    correct_observations = 0
    print('Testing k = '+str(n))
    for i in range(len(knn.df.to_array())):
        correct = knn.df.to_array()[i][0]
        observation = {column:knn.df.ordered_dict[column][i] for column in knn.df.columns if column != 'Cookie Type'}
        copy = knn.df.to_array()
        del copy[i]
        df1 = DataFrame.from_array(copy, columns = knn.df.columns)
        knn2 = KNearestNeighborsClassifier(df1, 'Cookie Type',k)

        if knn2.fit(observation) == correct:
            correct_observations += 1
    arr.append(correct_observations/len(knn.df.to_array()))




plt.plot([x for x in range(1,k)],arr,linewidth = 0.75)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.title('Best size k')
plt.savefig('TEST.png') 