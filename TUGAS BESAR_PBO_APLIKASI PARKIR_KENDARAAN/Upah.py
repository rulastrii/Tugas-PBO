from db import DBConnection as mydb
class Upah:
    def __init__(self):
        self.__id=None
        self.__nama=None
        self.__username=None
        self.__rolename=None
        self.__status=None
        self.__gaji=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def username(self):
        return self.__username
        
    @username.setter
    def username(self, value):
        self.__username = value
    @property
    def rolename(self):
        return self.__rolename
        
    @rolename.setter
    def rolename(self, value):
        self.__rolename = value
    @property
    def status(self):
        return self.__status
        
    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def gaji(self):
        return self.__gaji
        
    @gaji.setter
    def gaji(self, value):
        self.__gaji = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama,self.__username,self.__rolename,self.__status,self.__gaji)
        sql="INSERT INTO Upah (nama,username,rolename,status,gaji) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama,self.__username,self.__rolename,self.__status,self.__gaji, id)
        sql="UPDATE upah SET nama = %s,username = %s,rolename = %s,status = %s,gaji = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByUSERNAME(self, username):
        self.conn = mydb()
        val = (self.__nama,self.__rolename,self.__status,self.__gaji, username)
        sql="UPDATE upah SET nama = %s,rolename = %s,status = %s,gaji = %s WHERE username=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM upah WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByUSERNAME(self, username):
        self.conn = mydb()
        sql="DELETE FROM upah WHERE username='" + str(username) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM upah WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama = self.result[1]
        self.__username = self.result[2]
        self.__rolename = self.result[3]
        self.__status = self.result[4]
        self.__gaji = self.result[5]
        self.conn.disconnect
        return self.result
    def getByUSERNAME(self, username):
        a=str(username)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM upah WHERE username='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama = self.result[1]
           self.__username = self.result[2]
           self.__rolename = self.result[3]
           self.__status = self.result[4]
           self.__gaji = self.result[5]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama = ''
           self.__username = ''
           self.__rolename = ''
           self.__status = ''
           self.__gaji = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM upah"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,username FROM upah"
        self.result = self.conn.findAll(sql)
        return self.result