from tkinter import *
import numpy as np
from abc_madaline.madaline import Madaline

class App:
    def __init__(self, root, master=None):
        self.root = root
        self.master = Frame(master)
        self.master.pack()
        
        self.header = Label(self.master, text="ABC Madaline")
        self.header['font'] = ('Verdana', '20')
        self.header.pack()
        
        self.matrix_container = Frame(self.master)
        self.matrix_container.pack()
        self.matrix = Frame(self.matrix_container)
        self.matrix.pack(side=LEFT)
        
        self.checkboxes = []
        for i in range(8):
            row = []
            for j in range(8):
                var = IntVar()
                c = Checkbutton(self.matrix, variable=var)
                c.grid(row=i, column=j)
                row.append(var)
            self.checkboxes.append(row)
        
        self.buttons = Frame(self.master)
        self.buttons.pack(pady=10)
        
        self.clear_button = Button(self.buttons, text="Clear", command=self.clear)
        self.clear_button['font'] = ('Verdana', '10')
        self.clear_button.pack(side=LEFT, padx=5)
        
        self.train_button = Button(self.buttons, text="Train", command=self.train)
        self.train_button['font'] = ('Verdana', '10')
        self.train_button.pack(side=LEFT, padx=5)
        
    def clear(self):
        for row in self.checkboxes:
            for checkbox in row:
                checkbox.set(0)
                
    def get_matrix(self):
        return np.array([[checkbox.get() for checkbox in row] for row in self.checkboxes]).flatten()
    
    def train(self):
        pass

if __name__ == "__main__":
    root = Tk()
    root.title("ABC Madaline")
    app = App(root)
    root.mainloop()
