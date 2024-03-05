import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,Scrollbar,ttk,VERTICAL,HORIZONTAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Upah import Upah
from tkcalendar import Calendar, DateEntry
from datetime import datetime  # Import datetime module
import win32print # Import print
import win32ui # import ui print

class FormUpah:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("660x420")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='NAMA:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA
        self.txtNAMA = Entry(mainFrame) 
        self.txtNAMA.grid(row=0, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='USERNAME:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox USERNAME
        self.txtUSERNAME = Entry(mainFrame) 
        self.txtUSERNAME.grid(row=1, column=1, padx=5, pady=5) 
                
         # enum 
        Label(mainFrame, text='ROLENAME:').grid(row=1, column=2, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtROLENAME = StringVar()
        CboROLENAME = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtROLENAME) 
        CboROLENAME.grid(row=1, column=3, padx=5, pady=5)
        # Adding combobox drop down list
        CboROLENAME['values'] = ('petugas','manajer','direktur')
        CboROLENAME.current()
        
         # enum 
        Label(mainFrame, text='STATUS:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtSTATUS = StringVar()
        CboSTATUS = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtSTATUS) 
        CboSTATUS.grid(row=3, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboSTATUS['values'] = ('Tetap','Tidak Tetap')
        CboSTATUS.current()
        
         # enum 
        Label(mainFrame, text='GAJI:').grid(row=3, column=2, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtGAJI = StringVar()
        CboGAJI = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtGAJI) 
        CboGAJI.grid(row=3, column=3, padx=5, pady=5)
        # Adding combobox drop down list
        CboGAJI['values'] = ('Rp 500.000','Rp 1.500.000','Rp 2.500.000','Rp 3.000.000')
        CboGAJI.current()
        
         # Button
        self.btnCari = Button(mainFrame, text='Cari  Username', fg='white', bg='grey', command=self.onCari, width=10)
        self.btnCari.grid(row=0, column=2, padx=5, pady=5)
        self.btnSimpan = Button(mainFrame, text='Simpan', fg='white', bg='blue', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=5, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', fg='black', bg='yellow', command=self.onClear, width=10)
        self.btnClear.grid(row=5, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', fg='white', bg='red', command=self.onDelete, width=10)
        self.btnHapus.grid(row=5, column=2, padx=5, pady=5)
        # Tombol print
        self.btnPrintSlipGaji = Button(mainFrame, text='Print Slip Gaji', fg='white', bg='orange', command=self.onPrint1, width=10)
        self.btnPrintSlipGaji.grid(row=0, column=3, padx=5, pady=5)
        self.btnPrintSemua = Button(mainFrame, text='Print Semua', fg='black', bg='green', command=self.onPrint, width=10)
        self.btnPrintSemua.grid(row=5, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','nama','username','rolename','status','gaji')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('nama', text='nama')
        self.tree.column('nama', width="150")
        self.tree.heading('username', text='username')
        self.tree.column('username', width="150")
        self.tree.heading('rolename', text='rolename')
        self.tree.column('rolename', width="100")
        self.tree.heading('status', text='status')
        self.tree.column('status', width="100")
        self.tree.heading('gaji', text='gaji')
        self.tree.column('gaji', width="100")
        # set tree position
        self.tree.grid(row=7, column=0, columnspan=4, sticky='nsew')
        # Tambahkan Scrollbar vertikal
        vsb = Scrollbar(mainFrame, orient="vertical", command=self.tree.yview)
        vsb.place(x=620, y=130, height=240)
        self.tree.configure(yscrollcommand=vsb.set)

        # Tambahkan Scrollbar horizontal
        hsb = Scrollbar(mainFrame, orient="horizontal", command=self.tree.xview)
        hsb.place(x=0, y=350, width=620)
        self.tree.configure(xscrollcommand=hsb.set)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,"")
                                
        self.txtUSERNAME.delete(0,END)
        self.txtUSERNAME.insert(END,"")
                                
        self.txtROLENAME.set("")
            
        self.txtSTATUS.set("")
            
        self.txtGAJI.set("")
            
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data upah
        obj = Upah()
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
        obj = Upah()
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
        obj = Upah()
        res = obj.getByUSERNAME(username)
            
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,obj.nama)
                                
        self.txtROLENAME.set(obj.rolename)
            
        self.txtSTATUS.set(obj.status)
            
        self.txtGAJI.set(obj.gaji)
            
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        nama = self.txtNAMA.get()
        username = self.txtUSERNAME.get()
        rolename = self.txtROLENAME.get()
        status = self.txtSTATUS.get()
        gaji = self.txtGAJI.get()       
        obj = Upah()
        obj.nama = nama
        obj.username = username
        obj.rolename = rolename
        obj.status = status
        obj.gaji = gaji
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
        obj = Upah()
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
    # Print by Data
    def onPrint1(self):
        if self.ditemukan:
            data_to_print = self.getDataToPrintUpah()
            self.printData(data_to_print)
        else:
            messagebox.showwarning("Peringatan", "Anda harus mencari data terlebih dahulu sebelum mencetak.")

    def getDataToPrintUpah(self):
        nopol = self.txtUSERNAME.get()
        obj = Upah()
        res = obj.getByUSERNAME(nopol)
        data_to_print = [(obj.id, obj.nama, obj.username, obj.rolename, obj.status, obj.gaji)]
        return data_to_print

    # Print All Data
    def onPrint(self):
        # Ambil data yang ingin dicetak
        data_to_print = self.getDataToPrint()

        # Cetak data
        self.printData(data_to_print)

    def getDataToPrint(self):
        # Ambil data dari entri, pohon, atau komponen lain yang relevan
        # Misalnya, ambil data dari Treeview
        data_to_print = []
        for item in self.tree.get_children():
            data = self.tree.item(item)['values']
            data_to_print.append(data)
        return data_to_print

    def printData(self, data):
        # Get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Inisialisasi printer
        printer_name = win32print.GetDefaultPrinter()
        hprinter = win32print.OpenPrinter(printer_name)
        printer_info = win32print.GetPrinter(hprinter, 2)
        printer_info['pDevMode'].Duplex = 1  # Set duplexer (for duplex printers)

        # Mulai pencetakan
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)
        # Get current date and time
        hdc.StartDoc(f"Document_Laporan_Gaji_{current_datetime}")
        hdc.StartPage()

        # Set posisi awal untuk mencetak
        x = 500
        y = 500
        line_height = 200

        # Buat font tebal untuk judul
        font = win32ui.CreateFont({
            "name": "Arial",
            "height":70,
            "weight": 900  # Weight 700 untuk bold
        })
        # Pilih font
        hdc.SelectObject(font)
        # Tambahkan teks "Aplikasi Data Parkir"
        hdc.TextOut(x, y, "                                                                                              DATA LAPORAN GAJI                                            ")
        # Pindahkan posisi y ke bawah
        y += line_height

        # Judul kolom
        headers = ['ID', 'NAMA', 'USERNAME', 'ROLENAME', 'STATUS', 'GAJI']
        for header_index, header in enumerate(headers):
                hdc.TextOut(x + (header_index * 600), y, str(header))
        
        # Pindahkan posisi y ke bawah
        y += line_height

        # Cetak data
        for row_index, row in enumerate(data):
            for column_index, item in enumerate(row):
                hdc.TextOut(x + (column_index * 600), y + (row_index * line_height), str(item))

        # Tambahkan komentar "Terima Kasih"
        hdc.TextOut(x, y + ((row_index + 4) * line_height), "===============================================*Terima Kasih*==============================================")
    
        # Tambahkan teks "dicetak otomatis melalui sistem" dalam miring
        italic_font = win32ui.CreateFont({
            "name": "Arial",
            "height": 60,
            "weight": 300,  # Weight 400 untuk normal
            "italic": 10  # Atur teks menjadi miring
        })
        hdc.SelectObject(italic_font)
        hdc.TextOut(x, y + ((row_index + 5) * line_height), "*dicetak otomatis melalui sistem")

        # Akhiri pencetakan
        hdc.EndPage()
        hdc.EndDoc()
        hdc.DeleteDC()
        win32print.ClosePrinter(hprinter)
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormUpah(root, "Aplikasi Data Upah")
    root.mainloop()