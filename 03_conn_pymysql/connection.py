import pymysql

def get_db():
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="", 
            database="pbo2",
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection



#installed pymysql-1.1.0
#CREATE TABLE dosen (
#    id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
#    nidn VARCHAR(100) DEFAULT '',
#    nama VARCHAR(100) NOT NULL,
#    bidang VARCHAR(100) DEFAULT '',
#    PRIMARY KEY (id),
#    UNIQUE KEY nim (nidn)
#) ENGINE=InnoDB DEFAULT CHARSET=utf8;
