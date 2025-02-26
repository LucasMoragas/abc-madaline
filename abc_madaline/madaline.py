import numpy as np

class Madaline:
    def __init__(self, input_size, output_size, learning_rate=0.1, epochs=100):
        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.random.uniform(-0.1, 0.1, (output_size, input_size))
        self.bias = np.random.uniform(-0.1, 0.1, output_size)

    def activation(self, x):
        return np.where(x >= 0, 1, 0)

    def train(self, X, y):
        total_error = 0
        for i in range(len(X)):
            output = self.activation(np.dot(self.weights, X[i]) + self.bias)
            error = y[i] - output
            total_error += np.sum(error ** 2)  # Erro quadrático médio
            self.weights += self.learning_rate * np.outer(error, X[i])
            self.bias += self.learning_rate * error
        return total_error / len(X)  # Retornar o erro médio

    def predict(self, X):
        X = X.reshape(-1, self.input_size)  # Garante que a entrada esteja no formato correto
        return self.activation(np.dot(self.weights, X.T) + self.bias[:, np.newaxis]).T

