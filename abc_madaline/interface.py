import tkinter as tk
import numpy as np
from abc_madaline.madaline import Madaline

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Reconhecimento de Letras - Madaline")

        self.canvas_size = 200
        self.grid_size = 8
        self.cell_size = self.canvas_size // self.grid_size
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.clear_button = tk.Button(root, text="Limpar", command=self.clear_canvas)
        self.clear_button.grid(row=1, column=0)

        self.predict_button = tk.Button(root, text="Prever", command=self.predict_letter)
        self.predict_button.grid(row=1, column=1)

        self.result_label = tk.Label(root, text="Resultado: ")
        self.result_label.grid(row=1, column=2)

        self.madaline = Madaline(64, 26)  # 64 entradas (8x8) e 26 saídas (A-Z)

    def draw(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        self.canvas.create_rectangle(
            x * self.cell_size, y * self.cell_size,
            (x + 1) * self.cell_size, (y + 1) * self.cell_size,
            fill="black"
        )

    def clear_canvas(self):
        self.canvas.delete("all")

    def get_canvas_matrix(self):
        matrix = np.zeros((self.grid_size, self.grid_size))
        for item in self.canvas.find_all():
            coords = self.canvas.coords(item)
            x, y = int(coords[0] // self.cell_size), int(coords[1] // self.cell_size)
            matrix[y, x] = 1
        return matrix.flatten()

    def predict_letter(self):
        input_vector = self.get_canvas_matrix()
        prediction = self.madaline.predict(input_vector)
        letter = chr(np.argmax(prediction) + ord('A'))
        self.result_label.config(text=f"Resultado: {letter}")
