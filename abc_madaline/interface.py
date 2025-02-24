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
        
        self.clear_button = Frame(master)
        self.clear_button = Button(self.master, text="Clear", command=self.clear)
        self.clear_button['font'] = ('Verdana', '10')
        self.clear_button.pack()
        
        
        
    def clear(self):
        for row in self.checkboxes:
            for checkbox in row:
                checkbox.set(0)
                
    def get_matrix(self):
        return np.array([[checkbox.get() for checkbox in row] for row in self.checkboxes]).flatten()
        
        
        

