import numpy as np

class Madaline:
    def __init__(self, input_size, output_size, learning_rate=0.1, epochs=100):
        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.random.uniform(-1, 1, (output_size, input_size))
        self.bias = np.random.uniform(-1, 1, output_size)

    def activation(self, x):
        return np.where(x >= 0, 1, -1)

    def train(self, X, y):
        for _ in range(self.epochs):
            for i in range(len(X)):
                output = self.activation(np.dot(self.weights, X[i]) + self.bias)
                error = y[i] - output
                self.weights += self.learning_rate * np.outer(error, X[i])
                self.bias += self.learning_rate * error

    def predict(self, X):
        return self.activation(np.dot(self.weights, X) + self.bias)
