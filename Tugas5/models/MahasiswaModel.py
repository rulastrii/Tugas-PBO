from core.CoreModel import CoreModel
class MahasiswaModel(CoreModel):
    def __init__(self):
        super().__init__()
        self.table_name = "mahasiswa"
        self.table_id = "id"
        self.nim = "nim"
        self.nama = "nama"
        self.tempat_lahir = "tempat_lahir"
        self.tanggal_lahir = "tanggal_lahir"
        self.jenis_kelamin = "jenis_kelamin"
        self.jurusan = "jurusan"
        self.alamat = "alamat"
        self.gambar = "gambar"
        self.id = None  # Add this line to include an id attribute

    # Rest of your code...