# routes/MahasiswaViews.py
from flask import *
import os
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
        gambar = request.files['gambar']
        mahasiswa_obj.gambar = gambar.filename
        if not os.path.exists('static'):
            os.makedirs('static')
        if not os.path.exists('static/gambar'):
            os.makedirs('static/gambar')
        gambar.save('static/gambar/' + gambar.filename)
        MahasiswaModel.store(mahasiswa_obj)
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
        if 'gambar' in request.files:
            file = request.files['gambar']
            if file.filename == '':
                return 'Error: No selected file'
            if file:
                filename = file.filename
                file.save(os.path.join('static/gambar', filename))
                mahasiswa_obj.gambar = filename
            MahasiswaModel.update(mahasiswa_id, mahasiswa_obj)
            return redirect('/mahasiswa')
        else:
            return redirect(request.referrer)
    
    @staticmethod
    def delete(mahasiswa_id):
        data = MahasiswaModel().find(mahasiswa_id)
        if data:
            MahasiswaModel.delete(mahasiswa_id)
            return redirect('/mahasiswa')
        else:
            return redirect(request.referrer)