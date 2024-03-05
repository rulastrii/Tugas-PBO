from tkinter import Frame,Label,YES,BOTH,Tk,W

class FrmInfologin:
    def __init__(self, parent, title):
        self.parent = parent       

        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW")
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
#=============================================================================================
        Label(mainFrame, text="Info Login").grid(row=0, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text=" ").grid(row=1, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Username                 : ').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='-lastri06@gmail.com   |(Sebagai Petugas Parkir)').grid(row=2, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='-manajer@gmail.com |(Sebagai Manajer)').grid(row=3, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='-direktur@gmail.com  |(Sebagai Direktur)').grid(row=4, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Password                  : ").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="123").grid(row=5, column=1,
            sticky=W, padx=5, pady=5)


        Label(mainFrame, text="="*20).grid(row=8, column=1,
            sticky=W, padx=5, pady=5)






if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmInfologin(root, "Informasi Login")
    root.mainloop()