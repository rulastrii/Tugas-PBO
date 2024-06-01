# app.py
from flask import Flask, request, send_file
from modules.dosen.DosenRoute import app_dosen
from modules.mahasiswa.MahasiswaRoute import app_mahasiswa
from core.CoreModel import MahasiswaModel

app = Flask(__name__)
app.register_blueprint(app_dosen, url_prefix='/dosen')
app.register_blueprint(app_mahasiswa, url_prefix='/mahasiswa')

@app.route('/update_mahasiswa/<int:id>', methods=['POST'])
def update_mahasiswa(id):
    # Mengambil data dari form
    update_data = request.form.to_dict()

    # Mengambil file gambar jika ada
    if 'gambar' in request.files:
        gambar = request.files['gambar']
        update_data['gambar'] = gambar

    mahasiswa_model = MahasiswaModel()
    mahasiswa_model.update(id, update_data)

    return "Mahasiswa updated successfully"

if __name__ == '__main__':
    app.run(debug=True)
