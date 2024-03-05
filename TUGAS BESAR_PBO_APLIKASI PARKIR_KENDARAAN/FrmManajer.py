import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton, Scrollbar,ttk,VERTICAL,HORIZONTAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Users import Users
class FormManajer:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("650x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='USERNAME:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox USERNAME
        self.txtUSERNAME = Entry(mainFrame) 
        self.txtUSERNAME.grid(row=0, column=1, padx=5, pady=5) 
                
         # varchar 
        Label(mainFrame, text='PASSWORD:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox PASSWORD
        self.txtPASSWORD = Entry(mainFrame) 
        self.txtPASSWORD.grid(row=1, column=1, padx=5, pady=5)
                
         # enum 
        Label(mainFrame, text='ROLENAME:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtROLENAME = StringVar()
        CboROLENAME = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtROLENAME) 
        CboROLENAME.grid(row=2, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboROLENAME['values'] = ('admin','manajer','staff')
        CboROLENAME.current()

        Label(mainFrame, text='Untuk Membuat Password,Kunjungi situs:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='https://dnschecker.org/password-encryption-utility.php',font=("Arial",10)).grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Kemudian Copy password MD5',font=("Arial",10)).grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Cari', fg='white', bg='grey', command=self.onCari, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnSimpan = Button(mainFrame, text='Simpan', fg='white', bg='blue', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=1, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', fg='black', bg='yellow', command=self.onClear, width=10)
        self.btnClear.grid(row=2, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', fg='white', bg='red', command=self.onDelete, width=10)
        self.btnHapus.grid(row=3, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('iduser','username','password','rolename')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('iduser', text='iduser')
        self.tree.column('iduser', width="30")
        self.tree.heading('username', text='username')
        self.tree.column('username', width="250")
        self.tree.heading('password', text='password')
        self.tree.column('password', width="240")
        self.tree.heading('rolename', text='rolename')
        self.tree.column('rolename', width="100")
        # set tree position
        self.tree.grid(row=7, column=0, columnspan=4, sticky='nsew')
        # Tambahkan Scrollbar vertikal
        vsb = Scrollbar(mainFrame, orient="vertical", command=self.tree.yview)
        vsb.place(x=620, y=200, height=240)
        self.tree.configure(yscrollcommand=vsb.set)

        # Tambahkan Scrollbar horizontal
        hsb = Scrollbar(mainFrame, orient="horizontal", command=self.tree.xview)
        hsb.place(x=0, y=420, width=620)
        self.tree.configure(xscrollcommand=hsb.set)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtUSERNAME.delete(0,END)
        self.txtUSERNAME.insert(END,"")
                                
        self.txtPASSWORD.delete(0,END)
        self.txtPASSWORD.insert(END,"")
                                
        self.txtROLENAME.set("")
            
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data users
        obj = Users()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        username = self.txtUSERNAME.get()
        obj = Users()
        res = obj.getByUSERNAME(username)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        username = self.txtUSERNAME.get()
        obj = Users()
        res = obj.getByUSERNAME(username)
            
        self.txtPASSWORD.delete(0,END)
        self.txtPASSWORD.insert(END,obj.password)
                                
        self.txtROLENAME.set(obj.rolename)
            
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        username = self.txtUSERNAME.get()
        password = self.txtPASSWORD.get()
        rolename = self.txtROLENAME.get()       
        obj = Users()
        obj.username = username
        obj.password = password
        obj.rolename = rolename
        if(self.ditemukan==True):
            res = obj.updateByUSERNAME(username)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        username = self.txtUSERNAME.get()
        obj = Users()
        obj.username = username
        if(self.ditemukan==True):
            res = obj.deleteByUSERNAME(username)
            rec = obj.affected
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
    root = tk.Tk()
    aplikasi = FormManajer(root, "Aplikasi Data Users")
    root.mainloop()