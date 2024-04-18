from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    nama = "Rulastri"
    return render_template('hello.html', nama=nama)

@app.route('/template')
def template():
    nim = "220510071"
    nama = "Rulastri"
    prodi = "Teknik Informatika"
    return render_template('template.html', nim=nim, nama=nama, prodi=prodi)

@app.route('/hello')
def hello():
    nim = request.args.get('nim')
    return render_template('hello.html', nama=nim)

if __name__ == '__main__':
    app.run(debug=True, port=3001)
