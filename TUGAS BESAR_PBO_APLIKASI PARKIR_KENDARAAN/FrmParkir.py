import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Scrollbar,Radiobutton,ttk,VERTICAL,HORIZONTAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Parkir import Parkir
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import datetime  # Import datetime module
import win32print
import win32ui
import win32con
import qrcode
from PIL import Image, ImageDraw


class FormParkir:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("660x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='NOPOL        :').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOPOL
        self.txtNOPOL = Entry(mainFrame) 
        self.txtNOPOL.grid(row=0, column=1, padx=5, pady=5) 
                
         # date 
        Label(mainFrame, text='TANGGAL    :').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=1, column=1, padx=5, pady=5)
                    
         # enum 
        Label(mainFrame, text='JENIS            :').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtJENIS = StringVar()
        CboJENIS = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJENIS) 
        CboJENIS.grid(row=2, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboJENIS['values'] = ('Motor','Mobil')
        CboJENIS.current()
        
         # time 
        Label(mainFrame, text='MASUK        :').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtMASUK = StringVar()
        CboMASUK = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtMASUK) 
        CboMASUK.grid(row=3, column=1, padx=5, pady=5)
        # Get current time for MASUK
        current_time = datetime.now().strftime("%H:%M:%S")
        CboMASUK['values'] = (current_time,)
        CboMASUK.current(0)
        
         # time 
        Label(mainFrame, text='KELUAR       :').grid(row=3, column=2, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtKELUAR = StringVar()
        CboKELUAR = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtKELUAR) 
        CboKELUAR.grid(row=3, column=3, padx=5, pady=5)
        # Get current time for KELUAR
        CboKELUAR['values'] = (current_time,)
        CboKELUAR.current(0)
        
         # varchar 
        Label(mainFrame, text='TARIF           :').grid(row=5, column=2, sticky=W, padx=5, pady=5)
        # Textbox TARIF
        self.txtTARIF = Entry(mainFrame) 
        self.txtTARIF.grid(row=5, column=3, padx=5, pady=5)
                
        # Button
        self.btnCari = Button(mainFrame, text='Cari Nopol', fg='white', bg='grey', command=self.onCari, width=10)
        self.btnCari.grid(row=0, column=2, padx=5, pady=5)
        self.btnSimpan = Button(mainFrame, text='Simpan', fg='white', bg='blue', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=6, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', fg='black', bg='yellow', command=self.onClear, width=10)
        self.btnClear.grid(row=6, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', fg='white', bg='red', command=self.onDelete, width=10)
        self.btnHapus.grid(row=6, column=2, padx=5, pady=5)
        # Tombol Print
        self.btnPrintKartu = Button(mainFrame, text='Print Kartu', fg='white', bg='orange', command=self.onPrint1, width=10)
        self.btnPrintKartu.grid(row=1, column=2, padx=5, pady=5)
        self.btnPrint = Button(mainFrame, text='Print Semua', fg='black', bg='green', command=self.onPrint, width=10)
        self.btnPrint.grid(row=6, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','nopol','tanggal','jenis','masuk','keluar','tarif')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('nopol', text='nopol')
        self.tree.column('nopol', width="100")
        self.tree.heading('tanggal', text='tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('jenis', text='jenis')
        self.tree.column('jenis', width="100")
        self.tree.heading('masuk', text='masuk')
        self.tree.column('masuk', width="100")
        self.tree.heading('keluar', text='keluar')
        self.tree.column('keluar', width="100")
        self.tree.heading('tarif', text='tarif')
        self.tree.column('tarif', width="100")
        # set tree position
        self.tree.grid(row=7, column=0, columnspan=4, sticky='nsew')
        # Tambahkan Scrollbar vertikal
        vsb = Scrollbar(mainFrame, orient="vertical", command=self.tree.yview)
        vsb.place(x=630, y=195, height=240)
        self.tree.configure(yscrollcommand=vsb.set)

        # Tambahkan Scrollbar horizontal
        hsb = Scrollbar(mainFrame, orient="horizontal", command=self.tree.xview)
        hsb.place(x=0, y=420, width=630)
        self.tree.configure(xscrollcommand=hsb.set)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNOPOL.delete(0,END)
        self.txtNOPOL.insert(END,"")
                                
        self.txtJENIS.set("")
            
        self.txtTARIF.delete(0,END)
        self.txtTARIF.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data parkir
        obj = Parkir()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        nopol = self.txtNOPOL.get()
        obj = Parkir()
        res = obj.getByNOPOL(nopol)
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
        nopol = self.txtNOPOL.get()
        obj = Parkir()
        res = obj.getByNOPOL(nopol)
            
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.tanggal)
                                
        self.txtJENIS.set(obj.jenis)

        self.txtMASUK.set(obj.masuk) # Menampilkan waktu masuk yang tersimpan

        self.txtTARIF.delete(0,END)
        self.txtTARIF.insert(END,obj.tarif)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        nopol = self.txtNOPOL.get()
        tanggal = self.txtTANGGAL.get()
        jenis = self.txtJENIS.get()
        masuk = self.txtMASUK.get()
        keluar = self.txtKELUAR.get()
        # Konversi string waktu masuk dan keluar menjadi objek datetime
        masuk_time = datetime.strptime(masuk, "%H:%M:%S")
        keluar_time = datetime.strptime(keluar, "%H:%M:%S")
        
        # Hitung selisih waktu
        selisih = keluar_time - masuk_time
        
        # Hitung tarif berdasarkan jenis kendaraan
        if jenis == 'Motor':
            tarif_per_jam = 2000
        elif jenis == 'Mobil':
            tarif_per_jam = 4000
        else:
            messagebox.showwarning("Peringatan", "Jenis kendaraan tidak valid")
            return
        
        # Hitung tarif berdasarkan selisih waktu
        tarif_total = (selisih.total_seconds() / 3600) * tarif_per_jam
        
        # Tampilkan tarif yang dihitung pada kotak teks txtTARIF
        self.txtTARIF.delete(0, END)
        self.txtTARIF.insert(END, tarif_total)  

        obj = Parkir()
        obj.nopol = nopol
        obj.tanggal = tanggal
        obj.jenis = jenis
        obj.masuk = masuk
        obj.keluar = keluar
        obj.tarif = tarif_total
        if(self.ditemukan==True):
            res = obj.updateByNOPOL(nopol)
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
        nopol = self.txtNOPOL.get()
        obj = Parkir()
        obj.nopol = nopol
        if(self.ditemukan==True):
            res = obj.deleteByNOPOL(nopol)
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
            data_to_print = self.getDataToPrintKartu()
            self.printData(data_to_print)
        else:
            messagebox.showwarning("Peringatan", "Anda harus mencari data terlebih dahulu sebelum mencetak.")

    def getDataToPrintKartu(self):
        nopol = self.txtNOPOL.get()
        obj = Parkir()
        res = obj.getByNOPOL(nopol)
        data_to_print = [(obj.id, obj.nopol, obj.tanggal, obj.jenis, obj.masuk, obj.keluar, obj.tarif)]
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
        hdc.StartDoc(f"Document_Parkiran_{current_datetime}")
        hdc.StartPage()

        # Set posisi awal untuk mencetak
        x = 500
        y = 500
        line_height = 200

        # Buat font tebal untuk judul
        font = win32ui.CreateFont({
            "name": "Arial",
            "height":100,
            "weight": 700  # Weight 700 untuk bold
        })
        # Pilih font
        hdc.SelectObject(font)
        # Tambahkan teks "Aplikasi Data Parkir"
        hdc.TextOut(x, y, "                                                                     APLIKASI DATA PARKIR                                            ")
        # Pindahkan posisi y ke bawah
        y += line_height

        # Judul kolom
        headers = ['ID', 'NOPOL', 'TANGGAL', 'JENIS', 'MASUK', 'KELUAR', 'TARIF']
        for header_index, header in enumerate(headers):
                hdc.TextOut(x + (header_index * 600), y, str(header))
        
        # Pindahkan posisi y ke bawah
        y += line_height

        # Cetak data
        for row_index, row in enumerate(data):
            for column_index, item in enumerate(row):
                hdc.TextOut(x + (column_index * 600), y + (row_index * line_height), str(item))

        # Tambahkan komentar "Terima Kasih"
        hdc.TextOut(x, y + ((row_index + 3) * line_height), "==================================#Terima Kasih#==================================")
        
        # Tambahkan teks "dicetak otomatis melalui sistem" dalam miring
        italic_font = win32ui.CreateFont({
            "name": "Arial",
            "height": 100,
            "weight": 300,  # Weight 400 untuk normal
            "italic": 10  # Atur teks menjadi miring
        })
        hdc.SelectObject(italic_font)
        hdc.TextOut(x, y + ((row_index + 4) * line_height), "*dicetak otomatis melalui sistem")

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
    aplikasi = FormParkir(root, "Aplikasi Data Parkir")
    root.mainloop() 