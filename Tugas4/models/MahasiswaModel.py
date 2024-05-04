from connection import get_db
from interfaces.MahasiswaInterface import *

class MahasiswaModel(MahasiswaInterface):

    @staticmethod
    def all():
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM mahasiswa"
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results
    
    @staticmethod
    def find(mahasiswa_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM mahasiswa WHERE id = %s LIMIT 1"
        cursor.execute(query, (mahasiswa_id))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result
    
    @staticmethod
    def store(mahasiswa_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "INSERT INTO mahasiswa (nim, nama, tempat_lahir, tanggal_lahir, jenis_kelamin, jurusan, alamat, gambar) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (mahasiswa_obj.nim, mahasiswa_obj.nama, mahasiswa_obj.tempat_lahir, mahasiswa_obj.tanggal_lahir, mahasiswa_obj.jenis_kelamin, mahasiswa_obj.jurusan, mahasiswa_obj.alamat, mahasiswa_obj.gambar))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update(mahasiswa_id, mahasiswa_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "UPDATE mahasiswa SET nim = %s, nama = %s, tempat_lahir = %s, tanggal_lahir = %s, jenis_kelamin = %s, jurusan = %s, alamat = %s, gambar = %s WHERE id = %s"
        cursor.execute(query, (mahasiswa_obj.nim, mahasiswa_obj.nama, mahasiswa_obj.tempat_lahir, mahasiswa_obj.tanggal_lahir, mahasiswa_obj.jenis_kelamin, mahasiswa_obj.jurusan, mahasiswa_obj.alamat, mahasiswa_obj.gambar, mahasiswa_id))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(mahasiswa_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "DELETE FROM mahasiswa WHERE id = %s"
        cursor.execute(query, (mahasiswa_id))

        connection.commit()
        cursor.close()
        connection.close()