import os
from flask import Flask, render_template, request, redirect, url_for
from modules.mahasiswa.MahasiswaModel import MahasiswaModel
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class MahasiswaView:
    @staticmethod
    def index():
        data = MahasiswaModel().all()
        return render_template('mahasiswa_index.html', data=data)
    
    @staticmethod
    def search():
        query = request.args.get('query')
        data = MahasiswaModel().search(query)
        return render_template('mahasiswa_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('mahasiswa_create.html')

    @staticmethod
    def store():
        post = request.form
        mahasiswa_obj = MahasiswaModel()
        mahasiswa_obj.nim = post['nim']
        mahasiswa_obj.nama = post['nama']
        mahasiswa_obj.tempat_lahir = post['tempat_lahir']
        mahasiswa_obj.tanggal_lahir = post['tanggal_lahir']
        mahasiswa_obj.jenis_kelamin = post['jenis_kelamin']
        mahasiswa_obj.jurusan = post['jurusan']
        mahasiswa_obj.alamat = post['alamat']

        file = request.files['gambar']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file.save(file_path)
            mahasiswa_obj.gambar = filename

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
            mahasiswa_obj.id = mahasiswa_id
            mahasiswa_obj.nim = post['nim']
            mahasiswa_obj.nama = post['nama']
            mahasiswa_obj.tempat_lahir = post['tempat_lahir']
            mahasiswa_obj.tanggal_lahir = post['tanggal_lahir']
            mahasiswa_obj.jenis_kelamin = post['jenis_kelamin']
            mahasiswa_obj.jurusan = post['jurusan']
            mahasiswa_obj.alamat = post['alamat']

            file = request.files['gambar']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                file.save(file_path)
                mahasiswa_obj.gambar = filename

            update_data = {
                'nim': mahasiswa_obj.nim,
                'nama': mahasiswa_obj.nama,
                'tempat_lahir': mahasiswa_obj.tempat_lahir,
                'tanggal_lahir': mahasiswa_obj.tanggal_lahir,
                'jenis_kelamin': mahasiswa_obj.jenis_kelamin,
                'jurusan': mahasiswa_obj.jurusan,
                'alamat': mahasiswa_obj.alamat,
                'gambar': mahasiswa_obj.gambar,
            }

            mahasiswa_obj.update(mahasiswa_id, update_data)
            return redirect('/mahasiswa')
        else:
            return redirect(request.referrer)
        
    @staticmethod
    def delete(mahasiswa_id):
        data = MahasiswaModel().find(mahasiswa_id)
        if data:
            MahasiswaModel().delete(mahasiswa_id)
            return redirect('/mahasiswa')
        else:
            return redirect(request.referrer)
