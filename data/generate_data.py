import numpy as np
import os

# Letras desejadas
letters = "ABCDEJK"

# Representação das letras em matrizes 7x9 (1 = preenchido, 0 = vazio)
letter_representations = {
    'A': [
        "0011000",
        "0001000",
        "0001000",
        "0010100",
        "0010100",
        "0111110",
        "0100010",
        "0100010",
        "1110111"
    ],
    'B': [
        "1111110",
        "0100001",
        "0100001",
        "0100001",
        "0111110",
        "0100001",
        "0100001",
        "0100001",
        "1111110"
    ],
    'C': [
        "0011111",
        "0100001",
        "1000000",
        "1000000",
        "1000000",
        "1000000",
        "1000000",
        "0100001",
        "0011110"
    ],
    'D': [
        "1111100",
        "0100010",
        "0100001",
        "0100001",
        "0100001",
        "0100001",
        "0100001",
        "0100010",
        "1111100"
    ],
    'E': [
        "1111111",
        "0100001",
        "0100000",
        "0101000",
        "0111000",
        "0101000",
        "0100000",
        "0100001",
        "1111111"
    ],
    'J': [
        "0001111",
        "0000010",
        "0000010",
        "0000010",
        "0000010",
        "0000010",
        "0100010",
        "0100010",
        "0011100"
    ],
    'K': [
        "1110011",
        "0100100",
        "0101000",
        "0110000",
        "0110000",
        "0101000",
        "0100100",
        "0100010",
        "1110011"
    ]
}

# Transformar dicionário em arrays NumPy
X = []
y = []

for idx, letter in enumerate(letters):
    matrix = np.array([[int(bit) for bit in row] for row in letter_representations[letter]])
    X.append(matrix.flatten())  # Transformar matriz 7x9 em vetor
    y.append(idx)  # Índice da letra

# Converter para arrays NumPy
X = np.array(X)
y = np.array(y)

X_train = np.array([np.array([int(bit) for row in letter_representations[char] for bit in row]).flatten() for char in letters])
y_train = np.eye(len(letters))

# Criar a pasta "data" se não existir
data_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(data_path, "letters_7x9.npy")

# Salvar os dados
np.save(file_path, {"X": X, "y": y})
print(f"Arquivo '{file_path}' gerado com sucesso!")
