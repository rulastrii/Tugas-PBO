import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Scrollbar,Radiobutton,ttk,VERTICAL,HORIZONTAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Lapor import Lapor
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import datetime  # Import datetime module
import win32print # Import print
import win32ui # import ui print

class FormLapor:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("710x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # varchar 
        Label(mainFrame, text='NOPOLHILANG      :').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOPOLHILANG
        self.txtNOPOLHILANG = Entry(mainFrame) 
        self.txtNOPOLHILANG.grid(row=0, column=1, padx=5, pady=5) 
        
                
        # varchar
        Label(mainFrame, text='KETERANGAN         :').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox KETERANGAN
        self.txtKETERANGAN = Entry(mainFrame) 
        self.txtKETERANGAN.grid(row=1, column=1, padx=5, pady=5)
                
        # date
        Label(mainFrame, text='TANGGAL                :').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=2, column=1, padx=5, pady=5)
                    
        # time
        Label(mainFrame, text='JAMLAPOR              :').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtJAMLAPOR = StringVar()
        CboJAMLAPOR = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJAMLAPOR) 
        CboJAMLAPOR.grid(row=3, column=1, padx=5, pady=5)
        # Set current time to JAMLAPOR
        current_time = datetime.now().strftime("%H:%M:%S")
        CboJAMLAPOR['values'] = (current_time,)
        CboJAMLAPOR.current(0)
        
        # enum
        Label(mainFrame, text='JENIS                         :').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtJENIS = StringVar()
        CboJENIS = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJENIS) 
        CboJENIS.grid(row=4, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboJENIS['values'] = ('Motor','Mobil')
        CboJENIS.current()
        
        # enum
        Label(mainFrame, text='BUKTI                :').grid(row=4, column=2, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtBUKTI = StringVar()
        CboBUKTI = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtBUKTI) 
        CboBUKTI.grid(row=4, column=3, padx=5, pady=5)
        # Adding combobox drop down list
        CboBUKTI['values'] = ('STNK','BPKB','Faktur','Surat Beli')
        CboBUKTI.current()
        
        # Button
        self.btnCari = Button(mainFrame, text='Cari Nopol', fg='white', bg='grey', command=self.onCari, width=10)
        self.btnCari.grid(row=0, column=2, padx=5, pady=5)
        self.btnSimpan = Button(mainFrame, text='Simpan', fg='white', bg='blue', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=6, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', fg='black', bg='yellow', command=self.onClear, width=10)
        self.btnClear.grid(row=6, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', fg='white', bg='red', command=self.onDelete, width=10)
        self.btnHapus.grid(row=6, column=2, padx=5, pady=5)
        # Tombol print
        self.btnPrintLaporan = Button(mainFrame, text='Print Laporan', fg='white', bg='orange', command=self.onPrint1, width=10)
        self.btnPrintLaporan.grid(row=1, column=2, padx=5, pady=5)
        self.btnPrintSemua = Button(mainFrame, text='Print Semua', fg='black', bg='green', command=self.onPrint, width=10)
        self.btnPrintSemua.grid(row=6, column=3, padx=5, pady=5)

        # define columns
        columns = ('id','nopolhilang','keterangan','tanggal','jamlapor','jenis','bukti')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('nopolhilang', text='nopolhilang')
        self.tree.column('nopolhilang', width="100")
        self.tree.heading('keterangan', text='keterangan')
        self.tree.column('keterangan', width="150")
        self.tree.heading('tanggal', text='tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('jamlapor', text='jamlapor')
        self.tree.column('jamlapor', width="100")
        self.tree.heading('jenis', text='jenis')
        self.tree.column('jenis', width="100")
        self.tree.heading('bukti', text='bukti')
        self.tree.column('bukti', width="100")
        # set tree position
        self.tree.grid(row=7, column=0, columnspan=4, sticky='nsew')
        # Tambahkan Scrollbar vertikal
        vsb = Scrollbar(mainFrame, orient="vertical", command=self.tree.yview)
        vsb.place(x=680, y=195, height=240)
        self.tree.configure(yscrollcommand=vsb.set)

        # Tambahkan Scrollbar horizontal
        hsb = Scrollbar(mainFrame, orient="horizontal", command=self.tree.xview)
        hsb.place(x=0, y=420, width=680)
        self.tree.configure(xscrollcommand=hsb.set)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNOPOLHILANG.delete(0,END)
        self.txtNOPOLHILANG.insert(END,"")
                                
        self.txtKETERANGAN.delete(0,END)
        self.txtKETERANGAN.insert(END,"")
                                
        self.txtJENIS.set("")
            
        self.txtBUKTI.set("")
            
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data lapor
        obj = Lapor()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        nopolhilang = self.txtNOPOLHILANG.get()
        obj = Lapor()
        res = obj.getByNOPOLHILANG(nopolhilang)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
        return res
            
    def TampilkanData(self, event=None):
        nopolhilang = self.txtNOPOLHILANG.get()
        obj = Lapor()
        res = obj.getByNOPOLHILANG(nopolhilang)
            
        self.txtKETERANGAN.delete(0,END)
        self.txtKETERANGAN.insert(END,obj.keterangan)
                                
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.tanggal)
                                
        self.txtJENIS.set(obj.jenis)
            
        self.txtJAMLAPOR.set(obj.jamlapor) # Menampilkan waktu jamlapor yang tersimpan
        
        self.txtBUKTI.set(obj.bukti)
            
        self.btnSimpan.config(text="Update")
        
    def onSimpan(self, event=None):
        nopolhilang = self.txtNOPOLHILANG.get()
        keterangan = self.txtKETERANGAN.get()
        tanggal = self.txtTANGGAL.get()
        jamlapor = self.txtJAMLAPOR.get()
        jenis = self.txtJENIS.get()
        bukti = self.txtBUKTI.get()       
        obj = Lapor()
        obj.nopolhilang = nopolhilang
        obj.keterangan = keterangan
        obj.tanggal = tanggal
        obj.jamlapor = jamlapor
        obj.jenis = jenis
        obj.bukti = bukti
        if(self.ditemukan==True):
            res = obj.updateByNOPOLHILANG(nopolhilang)
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
        nopolhilang = self.txtNOPOLHILANG.get()
        obj = Lapor()
        obj.nopolhilang = nopolhilang
        if(self.ditemukan==True):
            res = obj.deleteByNOPOLHILANG(nopolhilang)
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
            data_to_print = self.getDataToPrintLapor()
            self.printData(data_to_print)
        else:
            messagebox.showwarning("Peringatan", "Anda harus mencari data terlebih dahulu sebelum mencetak.")

    def getDataToPrintLapor(self):
        nopol = self.txtNOPOLHILANG.get()
        obj = Lapor()
        res = obj.getByNOPOLHILANG(nopol)
        data_to_print = [(obj.id, obj.nopolhilang, obj.keterangan, obj.tanggal, obj.jamlapor, obj.jenis, obj.bukti)]
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
        hdc.StartDoc(f"Document_Laporan_Kehilangan_{current_datetime}")
        hdc.StartPage()

        # Set posisi awal untuk mencetak
        x = 500
        y = 500
        line_height = 200

        # Buat font tebal untuk judul
        font = win32ui.CreateFont({
            "name": "Arial",
            "height":80,
            "weight": 900  # Weight 700 untuk bold
        })
        # Pilih font
        hdc.SelectObject(font)
        # Tambahkan teks "Aplikasi Data Parkir"
        hdc.TextOut(x, y, "                                                                                   DATA LAPORAN KEHILANGAN                                            ")
        # Pindahkan posisi y ke bawah
        y += line_height

        # Judul kolom
        headers = ['ID', 'NOPOL', 'KETERANGAN', 'TANGGAL', 'JAMLAPOR', 'JENIS', 'BUKTI']
        for header_index, header in enumerate(headers):
                hdc.TextOut(x + (header_index * 600), y, str(header))
        
        # Pindahkan posisi y ke bawah
        y += line_height

        # Cetak data
        for row_index, row in enumerate(data):
            for column_index, item in enumerate(row):
                hdc.TextOut(x + (column_index * 600), y + (row_index * line_height), str(item))

        # Tambahkan komentar "Terima Kasih"
        hdc.TextOut(x, y + ((row_index + 4) * line_height), "========================================#Terima Kasih Telah Melapor#========================================")
        
        # Tambahkan teks "dicetak otomatis melalui sistem" dalam miring
        italic_font = win32ui.CreateFont({
            "name": "Arial",
            "height": 70,
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
    aplikasi = FormLapor(root, "Aplikasi Data Lapor")
    root.mainloop()
