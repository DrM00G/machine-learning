import sys
sys.path.append('src')
from node import Node
from graph import Graph


class WeightedGraph:
    def __init__(self, weights, vertic):
        self.verticies = vertic
        self.nodes = [Node(i) for i in range(len(vertic))]
        self.weights = weights
        self.build_from_edges(weights)

    def calc_shortest_path(self,init_node_index,end_node_index):
      self.nodes[init_node_index].d_value=0
      node_checklist=[init_node_index]
      for n in range(len(self.nodes)-1):
        for neighbor in self.nodes[node_checklist[n]].neighbors:
          if neighbor.index not in node_checklist:
            node_checklist.append(neighbor.index)
      # print(node_checklist)
      for node_index in node_checklist:
        for neighbor in self.nodes[node_index].neighbors:
          if (node_index,neighbor.index) in self.weights:
            new_dv=self.weights[(node_index,neighbor.index)]+self.nodes[node_index].d_value
          elif (neighbor.index,node_index) in self.weights:
            new_dv=self.weights[(neighbor.index,node_index)]+self.nodes[node_index].d_value
          if new_dv<neighbor.d_value:
            neighbor.d_value=new_dv
      # print([self.nodes[n].d_value for n in node_checklist])
      ideal_edges=[]
      for edge in self.weights:
        assumed_weight=abs(self.nodes[edge[0]].d_value-self.nodes[edge[1]].d_value)
        if assumed_weight == self.weights[edge]:
          ideal_edges.append(edge)
      ideal_graph=Graph(ideal_edges,self.verticies)
      return ideal_graph.calc_shortest_path(init_node_index, end_node_index)

    def calc_distance(self,init_node_index,end_node_index):
      path=self.calc_shortest_path(init_node_index,end_node_index)#now all the nodes have their d values.
      return self.nodes[end_node_index].d_value

    def build_from_edges(self, weights):
        for n in range(len(self.nodes)):
            self.nodes[n].set_value(self.verticies[n])
        for node in self.nodes:
            for edge in self.weights:
                if node.index == edge[0]:
                    for other_node in self.nodes:
                        if other_node.index == edge[1]:
                            node.set_neighbor(other_node)
                if node.index == edge[1]:
                    for other_node in self.nodes:
                        if other_node.index == edge[0]:
                            node.set_neighbor(other_node)
