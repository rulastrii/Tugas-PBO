'''
Nama    : Rulastri
Kelas   : TI22L
NIM     : 220511071
'''

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Sesuaikan dengan lokasi instalasi Tesseract di sistem Anda


class ImageToTextConverterApp:
    def __init__(self, parent, title):
        self.parent = parent       

        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)

#============================================================================

        self.image_label = tk.Label(root, text="Gambar:")
        self.image_label.pack()

        self.image_path = tk.StringVar()
        self.image_path_entry = tk.Entry(root, textvariable=self.image_path, state='disabled', width=40)
        self.image_path_entry.pack()

        self.browse_button = tk.Button(root, text="Cari Gambar",  fg= "white", bg="blue", command=self.browse_image)
        self.browse_button.pack(ipadx=50)

        self.convert_button = tk.Button(root, text="Convert ke Teks",  fg= "black", bg="red", command=self.convert_image)
        self.convert_button.pack()

        self.result_label = tk.Label(root, text="Hasil:")
        self.result_label.pack()

        self.result_text = tk.Text(root, height=10, width=40)
        self.result_text.pack()

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        self.image_path.set(file_path)

        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo

    def convert_image(self):
        image_path = self.image_path.get()
        if image_path:
            try:
                result_text = self.extract_text_from_image(image_path)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, result_text)
            except Exception as e:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Error: {str(e)}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please select an image.")

    def extract_text_from_image(self, image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    

    def onKeluar(self, event=None):

        self.parent.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextConverterApp(root, "Aplikasi Gambar to Teks")
    root.mainloop()
