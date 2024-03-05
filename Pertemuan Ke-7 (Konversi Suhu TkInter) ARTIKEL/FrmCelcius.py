from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
from celcius import *

class FrmCelcius:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES) 

# menambahkan label
        Label(mainFrame, text='Celcius:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=4, column=0, sticky=W, padx=5, pady=5)

# menambahkan textbox
        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=0, column=1, padx=5, pady=5)  

        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=2, column=1, padx=5, pady=5) 
        
        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=3, column=1, padx=5, pady=5) 

        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=4, column=1, padx=5, pady=5) 

# menambahkan button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)
           
    def onHitung(self):
        C = Celcius(int(self.txtCelcius.get()))

        F = C.get_fahrenheit()
        K = C.get_kelvin()
        R = C.get_reamur()

        self.txtFahrenheit.delete(0, END)
        self.txtFahrenheit.insert(END, str(F))

        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END, str(K))

        self.txtReamur.delete(0, END)
        self.txtReamur.insert(END, str(R))
               
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmCelcius(root, "Program Konversi Suhu Celcius")
    root.mainloop()