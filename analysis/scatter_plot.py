import matplotlib.pyplot as plt

dataset = [[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],
    [3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],
    [2,12,'B'],[2,12,'B'],
    [3,12,'A'],[3,12,'A'],
    [3,11,'A'],[3,11,'A'],
    [3,11.5,'A'],[3,11.5,'A'],
    [4,11,'A'],[4,11,'A'],
    [4,11.5,'A'],[4,11.5,'A'],
    [2,10.5,'A'],[2,10.5,'A'],
    [3,10.5,'B'],
    [4,10.5,'A']]
data_counter=[]
for data in dataset:
  if data not in data_counter:
    data_counter.append(data)
    data_counter.append(0)
for data in dataset:
  data_counter[data_counter.index(data)+1]+=1
red_blue = ([[],[],[]],[[],[],[]])#x,y,s
for n in range(int(len(data_counter)/2)):
  if data_counter[2*n][2] == 'A':
    color_select=0
  else:
    color_select=1
  red_blue[color_select][0].append(data_counter[2*n][0])
  red_blue[color_select][1].append(data_counter[2*n][1])
  red_blue[color_select][2].append(50*data_counter[2*n+1])

plt.scatter(x= red_blue[1][0], y=red_blue[1][1], s= red_blue[1][2], c='blue')
plt.scatter(x=red_blue[0][0], y=red_blue[0][1], s=red_blue[0][2], c='red')
plt.savefig('scatter.png')
plt.show()