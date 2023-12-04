'''
Nama    : Rulastri
Kelas   : TI22L
NIM     : 220511071
'''

import tkinter as tk
from tkinter import Label, Entry, Button
import pyttsx3

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Pengubah Teks Menjadi Suara")

        self.label = Label(master, text="Masukkan teks:")
        self.label.pack()

        self.text_entry = Entry(master, width=50)
        self.text_entry.pack()

        self.convert_button = Button(master, text="Convert Teks",  fg= "white", bg="blue", command=self.convert_text)
        self.convert_button.pack()

    def convert_text(self):
        text_to_speak = self.text_entry.get()
        if text_to_speak:
            self.speak(text_to_speak)
        else:
            self.speak("Tidak ada teks yang dimasukkan.")

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
