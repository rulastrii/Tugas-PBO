# file DosenModel.py
from core.CoreModel import DosenModel

class DosenModel(DosenModel):
    def __init__(self):
        super().__init__()
        self.table_name = "dosen"
        self.table_id = "id"
        self.nidn = "nidn"
        self.nama = "nama"
