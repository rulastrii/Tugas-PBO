from flask import render_template, request, redirect, url_for
from models.MahasiswaModel import *

class MahasiswaView:
    @staticmethod
    def index():
        data = MahasiswaModel().all()
        return render_template('mahasiswa_index.html', data=data)

    @staticmethod
    def create():
        return render_template('mahasiswa_create.html')

    @staticmethod
    def store():
        mahasiswa_obj = MahasiswaModel()
        post = request.form
        mahasiswa_obj.nim = post['nim']
        mahasiswa_obj.nama = post['nama']
        mahasiswa_obj.tempat_lahir = post['tempat_lahir']
        mahasiswa_obj.tanggal_lahir = post['tanggal_lahir']
        mahasiswa_obj.jenis_kelamin = post['jenis_kelamin']
        mahasiswa_obj.jurusan = post['jurusan']
        mahasiswa_obj.alamat = post['alamat']
        mahasiswa_obj.gambar = request.files['gambar']
        mahasiswa_obj.store(mahasiswa_obj)
        return redirect('/mahasiswa')

    @staticmethod
    def edit(mahasiswa_id):
        obj = MahasiswaModel().find(mahasiswa_id)
        return render_template('mahasiswa_edit.html', obj=obj)

    
    @staticmethod
    def update(mahasiswa_id):
        data = MahasiswaModel().find(mahasiswa_id)
        if data:
            post = request.form
            mahasiswa_obj = MahasiswaModel()
            mahasiswa_obj.nim = post['nim']
            mahasiswa_obj.nama = post['nama']
            mahasiswa_obj.tempat_lahir = post['tempat_lahir']
            mahasiswa_obj.tanggal_lahir = post['tanggal_lahir']
            mahasiswa_obj.jenis_kelamin = post['jenis_kelamin']
            mahasiswa_obj.jurusan = post['jurusan']
            mahasiswa_obj.alamat = post['alamat']
            mahasiswa_obj.gambar = request.files['gambar']
            dictionary = {
                'nim': mahasiswa_obj.nim,
                'nama': mahasiswa_obj.nama,
                'tempat_lahir': mahasiswa_obj.tempat_lahir,
                'tanggal_lahir': mahasiswa_obj.tanggal_lahir,
                'jenis_kelamin': mahasiswa_obj.jenis_kelamin,
                'jurusan': mahasiswa_obj.jurusan,
                'alamat': mahasiswa_obj.alamat,
                'gambar': mahasiswa_obj.gambar
            }
            CoreModel().update(mahasiswa_id, dictionary)
            return redirect('/mahasiswa')
        else:
            return redirect('/mahasiswa')

    @staticmethod
    def delete(mahasiswa_id):
        data = MahasiswaModel().find(mahasiswa_id)
        if data:
            MahasiswaModel().delete(mahasiswa_id)
            return redirect('/mahasiswa')
        else:
            return redirect('/mahasiswa')