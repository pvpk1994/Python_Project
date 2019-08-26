from numpy import exp, array, random, dot


class NeuralNetwork():
    def __init__(self):
        # seeding the random Number generator so that the generatpr generates 
        # same numbers on every Run
        random.seed(1)
        # Since we are trying to create a single neuron with 3 input connection
        # and 1 output connection, we accordingly need 3x1 matrix of weights with range (-1,1).
        self.syn_weights = 2*random.random((3, 1))-1
        # print(type(self.syn_weights))
        # sigmoid function

    def sigmoid(self, x):
        result = 1/(1 + exp(-x))
        return result

    def sigmoid_derivative(self, x):
        return x * (1-x)

    def think(self, inputs):
        return self.sigmoid(dot(inputs, self.syn_weights))

    # train the model with train function (just for a single iteration)
    def train(self, train_inputs, train_outputs, num_iterations):
        for x in range(num_iterations):
            output = self.think(train_inputs)
            error = train_outputs - output
            adjust_wts = dot(train_inputs.T, error*self.sigmoid_derivative(output))
            self.syn_weights += adjust_wts
        # return self.syn_weights
   # def train_parameter()



if __name__ == "__main__":
    # Init a single NeuralNetwork
    neuralNet = NeuralNetwork()
    print("Random syn weights b/n -1 and 1")
    print(neuralNet.syn_weights)
    res = neuralNet.sigmoid(2)
    print(res)
    training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_set_ouput = array([[0, 1, 1, 0]])
    res1 = neuralNet.think(training_set_inputs)
    print(f'Think output: {res1}')
    neuralNet.train(training_set_inputs, training_set_ouput.T, 1000)
    print(f'Syn_Wts after 10000 trials')
    print(neuralNet.syn_weights)
    print('Expected outcome for [1, 0, 0] will be:')
    print(neuralNet.think(array([1, 1, 1])))
    