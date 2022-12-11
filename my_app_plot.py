
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
from PIL import ImageTk
import numpy as np
from tkinter import filedialog
from tkinter.ttk import Radiobutton
import cv2


class APP(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("мой магазин")
        self.pack(fill=tk.BOTH, expand=1)

        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)

        self.label1 = tk.Label(self, border=15)
        self.label2 = tk.Label(self, border=15)
        self.label1.grid(row=1, column=1)
        self.label2.grid(row=1, column=2)
        fileMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Файл", menu=fileMenu)

        fileMenu.add_command(label="Выбрать товар", command=self.onOpen)
        fileMenu.add_command(label="Сохранить", command=self.saveImage)

        basicMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Информация о товаре", menu=basicMenu)

        basicMenu.add_command(label="Изменение цены товара", command=self.onPrice)
        basicMenu.add_command(label="Кол-во товара на складе", command=self.onNumber)
        basicMenu.add_command(label="Наличие товара", command=self.onMaguzen)

    def setImage(self):
        self.img = Image.open(self.fn)
        self.I = np.asarray(self.img)
        self.frame = cv2.imread(self.fn)
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        l, h = self.img.size
        text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
        self.parent.geometry(text)
        photo = ImageTk.PhotoImage(self.img)
        self.label1.configure(image=photo)
        self.label1.image = photo  # keep a reference!

    def onOpen(self):
        ftypes = [('Image Files', '*.tif *.jpg *.png')]
        dlg = filedialog.Open(self, filetypes=ftypes)
        filename = dlg.show()
        self.fn = filename
        self.setImage()

    def saveImage(self):
        self.edge = self.im
        filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if not filename:
            return
        self.edge.save(filename)

    def onPrice(self):


        data1 = {'Month': ['June', 'July', 'August'],
                 'Price': [45000, 42000, 52000]
                 }
        df1 = pd.DataFrame(data1)


        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.label2)
        bar1.get_tk_widget().grid(row=1, column=2)
        df1 = df1[['Month', 'Price']].groupby('Month').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Изменение цены')

    def onNumber(self):


        data1 = {'Month': ['June', 'July', 'August'],
                 'Number': [100, 200, 300]
                 }
        df1 = pd.DataFrame(data1)


        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.label2)
        bar1.get_tk_widget().grid(row=1, column=2)
        df1 = df1[['Month', 'Number']].groupby('Month').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Изменение количества')

    def onMaguzen(self):


        data1 = {'Shops': ['Sport', 'Xumukova', 'Adidas'],
                 'Number': [15, 20, 30]
                 }
        df1 = pd.DataFrame(data1)


        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.label2)
        bar1.get_tk_widget().grid(row=1, column=2)
        df1 = df1[['Shops', 'Number']].groupby('Shops').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Наличие в магазинах')


def main():
    root = tk.Tk()
    APP(root)
    root.geometry("320x240")
    root.mainloop()


if __name__ == '__main__':
    main()