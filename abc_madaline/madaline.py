import numpy as np
from data.data import get_X_train, get_y_train

class Madaline:
    def __init__(self, 
                 learning_rate=0.01,
                 epochs=100,
                 input_size=63,
                 num_neurons=7,  # Correspondendo ao número de classes
                 num_classes=7,
                 X_train=None,
                 Y_train=None):
        
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.input_size = input_size
        self.num_neurons = num_neurons  
        self.num_classes = num_classes
        self.X_train = X_train if X_train is not None else get_X_train()
        self.Y_train = Y_train if Y_train is not None else get_y_train()
        
        # Inicializa pesos e bias aleatórios pequenos para evitar saturação
        self.weights = np.random.uniform(-0.5, 0.5, (self.num_neurons, self.input_size))
        self.bias = np.random.uniform(-0.5, 0.5, self.num_neurons)
        
        self.X_error_axis = []
        self.y_error_axis = []
        
    def activation(self, x):
        """Função de ativação degrau bipolar vetorizada"""
        return np.where(x >= 0, 1, -1)

    def predict(self, x):
        """Faz a predição para uma amostra"""
        y = np.dot(self.weights, x) + self.bias
        return self.activation(y)

    def train(self):
        """Treina a rede Madaline"""
        self.X_train = []
        self.y_train = []
        for epoch in range(self.epochs):
            for i in range(self.X_train.shape[0]):
                x = self.X_train[i]  # Entrada (vetor de 63 posições)
                y_pred = self.predict(x)  # Saída prevista
                
                # One-hot encoding da saída esperada
                t = np.full(self.num_classes, -1)  # Inicializa todas as saídas como -1
                t[self.Y_train[i]] = 1  # Define a classe correta como +1
                
                # Calcula erro (agora ambas as variáveis têm shape (7,))
                e = t - y_pred
                
                # Adiciona erro ao gráfico
                self.X_error_axis.append(epoch)
                self.y_error_axis.append(np.sum(e))
                
                # Atualiza apenas os pesos dos neurônios com erro
                update_indices = np.where(e != 0)[0]  # Índices onde há erro
                for j in update_indices:
                    self.weights[j] += self.learning_rate * e[j] * x
                    self.bias[j] += self.learning_rate * e[j]

            # Exibir progresso a cada 10 epochs
            if epoch % 10 == 0:
                print(f"Epoch {epoch}/{self.epochs}: Treinando...")

        print("Treinamento concluído!")

    def identify_letter(self, x):
        """Retorna a letra correspondente ao índice previsto"""
        letters = ['A', 'B', 'C', 'D', 'E', 'J', 'K']  # Mantido correto
        if 0 <= x < len(letters):
            return letters[x]
        return "Desconhecido"

    def identify(self, x):
        """Prediz a letra associada à entrada"""
        y = self.predict(x)
        return self.identify_letter(np.argmax(y))

if __name__ == '__main__':
    madaline = Madaline()
    axis_error = madaline.train()
    
    for i in range(21):
        test_sample = get_X_train()[i]
        identified = madaline.identify(test_sample)
        print(f"Identified letter: {identified}")
        print(f"Expected letter: {madaline.identify(get_X_train()[i])}")
