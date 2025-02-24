from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from abc_madaline.madaline import Madaline

class App:
    def __init__(self, root, master=None):
        self.root = root
        self.root.configure(bg="#2E2E2E")
        self.master = Frame(master, bg="#2E2E2E")
        self.master.pack(fill=BOTH, expand=True)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.container = Frame(self.master, bg="#2E2E2E")
        self.container.pack(fill=BOTH, expand=True)
        
        self.left_frame = Frame(self.container, bg="#2E2E2E")
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)
        
        self.header = Label(self.left_frame, text="ABC Madaline", bg="#2E2E2E", fg="white", font=('Verdana', '24', 'bold'))
        self.header.pack(pady=10)
        
        self.matrix_container = Frame(self.left_frame, bg="#2E2E2E")
        self.matrix_container.pack()
        self.matrix = Frame(self.matrix_container, bg="#2E2E2E")
        self.matrix.pack()
        
        self.checkboxes = []
        for i in range(9):
            row = []
            for j in range(7):
                var = IntVar()
                c = Checkbutton(self.matrix, variable=var, bg="#2E2E2E", fg="white", selectcolor="#555555", width=3, height=2)
                c.grid(row=i, column=j, padx=3, pady=3)
                row.append(var)
            self.checkboxes.append(row)
        
        self.inputs_frame = Frame(self.left_frame, bg="#2E2E2E")
        self.inputs_frame.pack(pady=10, fill=X)
        
        Label(self.inputs_frame, text="Number of Cycles:", bg="#2E2E2E", fg="white", font=('Verdana', '12')).grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.cycles_entry = Entry(self.inputs_frame, bg="#555555", fg="white", insertbackground="white", font=('Verdana', '12'))
        self.cycles_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        Label(self.inputs_frame, text="Learning Rate:", bg="#2E2E2E", fg="white", font=('Verdana', '12')).grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.learning_rate_entry = Entry(self.inputs_frame, bg="#555555", fg="white", insertbackground="white", font=('Verdana', '12'))
        self.learning_rate_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        self.train_button = Button(self.inputs_frame, text="Train", command=self.train, bg="#555555", fg="white", font=('Verdana', '12', 'bold'))
        self.train_button.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky=W+E)
        
        self.buttons = Frame(self.left_frame, bg="#2E2E2E")
        self.buttons.pack(pady=10)
        
        self.clear_button = Button(self.buttons, text="Clear", command=self.clear, bg="#555555", fg="white", font=('Verdana', '12', 'bold'))
        self.clear_button.pack(side=LEFT, padx=5)
        
        self.identify_button = Button(self.buttons, text="Identify", command=self.identify, bg="#555555", fg="white", font=('Verdana', '12', 'bold'))
        self.identify_button.pack(side=LEFT, padx=5)
        
        self.result_label = Label(self.left_frame, text="Identified Character: ", bg="#2E2E2E", fg="white", font=('Verdana', '14', 'bold'))
        self.result_label.pack(pady=10)
        
        self.right_frame = Frame(self.container, bg="#2E2E2E")
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=20, pady=20)
        
        self.right_frame.configure(bg="#2E2E2E")
        self.plot_mock_graph()
        
    def clear(self):
        for row in self.checkboxes:
            for checkbox in row:
                checkbox.set(0)
                
    def get_matrix(self):
        return np.array([[checkbox.get() for checkbox in row] for row in self.checkboxes]).flatten()
    
    def get_cycles(self):
        try:
            return int(self.cycles_entry.get())
        except ValueError:
            return 0
    
    def get_learning_rate(self):
        try:
            return float(self.learning_rate_entry.get())
        except ValueError:
            return 0.0
    
    def plot_mock_graph(self):
        fig, ax = plt.subplots()
        fig.patch.set_facecolor("#2E2E2E")
        ax.set_facecolor("#2E2E2E")
        ax.plot(range(10), np.exp(-np.linspace(0, 2, 10)), color="cyan")
        ax.set_title("Error Decay", color="white", fontsize=14)
        ax.set_xlabel("Cycles", color="white", fontsize=12)
        ax.set_ylabel("Error", color="white", fontsize=12)
        ax.tick_params(colors='white', labelsize=10)
        
        self.canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        self.canvas.draw()
    
    def train(self):
        pass
    
    def identify(self):
        self.result_label.config(text="Identified Character: L")
    
    def on_close(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("ABC Madaline")
    root.geometry("800x600")
    app = App(root)
    root.mainloop()
