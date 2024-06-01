import pymysql

def get_db():
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",  # Ganti dengan kata sandi yang benar
            database="pbo2",
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print("Error connecting to MySQL:", e)
        return None

