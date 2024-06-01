# file CoreModel.py
from connection import get_db
from interfaces.DosenInterface import *
from interfaces.MahasiswaInterface import *

class DosenModel(DosenInterface):
    def __init__(self):
        super().__init__()
        self.table_name = "dosen"
        self.table_id = "id"
        self.nidn = "nidn"
        self.nama = "nama"

    def all(self):
        connection = get_db()
        cursor = connection.cursor()

        query = f"SELECT * FROM {self.table_name};"
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    def store(self):
        connection = get_db()
        cursor = connection.cursor()
        set_columns = []
        set_placeholders = []
        set_values = []

        for key, value in vars(self).items():
            if key not in ['table_name', 'table_id']:
                set_columns.append(key)
                set_placeholders.append('%s')
                set_values.append(value)

        columns_string = ', '.join(set_columns)
        placeholders_string = ', '.join(set_placeholders)

        sql_query = f"INSERT INTO {self.table_name} ({columns_string}) VALUES ({placeholders_string});"
        cursor.execute(sql_query, tuple(set_values))

        connection.commit()
        cursor.close()
        connection.close()

    def find(self, id):
        connection = get_db()
        cursor = connection.cursor()

        query = f"SELECT * FROM {self.table_name} WHERE {self.table_id} = %s LIMIT 1;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def update(self, id, obj):
        connection = get_db()
        cursor = connection.cursor()

        set_columns = []
        set_values = []

        for key, value in vars(obj).items():
            if key not in ['table_name', 'table_id']:
                column = f"{key} = %s"
                set_columns.append(column)
                set_values.append(value)

        set_column_string = ', '.join(set_columns)
        sql_query = f"UPDATE {self.table_name} SET {set_column_string} WHERE {self.table_id} = %s;"
        set_values.append(id)
        cursor.execute(sql_query, tuple(set_values))

        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, id):
        connection = get_db()
        cursor = connection.cursor()

        query = f"DELETE FROM {self.table_name} WHERE {self.table_id} = %s;"
        cursor.execute(query, (id,))

        connection.commit()
        cursor.close()
        connection.close()

    def search(self, query):
        connection = get_db()
        cursor = connection.cursor()

        search_query = f"%{query}%"
        sql_query = f"SELECT * FROM {self.table_name} WHERE {self.nidn} LIKE %s OR {self.nama} LIKE %s;"
        cursor.execute(sql_query, (search_query, search_query))
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

class MahasiswaModel(MahasiswaInterface):
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

    def all(self):
        connection = get_db()
        cursor = connection.cursor()

        query = f"SELECT * FROM {self.table_name};"
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    def store(self, mahasiswa_obj):
        connection = get_db()
        cursor = connection.cursor()
        set_columns = []
        set_placeholders = []
        set_values = []

        for key, value in vars(mahasiswa_obj).items():
            if key not in ['table_name', 'table_id']:
                set_columns.append(key)
                set_placeholders.append('%s')
                set_values.append(value)

        columns_string = ', '.join(set_columns)
        placeholders_string = ', '.join(set_placeholders)

        sql_query = f"INSERT INTO {self.table_name} ({columns_string}) VALUES ({placeholders_string});"
        cursor.execute(sql_query, tuple(set_values))

        if 'gambar' in mahasiswa_obj.__dict__ and hasattr(mahasiswa_obj.gambar, 'save'):
            gambar = mahasiswa_obj.gambar
            gambar.save(f'static/uploads/{gambar.filename}')
            sql_query = f"UPDATE {self.table_name} SET gambar = %s WHERE id = %s;"
            cursor.execute(sql_query, (gambar.filename, mahasiswa_obj.id))

        connection.commit()
        cursor.close()
        connection.close()

    def update(self, id, dictionary):
        connection = get_db()
        cursor = connection.cursor()

        set_columns = []
        set_values = []

        for key, value in dictionary.items():
            if key not in ['table_name', 'table_id']:
                column = f"{key} = %s"
                set_columns.append(column)
                set_values.append(value)

        set_column_string = ', '.join(set_columns)
        sql_query = f"UPDATE {self.table_name} SET {set_column_string} WHERE {self.table_id} = %s;"
        set_values.append(id)
        cursor.execute(sql_query, tuple(set_values))

        # Mengecek apakah gambar adalah file yang dapat disimpan
        if 'gambar' in dictionary and hasattr(dictionary['gambar'], 'save'):
            gambar = dictionary['gambar']
            gambar.save(f'static/gambar/{gambar.filename}')
            sql_query = f"UPDATE {self.table_name} SET gambar = %s WHERE id = %s;"
            cursor.execute(sql_query, (gambar.filename, id))

        connection.commit()
        cursor.close()
        connection.close()

    def find(self, id):
        connection = get_db()
        cursor = connection.cursor()

        query = f"SELECT * FROM {self.table_name} WHERE {self.table_id} = %s LIMIT 1;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def delete(self, id):
        connection = get_db()
        cursor = connection.cursor()

        query = f"DELETE FROM {self.table_name} WHERE {self.table_id} = %s;"
        cursor.execute(query, (id,))

        connection.commit()
        cursor.close()
        connection.close()

    def search(self, query):
        connection = get_db()
        cursor = connection.cursor()

        search_query = f"%{query}%"
        sql_query = f"SELECT * FROM {self.table_name} WHERE {self.nim} LIKE %s OR {self.nama} LIKE %s;"
        cursor.execute(sql_query, (search_query, search_query))
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results
