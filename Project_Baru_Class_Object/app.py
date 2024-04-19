from flask import Flask, render_template

app = Flask(__name__)
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, angkatan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan

class Dosen:
    def __init__(self, nidn, nama, spesialis):
        self.nidn = nidn
        self.nama = nama
        self.spesialis = spesialis

# Objek Mahasiswa
mahasiswa = [
    Mahasiswa("123", "John", "Teknik Informatika", 2019),
    Mahasiswa("222", "Wick", "Sistem Informasi", 2020),
    Mahasiswa("231", "Rifki", "Teknik Elektro", 2018),
    Mahasiswa("204", "Lastri", "Teknik Kimia", 2021),
    Mahasiswa("102", "Eka", "Teknik Mesin", 2017),
    # Tambahkan mahasiswa lainnya di sini
]

# Objek Dosen
dosen = [
    Dosen(111, "Agung", "Rekayasa Perangkat Lunak"),
    Dosen(222, "Bobon", "Jaringan komputer"),
    Dosen(333, "Candra", "Sains Data"),
    Dosen(444, "Deden", "Pemrograman mobile"),
    Dosen(555, "Endra", "Basisdata"),
    # Tambahkan dosen lainnya di sini
]

@app.route('/one')
def one_object():
    return render_template('one_object.html', mahasiswa=mahasiswa, dosen=dosen)

@app.route('/many')
def many_object():
    return render_template('many_object.html', mahasiswa=mahasiswa, dosen=dosen)

if __name__ == '__main__':
    app.run(debug=True, port=3004)