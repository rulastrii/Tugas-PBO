import pymysql

def get_db():
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",  # Ganti dengan kata sandi yang benar
        database="pbo2",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

#CREATE TABLE mahasiswa (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    nim VARCHAR(20) NOT NULL,
#    nama VARCHAR(255) NOT NULL,
#    tempat_lahir VARCHAR(100),
#    tanggal_lahir DATE,
#    jenis_kelamin ENUM('Laki-laki', 'Perempuan'),
#    jurusan ENUM('Teknik Informatika', 'Kimia', 'Olahraga', 'Matematika'),
#    alamat TEXT,
#    gambar VARCHAR(255) -- path untuk menyimpan lokasi file foto
#);
