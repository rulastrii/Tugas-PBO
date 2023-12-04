'''
Nama    : Rulastri
Kelas   : TI22L
NIM     : 220511071
'''

from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import tkinter as tk


class KonversiSuhu:
    def __init__(self, parent, title):
        self.parent = parent       

        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
#=============================================================================================
        Label(mainFrame, text="Mari Mengkonversi Suhu❤️").grid(row=0, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Celcius :').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Farenheit  :').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin :").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur :").grid(row=7, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="="*20).grid(row=8, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Suhu Dalam Celcius =").grid(row=9, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Suhu Dalam Reamur =").grid(row=10, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Suhu Dalam Farenheit =").grid(row=11, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Suhu Dalam Kelvin =").grid(row=12, column=0,
            sticky=W, padx=5, pady=5)

#=============================================================================================
        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=1, column=1, padx=5, pady=5) 

        self.txtFarenheit = Entry(mainFrame) 
        self.txtFarenheit.grid(row=3, column=1, padx=5, pady=5) 

        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=5, column=1, padx=5, pady=5) 

        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=7, column=1, padx=5, pady=5) 

        self.txtDalamCelcius = Entry(mainFrame) 
        self.txtDalamCelcius.grid(row=9, column=1, padx=5, pady=5) 

        self.txtDalamReamur = Entry(mainFrame) 
        self.txtDalamReamur.grid(row=10, column=1, padx=5, pady=5) 

        self.txtDalamFarenheit = Entry(mainFrame) 
        self.txtDalamFarenheit.grid(row=11, column=1, padx=5, pady=5)

        self.txtDalamKelvin = Entry(mainFrame) 
        self.txtDalamKelvin.grid(row=12, column=1, padx=5, pady=5) 

#=============================================================================================

        self.btnHitung = Button(mainFrame, text='Konversikan Suhu Celcius',  fg= "white", bg="blue",
            command=self.onHitung3)
        self.btnHitung.grid(row=7, column=2, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Konversikan Suhu Farenheit', fg= "black", bg="red",
            command=self.onHitung)
        self.btnHitung.grid(row=8, column=2, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Konversikan Suhu Kelvin',  fg= "white", bg="green",
            command=self.onHitung1)
        self.btnHitung.grid(row=9, column=2, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Konversikan Suhu Reamur',  fg= "black", bg="yellow",
            command=self.onHitung2)
        self.btnHitung.grid(row=10, column=2, padx=5, pady=5)


#=============================================================================================

    def onHitung(self, event=None):
        farenheit = float(self.txtFarenheit.get())
        
        celcius1 = 5/9 * (farenheit - 32)
        kelvin1 = 5/9 * (farenheit - 32) +273
        reamur1 = 4/9 * (farenheit - 32)
        self.txtDalamCelcius.delete(0,END)
        self.txtDalamCelcius.insert(END,str(celcius1))
        self.txtDalamKelvin.delete(0,END)
        self.txtDalamKelvin.insert(END,str(kelvin1))
        self.txtDalamReamur.delete(0,END)
        self.txtDalamReamur.insert(END,str(reamur1))

    def onHitung1(self, event=None):
        kelvin = float(self.txtKelvin.get())
        
        celcius2 = kelvin - 273
        farenheit1 = 9/5 * (kelvin - 273) + 32
        reamur2 = 4/5 * (kelvin - 273)
        self.txtDalamCelcius.delete(0,END)
        self.txtDalamCelcius.insert(END,str(celcius2))
        self.txtDalamFarenheit.delete(0,END)
        self.txtDalamFarenheit.insert(END,str(farenheit1))
        self.txtDalamReamur.delete(0,END)
        self.txtDalamReamur.insert(END,str(reamur2))

    def onHitung2(self, event=None):
        reamur = float(self.txtReamur.get())
        
        celcius3 = 5/4 * reamur
        farenheit2 = (9/4 * reamur) + 32
        kelvin2 = (5/4 * reamur) + 273
        self.txtDalamCelcius.delete(0,END)
        self.txtDalamCelcius.insert(END,str(celcius3))
        self.txtDalamFarenheit.delete(0,END)
        self.txtDalamFarenheit.insert(END,str(farenheit2))
        self.txtDalamKelvin.delete(0,END)
        self.txtDalamKelvin.insert(END,str(kelvin2,))

    def onHitung3(self, event=None):
        celcius = float(self.txtCelcius.get())
        
        farenheit3 = (9/5 * celcius) + 32
        kelvin3 = celcius + 273
        reamur3 = 4/5 * celcius
        self.txtDalamFarenheit.delete(0,END)
        self.txtDalamFarenheit.insert(END,str(farenheit3))
        self.txtDalamKelvin.delete(0,END)
        self.txtDalamKelvin.insert(END,str(kelvin3))
        self.txtDalamReamur.delete(0,END)
        self.txtDalamReamur.insert(END,str(reamur3))

#=============================================================================================
    def onKeluar(self, event=None):

        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = KonversiSuhu(root, "Aplikasi Mengkonversi Suhu")
    root.mainloop()