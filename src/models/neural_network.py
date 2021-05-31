
class NeuralNetwork:
    def __init__(self, weights):
        self.weights=weights
        self.vertices = {x:0 for x in list(set([x for x,y in self.weights]+[y for x,y in self.weights]))}
        self.inputs = list(set([x for x,y in weights]))
        self.output = list(set([y for x,y in weights]))

    def predict(self,inputs):
        for n in range(len(inputs)):
          self.vertices[self.inputs[n]] = inputs[n]
        # print(self.inputs)
        # print(self.output)
          
        result = 0
        for x,y in self.weights:
            if y == self.output[0]:
                result += self.vertices[x]*self.weights[(x,y)]
        return result
    
    def calc_squared_error(self,data_point):
      result=nn.predict(data_point['input'])
      return (data_point['output'][0]-result)**2

    def calc_gradient(self,data_point)
        for i in range(len(data_point['input'])):
            self.vertices[self.inputs[i]] = data_point['input'][i]

weights = {(0,2): -0.1, (1,2): 0.5}
nn = NeuralNetwork(weights)

print(nn.predict([1,3]))

data_point = {'input': [1,3], 'output': [7]}
print(nn.calc_squared_error(data_point))