import numpy as np
from data.data import get_X_train, get_y_train
import matplotlib.pyplot as plt

class Madaline:
    def __init__(self, 
                 learning_rate=0.01,
                 epochs=30,
                 input_size=63,
                 num_classes=7,
                 X_train=None,
                 Y_train=None):
        
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.input_size = input_size
        self.num_classes = num_classes
        self.X_train = X_train if X_train is not None else get_X_train()
        self.Y_train = Y_train if Y_train is not None else get_y_train()
        
        self.weights = np.random.uniform(-0.5, 0.5, (self.num_classes, self.input_size))
        self.bias = np.random.uniform(-0.5, 0.5, self.num_classes)
        
        self.sum_error = 0
        self.X_error_axis = []
        self.y_error_axis = []
        
    def activation(self, x):
        return np.where(x >= 0, 1, -1)

    def predict(self, x):
        y = np.dot(self.weights, x) + self.bias
        return self.activation(y)

    def train(self, by_epoch=True, error_threshold=0.01):
        self.X_error_axis = []
        self.y_error_axis = []
        
        if by_epoch:
            for epoch in range(self.epochs):
                self.sum_error = 0
                for i in range(self.X_train.shape[0]):
                    x = self.X_train[i]
                    y_pred = self.predict(x)
                    
                    t = np.full(self.num_classes, -1)
                    t[self.Y_train[i]] = 1  
                    
                    e = t - y_pred
                    self.sum_error += pow(np.sum(e), 2)
                    
                    update_indices = np.where(e != 0)[0]
                    for j in update_indices:
                        self.weights[j] += self.learning_rate * e[j] * x
                        self.bias[j] += self.learning_rate * e[j]
                
                self.X_error_axis.append(epoch)
                self.y_error_axis.append(0.5 * self.sum_error)
        else:
            epoch = 0
            while True:
                self.sum_error = 0
                for i in range(self.X_train.shape[0]):
                    x = self.X_train[i]
                    y_pred = self.predict(x)
                    
                    t = np.full(self.num_classes, -1)
                    t[self.Y_train[i]] = 1  
                    
                    e = t - y_pred
                    self.sum_error += pow(np.sum(e), 2)
                    
                    update_indices = np.where(e != 0)[0]
                    for j in update_indices:
                        self.weights[j] += self.learning_rate * e[j] * x
                        self.bias[j] += self.learning_rate * e[j]
                
                self.X_error_axis.append(epoch)
                self.y_error_axis.append(0.5 * self.sum_error)
                epoch += 1
                if self.sum_error <= error_threshold:
                    break

        print("Treinamento concluído!")

    def identify_letter(self, x):
        letters = ['A', 'B', 'C', 'D', 'E', 'J', 'K'] 
        if 0 <= x < len(letters):
            return letters[x]
        return "Desconhecido"

    def identify(self, x):
        y = self.predict(x)
        return self.identify_letter(np.argmax(y))

if __name__ == '__main__':
    madaline = Madaline()
    axis_error = madaline.train(by_epoch=False, error_threshold=0.01)
    
    for i in range(21):
        test_sample = get_X_train()[i]
        identified = madaline.identify(test_sample)
        print(f"Identified letter: {identified}")
        print(f"Expected letter: {madaline.identify(get_X_train()[i])}")
        
    plt.plot(madaline.X_error_axis, madaline.y_error_axis)
    plt.xlabel('Epochs')
    plt.ylabel('Error')
    plt.title('Error x Epochs')
    plt.show()
