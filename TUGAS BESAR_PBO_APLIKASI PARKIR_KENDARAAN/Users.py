from db import DBConnection as mydb
import hashlib
import bcrypt


class Users:
    def __init__(self):
        self.__iduser=None
        self.__username=None
        self.__password=None
        self.__rolename=None
        self.__uservalid = None
        self.__passwordvalid = None
        self.__loginvalid = None    
    
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def iduser(self):
        return self.__iduser
    @property
    def username(self):
        return self.__username
        
    @username.setter
    def username(self, value):
        self.__username = value
    @property
    def password(self):
        return self.__password
        
    @password.setter
    def password(self, value):
        self.__password = value
    @property
    def rolename(self):
        return self.__rolename
        
    @rolename.setter
    def rolename(self, value):
        self.__rolename = value
        
    def Login(self):
        a=str(self.__username)
        pwd = hashlib.md5(self.__password.encode("utf-8")).hexdigest()
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM users WHERE username='" + b + "' and password='" + pwd + "'"
        self.result = self.conn.findOne(sql)
        val = []
        if(self.result!=None):
            self.__username = self.result[1]
            self.__password = self.result[2]
            self.__rolename = self.result[3]
            self.affected = self.conn.cursor.rowcount
            val.append('True')
            val.append(self.__rolename)
        else:
            self.__username = ''
            self.__password = ''
            self.__rolename = ''
            self.affected = 0
            val.append('')
            val.append('')
        self.conn.disconnect
        return val
   
    def cekUsername(self, username):
        self.conn = mydb()
        sql="SELECT * FROM users WHERE username='" + username + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__iduser = self.result[0]
           self.__username = self.result[1]
           self.__password = self.result[2]
           self.__rolename = self.result[3]
           self.affected = self.conn.cursor.rowcount
           self.__uservalid = True
        else:
           self.__iduser = ''
           self.__username = ''
           self.__password = ''
           self.__rolename = ''
           self.affected = 0
           self.__uservalid = False
        return self.__uservalid
    def cekPassword(self, password):
        hashedpass=self.__password.encode('utf-8')
        c = password.encode('utf-8')
        d = bcrypt.checkpw(c, hashedpass)
        if(d):
            self.__passwordvalid=True
        else:
            self.__passwordvalid=False
        return self.__passwordvalid
    def Validasi(self, email, password):
        a = self.cekUsername(email)
        if(a==True):
            b = self.cekPassword(password)
            if(b==True):
                self.__loginvalid=True
            else:
                self.__loginvalid=False
        else:
            self.__loginvalid=False
        
        val = []
        val = [self.__level, self.__loginvalid]
        return val
    def simpan(self):
        self.conn = mydb()
        val = (self.__username,self.__password,self.__rolename)
        sql="INSERT INTO Users (username,password,rolename) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__username,self.__password,self.__rolename, id)
        sql="UPDATE users SET username = %s,password = %s,rolename = %s WHERE iduser=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByUSERNAME(self, username):
        self.conn = mydb()
        val = (self.__password,self.__rolename, username)
        sql="UPDATE users SET password = %s,rolename = %s WHERE username=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM users WHERE iduser='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByUSERNAME(self, username):
        self.conn = mydb()
        sql="DELETE FROM users WHERE username='" + str(username) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM users WHERE iduser='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__iduser = self.result[0]
        self.__username = self.result[1]
        self.__password = self.result[2]
        self.__rolename = self.result[3]
        self.conn.disconnect
        return self.result
    def getByUSERNAME(self, username):
        a=str(username)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM users WHERE username='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__iduser = self.result[0]
           self.__username = self.result[1]
           self.__password = self.result[2]
           self.__rolename = self.result[3]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__iduser = ''
           self.__username = ''
           self.__password = ''
           self.__rolename = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM users"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,password FROM users"
        self.result = self.conn.findAll(sql)
        return self.result