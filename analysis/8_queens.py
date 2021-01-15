import random
def show_board(locations):
  empty_board=[["." for x in range(8)] for x in range(8)]
  count=0
  for coord in locations:
    empty_board[coord[0]][coord[1]]=str(count)
    count=count+1
  row_array = ['0', '.', '.', '.', '.', '.', '.', '.']
  for row_array in empty_board:
    row_string = '  '.join(row_array) # note that '  ' is TWO spaces
    print(row_string)

def calc_cost(locations):
  cost=0
  for coord_1 in locations:
    for coord_2 in locations:
      if coord_1 != coord_2:
        if coord_1[0] == coord_2[0]:
          # print(str(coord_1)+"&"+str(coord_2))
          cost=cost+1
        elif coord_1[1] == coord_2[1]:
          # print(str(coord_1)+"&"+str(coord_2))
          cost=cost+1
        elif abs((coord_1[1]-coord_2[1])/(coord_1[0]-coord_2[0]))==1:
          # print(str(coord_1)+"&"+str(coord_2))
          # print((coord_1[1]-coord_2[1])/(coord_1[0]-coord_2[0]))
          cost=cost+1
  return(cost/2)

def random_optimizer(n):
  best_cost = 1000000000
  best_array = []
  for i in range(n):
    rand_locs=[]
    while len(rand_locs)<8:
      rand_point=(random.randint(0,7),random.randint(0,7))
      if rand_point not in rand_locs:
        rand_locs.append(rand_point)
    cost=calc_cost(rand_locs)
    if cost<best_cost:
      best_cost=cost
      best_array=rand_locs
  final_dict = {
    'locations': best_array,
    'cost': best_cost
  }
  return final_dict


locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
show_board(locations)
print(calc_cost(locations))
print("Optimizer Tests:")
for n in [10,50,100,500,1000]:
  rand_dict=random_optimizer(n)
  print(rand_dict["cost"])
  if rand_dict["cost"]==0:
    show_board(rand_dict['locations'])
# print("Final Solution")
# cost=100
# locs=[]
# while cost!=0:
#   rand_dict=random_optimizer(2000)
#   cost=rand_dict["cost"]
#   locs=rand_dict["locations"]
# show_board(locs)

