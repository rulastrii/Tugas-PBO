from tkinter import Frame,Label,YES,BOTH,Tk,W

class FrmBio:
    def __init__(self, parent, title):
        self.parent = parent       

        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW")
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
#=============================================================================================
        Label(mainFrame, text="PBO Aplikasi Parkir").grid(row=0, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text=" ").grid(row=1, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Nama                 : ').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Rulastri').grid(row=2, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NIM                    :').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='220511071').grid(row=3, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelas                  : ").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Karyawan 1 (TI22L)").grid(row=4, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Semester           : ").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="3 (Tiga)").grid(row=5, column=1,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="="*20).grid(row=8, column=1,
            sticky=W, padx=5, pady=5)






if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmBio(root, "Biodata Pembuat")
    root.mainloop()