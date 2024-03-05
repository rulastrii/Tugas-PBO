import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class KalkulatorBola(QWidget):
    def __init__(self):
        super().__init__()

        # user interface
        self.init_ui()

    def init_ui(self):
        # pembuatan label dan inputan
        self.label_jarijari = QLabel('Masukan Jari-jari Bola:')
        self.input_jarijari = QLineEdit(self)
        self.input_jarijari.setPlaceholderText('Masukan Jari-jari')

        # label hasil
        self.label_hasil = QLabel('Hasil:')
        self.label_hasil_luas = QLabel('Luas Bola:')
        self.label_hasil_volume = QLabel('Volume Bola:')

        # tombol hitung
        self.tombol_hitung = QPushButton('Hitung', self)
        self.tombol_hitung.clicked.connect(self.hitung)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_jarijari)
        layout.addWidget(self.input_jarijari)
        layout.addWidget(self.label_hasil)
        layout.addWidget(self.label_hasil_luas)
        layout.addWidget(self.label_hasil_volume)
        layout.addWidget(self.tombol_hitung)
        
        # layout untuk tampilan pertama dibuka
        self.setLayout(layout)

        # judul program
        self.setWindowTitle('Kalkulator Bola')
        self.setGeometry(100, 100, 300, 200)

    def hitung(self):
        try:
            # ambil jari-jari dari inputan user
            jarijari = float(self.input_jarijari.text())
            
            # kondisi apakah jari-jari merupakan kelipatan 7 atau bukan untuk menentukan phi
            
            if jarijari % 7 == 0:
                phi = 22/7
            else:
                phi = 3.14


            # rumus hitung luas dan volume
            luas = 4 * phi * jarijari ** 2
            volume = (4 / 3) * phi * jarijari ** 3

            # menampilkan hasil
            self.label_hasil.setText('Hasil :')
            self.label_hasil_luas.setText(f'Luas Bola: {luas:.2f}')
            self.label_hasil_volume.setText(f'Volume Bola: {volume:.2f}')

        # jika inputan bukan angka
        except ValueError:
            self.label_hasil.setText('')
            self.label_hasil_luas.setText('Error: Masukan bukan angka')
            self.label_hasil_volume.setText('Masukan Tidak Valid')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = KalkulatorBola()
    calculator.show()
    sys.exit(app.exec_())
