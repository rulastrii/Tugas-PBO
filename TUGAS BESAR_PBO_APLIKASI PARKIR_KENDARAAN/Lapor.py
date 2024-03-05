from db import DBConnection as mydb
class Lapor:
    def __init__(self):
        self.__id=None
        self.__nopolhilang=None
        self.__keterangan=None
        self.__tanggal=None
        self.__jamlapor=None
        self.__jenis=None
        self.__bukti=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nopolhilang(self):
        return self.__nopolhilang
        
    @nopolhilang.setter
    def nopolhilang(self, value):
        self.__nopolhilang = value
    @property
    def keterangan(self):
        return self.__keterangan
        
    @keterangan.setter
    def keterangan(self, value):
        self.__keterangan = value
    @property
    def tanggal(self):
        return self.__tanggal
        
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value
    @property
    def jamlapor(self):
        return self.__jamlapor
        
    @jamlapor.setter
    def jamlapor(self, value):
        self.__jamlapor = value
    @property
    def jenis(self):
        return self.__jenis
        
    @jenis.setter
    def jenis(self, value):
        self.__jenis = value
    @property
    def bukti(self):
        return self.__bukti
        
    @bukti.setter
    def bukti(self, value):
        self.__bukti = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nopolhilang,self.__keterangan,self.__tanggal,self.__jamlapor,self.__jenis,self.__bukti)
        sql="INSERT INTO Lapor (nopolhilang,keterangan,tanggal,jamlapor,jenis,bukti) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nopolhilang,self.__keterangan,self.__tanggal,self.__jamlapor,self.__jenis,self.__bukti, id)
        sql="UPDATE lapor SET nopolhilang = %s,keterangan = %s,tanggal = %s,jamlapor = %s,jenis = %s,bukti = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNOPOLHILANG(self, nopolhilang):
        self.conn = mydb()
        val = (self.__keterangan,self.__tanggal,self.__jamlapor,self.__jenis,self.__bukti, nopolhilang)
        sql="UPDATE lapor SET keterangan = %s,tanggal = %s,jamlapor = %s,jenis = %s,bukti = %s WHERE nopolhilang=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM lapor WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNOPOLHILANG(self, nopolhilang):
        self.conn = mydb()
        sql="DELETE FROM lapor WHERE nopolhilang='" + str(nopolhilang) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM lapor WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nopolhilang = self.result[1]
        self.__keterangan = self.result[2]
        self.__tanggal = self.result[3]
        self.__jamlapor = self.result[4]
        self.__jenis = self.result[5]
        self.__bukti = self.result[6]
        self.conn.disconnect
        return self.result
    def getByNOPOLHILANG(self, nopolhilang):
        a=str(nopolhilang)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM lapor WHERE nopolhilang='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nopolhilang = self.result[1]
           self.__keterangan = self.result[2]
           self.__tanggal = self.result[3]
           self.__jamlapor = self.result[4]
           self.__jenis = self.result[5]
           self.__bukti = self.result[6]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nopolhilang = ''
           self.__keterangan = ''
           self.__tanggal = ''
           self.__jamlapor = ''
           self.__jenis = ''
           self.__bukti = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM lapor"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,keterangan FROM lapor"
        self.result = self.conn.findAll(sql)
        return self.result   