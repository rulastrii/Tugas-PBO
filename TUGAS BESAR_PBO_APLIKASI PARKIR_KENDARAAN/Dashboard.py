# Tambahkan fungsi menu Petugas, menu Manager, dan menu direktur
# Update script onLogin
# Tambahkan fungsi onLogout

import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from FrmBio import *
from FrmDirektur2 import *
from FrmInfologin import *
from FrmLapor import *
from FrmManajer import *
from FrmManajer2 import *
from FrmParkir import *
from FrmUsers import *
from FrmUpah import *
from PIL import Image,ImageTk
from Users import *



class Dashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1350x600")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.my_w_child = None
        self.aturKomponen()

    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg="blue")

        gambar = Image.open('Source\\P1.png')
        resized = gambar.resize((300,300))
        photo = ImageTk.PhotoImage(resized)
        label_gambar = tk.Label(image=photo, bg="blue")
        label_gambar.image = photo
        label_gambar.place(x=500, y=20)

        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)
        file_menu1 = Menu(mainmenu)
        
        #Teks Parkir
        teks = tk.Label(text="Aplikasi Parkir\n(Motor & Mobil)",font=('arial bold',30), bg='blue', fg='white')
        teks.place(x=500, y=350)
        
        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)
        file_menu_awal = Menu(mainmenu)
        file_menu_awal
        # Menu Awal
        file_menu_awal.add_command(
            label='📝Registrasi', command= lambda: self.new_window("Registrasi User", FormUsers)
        )
        file_menu_awal.add_command(
            label='🔓Login', command=self.show_login
        )
        file_menu_awal.add_command(
            label='🔐Logout', command=root.destroy
        )
       
        
        # Tampilkan menu ke layar
        mainmenu.add_cascade(
            label="📖|Menu", menu=file_menu_awal
        )     
        mainmenu.add_cascade(
            label='👶|Biodata', command= lambda: self.new_window("Biodata Pengembang", FrmBio)
        )     
        mainmenu.add_cascade(
            label='ℹ️|Info Login', command= lambda: self.new_window("Informasi Login", FrmInfologin)
        )     


    def menuPetugas(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        petugas_menu = Menu(menubar)

        # Menu File
        file_menu.add_command(
            label='🔐Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='🚪Exit', command=root.destroy
        )

      
        # Menu Petugas
        petugas_menu.add_command(
            label='Data Parkiran', command= lambda: self.new_window("Daftar Kendaraan Di Parkiran", FormParkir)
        )
        petugas_menu.add_command(
            label='Data Laporan', command= lambda: self.new_window("Daftar Laporan Kehilangan Kendaraan", FormLapor)
        )


        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="Main Menu", menu=file_menu
        )
        
        menubar.add_cascade(
            label="💁Menu petugas", menu=petugas_menu
        )
       

    def menuManajer(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        manajer_menu = Menu(menubar)
        
        # Menu File
        file_menu.add_command(
            label='🔐Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='🚪Exit', command=root.destroy
        )

      

        # Menu Manajer
        manajer_menu.add_command(
            label='Data Karyawan Akses', command= lambda: self.new_window("Daftar Karyawan", FormManajer)
        )
        manajer_menu.add_command(
            label='Data Absensi Karyawan', command= lambda: self.new_window("Daftar Absensi", FrmManajer2)
        )
        

        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="Main Menu", menu=file_menu
        )    
        menubar.add_cascade(
            label="💁Menu Manajer", menu=manajer_menu
        )
             

    def menuDirektur(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        direktur_menu = Menu(menubar)

        # Menu File
       
        file_menu.add_command(
            label='🔐Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='🚪Exit', command=root.destroy
        )

      
        # Menu direktur
        direktur_menu.add_command(
            label='Data Gaji', command= lambda: self.new_window("Daftar Gaji Karyawan", FormUpah)
        )
        direktur_menu.add_command(
            label='Data Kebutuhan Parkiran', command= lambda: self.new_window("Daftar Kebutuhan", FrmDirektur2)
        )
        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="Main Menu", menu=file_menu
        )
        menubar.add_cascade(
            label="💁Menu Direktur", menu=direktur_menu
        )
        
    def show_login(self):
        self.my_w_child=tk.Toplevel(root)
        self.my_w_child.geometry("300x200") 
        # pasang Label
        Label(self.my_w_child, text='Username:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)

        Label(self.my_w_child, text="Password:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtUsername = Entry(self.my_w_child) 
        self.txtUsername.grid(row=0, column=1, padx=5, pady=5)

        self.txtPassword = Entry(self.my_w_child) 
        self.txtPassword.grid(row=1, column=1, padx=5, pady=5)  
        self.txtPassword.config(show='*')
                
        # Pasang Button
        self.btnLogin = tk.Button(self.my_w_child, text='Login', fg="white", bg="blue",
            command=self.onLogin)
        self.btnLogin.grid(row=2, column=0, padx=5, pady=5) 

        self.btnCancel = tk.Button(self.my_w_child, text='Cancel', fg="white", bg="red",
            command=self.onLogout)
        self.btnCancel.grid(row=2, column=1, padx=5, pady=5) 
        
    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = Users()
        B =[]
        A.username = u
        A.password = p
        B = A.Login()
        
        if(B[0]=='True'):           
            if(B[1]=='petugas'):
                messagebox.showinfo("showinfo","Anda login sebagai Petugas")
                self.my_w_child.destroy()
                self.menuPetugas()
            elif(B[1]=='manajer'):
                messagebox.showinfo("showinfo","Anda login sebagai Manajer")
                self.my_w_child.destroy() 
                self.menuManajer()
            elif(B[1]=='direktur'):
                messagebox.showinfo("showinfo","Anda login sebagai Direktur")
                self.my_w_child.destroy()
                self.menuDirektur()
            else: 
                messagebox.showinfo("showinfo", "Maaf, User tidak dikenal")    
            
        else:
            messagebox.showinfo("showinfo", "Login Not Valid")   

    def onLogout(self):
        self.aturKomponen()
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Dashboard(root, "Dashboard Aplikasi")
    root.mainloop() 