'''
Nama    : Rulastri
Kelas   : TI22L
NIM     : 220511071
'''

import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator")
        self.root.geometry("600x400")

        self.translator = Translator()

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Rulastri (220511071)", font=("Helvetica", 16), bg='white', fg='Black')
        self.title_label.pack(pady=10)
        # Label
        self.label = ttk.Label(self.root, text="Masukkan Teks:")
        self.label.pack(pady=10)

        # Text Entry
        self.text_entry = ttk.Entry(self.root, width=40)
        self.text_entry.pack(pady=10)

        # Language Selection
        self.lang_label = ttk.Label(self.root, text="Pilih Bahasa:")
        self.lang_label.pack()

        self.languages = ["english", "filipino", "vietnamese"]
        self.lang_var = tk.StringVar()
        self.lang_var.set(self.languages[0])

        self.lang_menu = ttk.Combobox(self.root, textvariable=self.lang_var, values=self.languages)
        self.lang_menu.pack(pady=10)

        # Translate Button
        self.translate_button = ttk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        # Output Label
        self.output_label = ttk.Label(self.root, text="")
        self.output_label.pack(pady=10)

    def translate_text(self):
        input_text = self.text_entry.get()
        target_lang = self.lang_var.get()

        try:
            translation = self.translator.translate(input_text, dest=target_lang)
            translated_text = translation.text
            self.output_label.config(text=f"Trasnlate: {translated_text}")
        except Exception as e:
            print(f"Error during translation: {e}")
            self.output_label.config(text="Translation error")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
