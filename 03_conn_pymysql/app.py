from flask import Flask, render_template, request, redirect, url_for
from connection import get_db

app = Flask(__name__)
db = get_db()

@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM dosen")
    data = cursor.fetchall()
    cursor.close()
    return render_template("index.html", dosen=data)

@app.route("/insert", methods=["POST"])
def insert():
    nidn = request.form["nidn"]
    nama = request.form["nama"]
    cursor = db.cursor()
    cursor.execute("INSERT INTO dosen (nidn, nama) VALUES (%s, %s)", (nidn, nama))
    db.commit()
    cursor.close()
    return redirect(url_for("index"))

@app.route("/update/<string:nidn>", methods=["POST"])
def update(nidn):
    new_nama = request.form["new_nama"]
    cursor = db.cursor()
    cursor.execute("UPDATE dosen SET nama = %s WHERE nidn = %s", (new_nama, nidn))
    db.commit()
    cursor.close()
    return redirect(url_for("index"))

@app.route("/delete/<string:nidn>", methods=["POST"])
def delete(nidn):
    cursor = db.cursor()
    cursor.execute("DELETE FROM dosen WHERE nidn = %s", (nidn,))
    db.commit()
    cursor.close()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True, port=3003)
