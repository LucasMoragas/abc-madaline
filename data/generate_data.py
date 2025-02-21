import numpy as np
import os

# Letras desejadas
letters = "ABCDEJK"

# Representação das letras em matrizes 8x8 (1 = preenchido, 0 = vazio)
letter_representations = {
    'A': [
        "00111100",
        "01000010",
        "10000001",
        "10000001",
        "11111111",
        "10000001",
        "10000001",
        "10000001"
    ],
    'B': [
        "11111100",
        "10000010",
        "10000010",
        "11111100",
        "10000010",
        "10000010",
        "10000010",
        "11111100"
    ],
    'C': [
        "00111110",
        "01000000",
        "10000000",
        "10000000",
        "10000000",
        "10000000",
        "01000000",
        "00111110"
    ],
    'D': [
        "11111000",
        "10000100",
        "10000010",
        "10000010",
        "10000010",
        "10000010",
        "10000100",
        "11111000"
    ],
    'E': [
        "11111111",
        "10000000",
        "10000000",
        "11111110",
        "10000000",
        "10000000",
        "10000000",
        "11111111"
    ],
    'J': [
        "00011111",
        "00000010",
        "00000010",
        "00000010",
        "00000010",
        "10000010",
        "10000010",
        "01111100"
    ],
    'K': [
        "10000001",
        "10000010",
        "10000100",
        "10001000",
        "10010000",
        "10100000",
        "11000000",
        "10000000"
    ]
}

# Transformar dicionário em arrays NumPy
X = []
y = []

for idx, letter in enumerate(letters):
    matrix = np.array([[int(bit) for bit in row] for row in letter_representations[letter]])
    X.append(matrix.flatten())  # Transformar matriz 8x8 em vetor de 64 valores
    y.append(idx)  # Índice da letra

# Converter para arrays NumPy
X = np.array(X)
y = np.array(y)

# Criar a pasta "data" se não existir
data_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(data_path, "letters_8x8.npy")

# Salvar os dados
np.save(file_path, {"X": X, "y": y})
print(f"Arquivo '{file_path}' gerado com sucesso!")
