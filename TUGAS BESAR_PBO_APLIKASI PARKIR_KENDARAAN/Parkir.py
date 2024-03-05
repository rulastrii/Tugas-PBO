from db import DBConnection as mydb
class Parkir:
    def __init__(self):
        self.__id=None
        self.__nopol=None
        self.__tanggal=None
        self.__jenis=None
        self.__masuk=None
        self.__keluar=None
        self.__tarif=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nopol(self):
        return self.__nopol
        
    @nopol.setter
    def nopol(self, value):
        self.__nopol = value
    @property
    def tanggal(self):
        return self.__tanggal
        
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value
    @property
    def jenis(self):
        return self.__jenis
        
    @jenis.setter
    def jenis(self, value):
        self.__jenis = value
    @property
    def masuk(self):
        return self.__masuk
        
    @masuk.setter
    def masuk(self, value):
        self.__masuk = value
    @property
    def keluar(self):
        return self.__keluar
        
    @keluar.setter
    def keluar(self, value):
        self.__keluar = value
    @property
    def tarif(self):
        return self.__tarif
        
    @tarif.setter
    def tarif(self, value):
        self.__tarif = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nopol,self.__tanggal,self.__jenis,self.__masuk,self.__keluar,self.__tarif)
        sql="INSERT INTO Parkir (nopol,tanggal,jenis,masuk,keluar,tarif) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nopol,self.__tanggal,self.__jenis,self.__masuk,self.__keluar,self.__tarif, id)
        sql="UPDATE parkir SET nopol = %s,tanggal = %s,jenis = %s,masuk = %s,keluar = %s,tarif = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNOPOL(self, nopol):
        self.conn = mydb()
        val = (self.__tanggal,self.__jenis,self.__masuk,self.__keluar,self.__tarif, nopol)
        sql="UPDATE parkir SET tanggal = %s,jenis = %s,masuk = %s,keluar = %s,tarif = %s WHERE nopol=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM parkir WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNOPOL(self, nopol):
        self.conn = mydb()
        sql="DELETE FROM parkir WHERE nopol='" + str(nopol) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM parkir WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nopol = self.result[1]
        self.__tanggal = self.result[2]
        self.__jenis = self.result[3]
        self.__masuk = self.result[4]
        self.__keluar = self.result[5]
        self.__tarif = self.result[6]
        self.conn.disconnect
        return self.result
    def getByNOPOL(self, nopol):
        a=str(nopol)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM parkir WHERE nopol='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nopol = self.result[1]
           self.__tanggal = self.result[2]
           self.__jenis = self.result[3]
           self.__masuk = self.result[4]
           self.__keluar = self.result[5]
           self.__tarif = self.result[6]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nopol = ''
           self.__tanggal = ''
           self.__jenis = ''
           self.__masuk = ''
           self.__keluar = ''
           self.__tarif = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM parkir"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,tanggal FROM parkir"
        self.result = self.conn.findAll(sql)
        return self.result 