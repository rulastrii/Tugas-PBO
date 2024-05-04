# app.py
from flask import Flask, request, send_file
import os
from routes.DosenRoute import app_dosen
from routes.MahasiswaRoute import app_mahasiswa

app = Flask(__name__)

# Create directories if they do not exist
if not os.path.exists('static'):
    os.makedirs('static')
if not os.path.exists('static/gambar'):
    os.makedirs('static/gambar')

@app.route('/upload', methods=['POST'])
def upload():
    if 'gambar' not in request.files:
        return 'Error: No file part'
    file = request.files['gambar']
    if file.filename == '':
        return 'Error: No selected file'
    if file:
        filename = file.filename
        file.save(os.path.join('static/gambar', filename))
        return 'File uploaded successfully'

app.register_blueprint(app_dosen, url_prefix='/dosen')
app.register_blueprint(app_mahasiswa, url_prefix='/mahasiswa')

if __name__ == '__main__':
    app.run(debug=True, port="3004")
