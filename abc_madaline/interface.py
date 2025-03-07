from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from abc_madaline.Madaline import Madaline
from data.data import get_matrices

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
        
        self.header = Label(self.left_frame, text="ABC Madaline", bg="#2E2E2E", fg="white", font=('Verdana', '20', 'bold'))
        self.header.pack(pady=5)
        
        self.matrix_container = Frame(self.left_frame, bg="#2E2E2E")
        self.matrix_container.pack()
        self.matrix = Frame(self.matrix_container, bg="#2E2E2E")
        self.matrix.pack()
        
        self.checkboxes = []
        for i in range(9):
            row = []
            for j in range(7):
                var = IntVar()
                c = Checkbutton(self.matrix, variable=var, bg="#2E2E2E", fg="white", selectcolor="#555555",
                                width=2, height=1, padx=3, pady=1, indicatoron=0)
                c.grid(row=i, column=j, padx=3, pady=3)
                row.append(var)
            self.checkboxes.append(row)
        
        self.inputs_frame = Frame(self.left_frame, bg="#2E2E2E")
        self.inputs_frame.pack(pady=10, fill=X)
        
        Label(self.inputs_frame, text="Training Type:", bg="#2E2E2E", fg="white", font=('Verdana', '12')).grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.train_type = StringVar()
        self.train_type.set("By Epoch")
        self.train_type_menu = OptionMenu(self.inputs_frame, self.train_type, "By Epoch", "By Error Threshold")
        self.train_type_menu.config(bg="#555555", fg="white", font=('Verdana', '12'))
        self.train_type_menu.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        Label(self.inputs_frame, text="Epochs:", bg="#2E2E2E", fg="white", font=('Verdana', '12')).grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.epochs = Entry(self.inputs_frame, bg="#555555", fg="white", insertbackground="white", font=('Verdana', '12'))
        self.epochs.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        Label(self.inputs_frame, text="Learning Rate:", bg="#2E2E2E", fg="white", font=('Verdana', '12')).grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.learning_rate_entry = Entry(self.inputs_frame, bg="#555555", fg="white", insertbackground="white", font=('Verdana', '12'))
        self.learning_rate_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        
        Label(self.inputs_frame, text="Error Threshold:", bg="#2E2E2E", fg="white", font=('Verdana', '12')).grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.error_threshold_entry = Entry(self.inputs_frame, bg="#555555", fg="white", insertbackground="white", font=('Verdana', '12'))
        self.error_threshold_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        
        Label(self.inputs_frame, text="Select Letter:", bg="#2E2E2E", fg="white", font=('Verdana', '12')).grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.selected_letter = StringVar()
        self.selected_letter.set("A1") 

        self.letters_data = get_matrices() 
        letters_options = list(self.letters_data.keys())

        self.letter_menu = OptionMenu(self.inputs_frame, self.selected_letter, *letters_options, command=self.fill_matrix_from_selection)
        self.letter_menu.config(bg="#555555", fg="white", font=('Verdana', '12'))
        self.letter_menu.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        self.fill_matrix_from_selection("A1")

        self.buttons = Frame(self.left_frame, bg="#2E2E2E")
        self.buttons.pack(pady=10)
        
        self.train_button = Button(self.buttons, text="Train", command=self.train, bg="#555555", fg="white", font=('Verdana', '12', 'bold'))
        self.train_button.pack(side=LEFT, padx=5)
        
        self.clear_button = Button(self.buttons, text="Clear", command=self.clear, bg="#555555", fg="white", font=('Verdana', '12', 'bold'))
        self.clear_button.pack(side=LEFT, padx=5)
        
        self.identify_button = Button(self.buttons, text="Identify", command=self.identify, bg="#555555", fg="white", font=('Verdana', '12', 'bold'))
        self.identify_button.pack(side=LEFT, padx=5)
        
        self.result_label = Label(self.left_frame, text="Identified Character: ", bg="#2E2E2E", fg="white", font=('Verdana', '14', 'bold'))
        self.result_label.pack(pady=5)
        
        self.right_frame = Frame(self.container, bg="#2E2E2E")
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=20, pady=20)

        self.madaline = None
        
    def clear(self):
        for row in self.checkboxes:
            for checkbox in row:
                checkbox.set(0)
                
    def get_matrix(self):
        return np.array([[checkbox.get() for checkbox in row] for row in self.checkboxes]).flatten()
    
    def get_epochs(self):
        try:
            return int(self.epochs.get())
        except ValueError:
            return 20
    
    def get_error_threshold(self):
        try:
            return float(self.error_threshold_entry.get())
        except ValueError:
            return 0.01
    
    def get_learning_rate(self):
        try:
            return float(self.learning_rate_entry.get())
        except ValueError:
            return 0.01
    
    def get_train_type(self):
        return self.train_type.get() == "By Epoch"
    
    def fill_matrix_from_selection(self, selected):
        if selected in self.letters_data:
            matrix = self.letters_data[selected] 

            for i in range(9):
                for j in range(7):
                    self.checkboxes[i][j].set(matrix[i, j])


    def plot_graph(self, X, y):
        if hasattr(self, 'canvas') and self.canvas is not None:
            self.canvas.get_tk_widget().destroy()
        
        fig, ax = plt.subplots()
        fig.patch.set_facecolor("#2E2E2E")
        ax.set_facecolor("#2E2E2E")
        ax.plot(X, y, color="cyan")
        ax.set_title("Error Decay", color="white", fontsize=14)
        ax.set_xlabel("Cycles", color="white", fontsize=12)
        ax.set_ylabel("Error", color="white", fontsize=12)
        ax.tick_params(colors='white', labelsize=10)

        self.canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        self.canvas.draw()

    def train(self):
        by_epoch = self.get_train_type()
        self.madaline = Madaline(learning_rate=self.get_learning_rate(), epochs=self.get_epochs())
        self.madaline.train(by_epoch=by_epoch, error_threshold=self.get_error_threshold())
        self.plot_graph(self.madaline.X_error_axis, self.madaline.y_error_axis)
    
    def identify(self):
        if self.madaline is None:
            self.result_label.config(text="Please train the model first.")
            return
        else:
            x = self.get_matrix()
            result = self.madaline.identify(x)
            self.result_label.config(text=f'Identified Character: {result}')
    
    def on_close(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("ABC Madaline")
    root.geometry("800x600")
    app = App(root)
    root.mainloop()
