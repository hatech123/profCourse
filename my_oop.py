import tkinter as tk
class My_window:
    def __init__(self,n):
        self.n=n
    def show_window(self):
        self.window=tk.Tk()
        self.window.geometry('400x400')
        # self.window.mainloop()
    def mult(self):
        for i in range(self.n):
            self.show_window()
my_window=My_window(10)
window=tk.Tk()
my_window.mult()
window.mainloop()