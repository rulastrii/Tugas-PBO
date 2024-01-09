# Nama file: FrmMatakuliah.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Matakuliah import Matakuliah
import os


os.system("cls")

class FormMatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("550x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Data Matakuliah Universitas Muhammadiyah Cirebon   ').grid(row=15, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE MK                   :').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Nama MK                  :').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Jumlah SKS                :').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtKODEMK = Entry(mainFrame) 
        self.txtKODEMK.grid(row=1, column=1, padx=5, pady=5) 
        self.txtKODEMK.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtNamaMK = Entry(mainFrame) 
        self.txtNamaMK.grid(row=2, column=1, padx=5, pady=5) 
        
        # Radio Button
        # self.txtJK = StringVar()
        # self.L = Radiobutton(mainFrame, text='Laki-laki', value='L', variable=self.txtJK)
        # self.L.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        # self.L.select() # set pilihan yg pertama
        # self.P = Radiobutton(mainFrame, text='Perempuan', value='P', variable=self.txtJK)
        # self.P.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        
       
        # Combo Box
        self.txtSKS = StringVar()
        Cbo = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtSKS) 
        Cbo.grid(row=3, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        Cbo['values'] = ('1','2', '3', '4')
        Cbo.current()
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Save', command=self.onSimpan, width=10,  fg= "white", bg="blue")
        self.btnSimpan.grid(row=6, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10,  fg= "black", bg="yellow")
        self.btnClear.grid(row=6, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Delete', command=self.onDelete, width=10,  fg= "white", bg="red")
        self.btnHapus.grid(row=6, column=2, padx=5, pady=5)
        self.btnCari = Button(mainFrame, text='Cari KODE MK', command=self.onCari, width=10,  fg= "white", bg="green")
        self.btnCari.grid(row=1, column=2, padx=5, pady=5)

        # define columns
        columns = ('id', 'kodemk', 'namamk','sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='No')
        self.tree.column('id', width="30")
        self.tree.heading('kodemk', text='KODE MK')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='Nama MK')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='Jumlah SKS')
        self.tree.column('sks', width="100")
        # set tree position
        self.tree.place(x=80, y=165)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtKODEMK.delete(0,END)
        self.txtKODEMK.insert(END,"")
        self.txtNamaMK.delete(0,END)
        self.txtNamaMK.insert(END,"")       
        self.txtSKS.set("")
        self.btnSimpan.config(text="Simpan")
        # self.L.select()
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data Matakuliah
        mk = Matakuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kodemk = self.txtKODEMK.get()
        mk = Matakuliah()
        res = mk.getByNIM(kodemk)
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNamaMK.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtKODEMK.get()
        mk = Matakuliah()
        res = mk.getByNIM(kodemk)
        self.txtNamaMK.delete(0,END)
        self.txtNamaMK.insert(END,mk.namamk)
        # jk = mk.jk
        # if(jk=="P"):
        #    self.P.select()
        # else:
        #    self.L.select()
        self.txtSKS.set(mk.sks)   
        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        kodemk = self.txtKODEMK.get()
        namamk = self.txtNamaMK.get()
        # jk = self.txtJK.get()
        sks = self.txtSKS.get()
        
        mk = Matakuliah()
        mk.kodemk = kodemk
        mk.namamk = namamk
        # mk.jk = jk
        mk.sks = sks
        if(self.ditemukan==True):
            res = mk.updateByNIM(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtKODEMK.get()
        mk = Matakuliah()
        mk.kodemk = kodemk
        if(self.ditemukan==True):
            res = mk.deleteByNIM(kodemk)
            rec = mk.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FormMatakuliah(root2, "Aplikasi Data Matakuliah")
    root2.mainloop() 
